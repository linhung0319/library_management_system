from abc import ABC
import logging
logger = logging.getLogger(__name__)

from LMS.constants import AccountStatus, Person, LibraryRule
from LMS.service import IssueService

class Account(ABC):
    def __init__(self, issueService: IssueService,
                 accountId, password, 
                 person: Person=Person(), 
                 status: AccountStatus=AccountStatus.ACTIVE):
        self.__issueService = issueService
        self.__accountId = accountId
        self.__password = password
        self.__person = person
        self.__status = status
        self.__totalBooksCheckout = 0

    def reset_password(self, password):
        self.__password = password

    @property
    def totalBooksCheckout(self):
        return self.__totalBooksCheckout

    def checkout_book(self, bibNum):

        # System checks the number of books issued to the member
        if self.totalBooksCheckout >= LibraryRule.MAX_BOOKS_ISSUED_TO_A_USER:
            logger.info("The user has already checked-out maximum number of books\n")
            return False
        
        # System checks if the book has been reserved by any other member
       
        # System creates book checkout transaction
        # System update the status of the book to 'Loaned'
        if not self.__issueService.checkout(bibNum, self.__accountId):
            return False

        # System increments number of books issued to the member
        self.__totalBooksCheckout += 1

        # System marks any reservation Completed 
        # that the member had made against the book

        return True

class Librarian(Account):
    def __init__(self, issueService: IssueService,
                 accountId, password, 
                 person: Person=Person(), 
                 status: AccountStatus=AccountStatus.ACTIVE):
        super(Librarian, self).__init__(issueService, accountId, password, 
                                        person, status)

    def addBookItem(self):
        pass
    
    def blockMember(self):
        pass

    def unblockMember(self):
        pass

class Member(Account):
    def __init__(self, issueService: IssueService,
                 accountId, password, 
                 person: Person=Person(), 
                 status: AccountStatus=AccountStatus.ACTIVE):
        super(Member, self).__init__(issueService, accountId, password, 
                                     person, status)

    def getTotalCheckoutBook(self):
        pass