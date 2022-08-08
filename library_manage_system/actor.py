from abc import ABC
from library_manage_system.constants import *

class Author(Person):
    def __init__(self, name, address='', email='', phone='', description=''):
        super(Author, self).__init__(name, address, email, phone)
        self.description = description

class Account(ABC):
    def __init__(self, id, password, person, status):
        self.__id = id
        self.__password = password
        self.__person = person
        self.__status = status

    def reset_password(self, password):
        self.__password = password

class Librarian(Account):
    def __init__(self, id, password, person, status):
        super(Librarian, self).__init__(id, password, person, status)

    def addBookItem(self):
        pass
    
    def blockMember(self):
        pass

    def unblockMember(self):
        pass

class Member(Account):
    def __init__(self, id, password, person, status):
        super(Member, self).__init__(id, password, person, status)

    def getTotalCheckoutBook(self):
        pass