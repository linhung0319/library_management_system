from abc import ABC
from LMS.constants import AccountStatus, Person

class Account(ABC):
    def __init__(self, accountId, password, 
                 person: Person, status: AccountStatus):
        self.__accountId = accountId
        self.__password = password
        self.__person = person
        self.__status = status

    def reset_password(self, password):
        self.__password = password

class Librarian(Account):
    def __init__(self, accountId, password, 
                 person: Person, status: AccountStatus):
        super(Librarian, self).__init__(accountId, password, person, status)

    def addBookItem(self):
        pass
    
    def blockMember(self):
        pass

    def unblockMember(self):
        pass

class Member(Account):
    def __init__(self, accountId, password, 
                 person: Person, status: AccountStatus):
        super(Member, self).__init__(accountId, password, person, status)

    def getTotalCheckoutBook(self):
        pass