from datetime import timedelta, date
import logging
logger = logging.getLogger(__name__)

from LMS.constants import Address, BookStatus, LibraryRule
from LMS.utils import ClockInterface
class Book():
    def __init__(self, author='', ISBN='', 
                 title='', subjects='', publisher=''):
        self.__author = author
        self.__ISBN = ISBN
        self.__title = title
        self.__subjects = subjects
        self.__publisher = publisher
     
    @property
    def author(self):
        return self.__author
    
    @property
    def ISBN(self):
        return self.__ISBN

    @property
    def title(self):
        return self.__title

    @property
    def subjects(self):
        return self.__subjects

    @property
    def publisher(self):
        return self.__publisher


class BookItem(Book):
    def __init__(self, author='', ISBN='', 
                 title='', subjects='', publisher='',
                 bib_num='', publication_year=None,
                 borrow_date=None, due_date=None, 
                 status: BookStatus=BookStatus.AVAILABLE):
        super(BookItem, self).__init__(author, ISBN, title, 
                                       subjects, publisher)
        
        self.__bib_num = bib_num
        self.__publication_year = publication_year
        
        self.__borrow_date = borrow_date
        self.__due_date = due_date
        self.__status = status

    def checkout(self):
        if self.status == BookStatus.AVAILABLE :
            self.status = BookStatus.LOANED
            self.borrow_date = ClockInterface().now()
            self.due_date += timedelta(days=LibraryRule.MAX_LENDING_DAYS)
            return True
        else:
            msg = """The book status is in {}. You can \ 
                     not check out this book!!""".format(self.bookStatus)
            logger.info(msg)
            return False

    @property
    def bib_num(self):
        return self.__bib_num

    @property
    def publication_year(self):
        return self.__publication_year
    
    @property
    def borrow_date(self):
        return self.__borrow_date

    @property
    def due_date(self):
        return self.__due_date

    @due_date.setter
    def due_date(self, due_date: date):
        self.__due_date = due_date

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: BookStatus):
        self.__status = status

class Library():
    def __init__(self, name, address: Address, book_items: dict):
        self.__name = name
        self.__address = address
        self.__book_items = book_items
        
    def __len__(self):
        return len(self.__book_items)

    @property
    def book_items(self):
        return self.__book_items

class BookIssueRecord():
    def __init__(self):
        self.__lending_history = []
        self.__lending_ongoing = {}
        self.__reservation_history = []
        self.__reservation_ongoing = {}

    def checkout_book(self, book_lending):
        member_id = book_lending
        self.__lending_ongoing[member_id] = self.__lending_ongoing.get(member_id, []) + [book_lending]
        return True
    
    def return_book(self, bib_num, member_id):
        lendings = self.__lending_ongoing[member_id]
        found = False
        for i , lending in enumerate(lendings):
            if lending.bib_num == bib_num:
                found = True
                break
        if found:
            lendings.pop(i)
            self.__lending_history.append(lending)
            return True
        logger.warning("Book lending detail is not found")
        return False
        

    def reserve_book(self):
        pass