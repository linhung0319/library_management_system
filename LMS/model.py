import logging
logger = logging.getLogger(__name__)

from LMS.constants import Address, BookStatus

class Library():
    def __init__(self, name, address: Address, bookItems: list):
        self.__name = name
        self.__address = address
        self.__bookItems = bookItems

    def __len__(self):
        return len(self.__bookItems)

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
                 bibNum='', publicationYear=None,
                 borrowedDate=None, dueDate=None, 
                 bookStatus: BookStatus=BookStatus.AVAILABLE):
        super(BookItem, self).__init__(author, ISBN, title, 
                                       subjects, publisher)
        
        self.__bibNum = bibNum
        self.__publicationYear = publicationYear
        
        self.__borrowedDate = borrowedDate
        self.__dueDate = dueDate
        self.__bookStatus = bookStatus

    def checkout(self):
        if self.bookStatus == BookStatus.AVAILABLE:
            self.bookStatus = BookStatus.LOANED
            return True
        else:
            msg = """The book status is in {}. You can \ 
                     not check out this book!!""".format(self.bookStatus)
            logger.info(msg)
            return False

    @property
    def bibNum(self):
        return self.__bibNum

    @property
    def publicationYear(self):
        return self.__publicationYear
    
    @property
    def borrowedDate(self):
        return self.__borrowedDate

    @property
    def dueDate(self):
        return self.__dueDate

    @property
    def bookStatus(self):
        return self.__bookStatus

    @bookStatus.setter
    def bookStatus(self, status: BookStatus):
        self.__bookStatus = status