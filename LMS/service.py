import logging
logger = logging.getLogger(__name__)

from LMS.model import Library
from utils import Search

class IssueService():
    def __init__(self, library: Library):
        self.__library = library
        self.__BookLending = BookLending

    def setBookLending(self, BookLending):
        self.__BookLending = BookLending

    def checkout(self, bibNum, memberId):
        lending_detail =  self.__BookLending.lendBookItem(self.__library, bibNum, memberId)
        if lending_detail:
            lending_detail.save_lending_detail
        return False

class BookLending():
    def __init__(self, borrow_date=None, due_date=None, 
                 return_date=None, bib_num=-1, member_id=''):
        self.__borrow_data = borrow_date
        self.__due_date = due_date
        self.__return_date = return_date
        self.__bib_num = bib_num
        self.__member_id = member_id

    @property
    def returnDate(self):
        return self.__returnDate

    @property
    def bookItemBibNum(self):
        return self.__bookItemBibNum

    def fetchLendingDetail(cls, bibNum, memberId):
        return cls()

    #def save_lenging_detail()

    @classmethod
    def lendBookItem(cls, library: Library, bibNum, memberId):
        # If bookItem exists in the library
        if bibNum in library.bookItems:
            bookItem = library.bookItems[bibNum]
            # If bookItem can be checkouted
            if bookItem.checkout():
                bookLendingDetail =  cls(borrowDate=bookItem.borrowDate,
                                   dueDate=bookItem.dueDate,
                                   bibNum=bibNum,
                                   memberId=memberId)
                Library.addcheckoutDetail(bookLendingDetail)
                return bookLendingDetail
        return False
            
            
