from library_manage_system.constants import *

class Library():
    def __init__(self, name, address: Address, books: list):
        self.__name = name
        self.__address = address
        self.__books = books

class Book():
    def __init__(self, bookInfo):
        self.__bookInfo = bookInfo
     
    @property
    def title(self):
        return self.__bookInfo.title

class BookItem(Book):
    def __init__(self, bookInfo: BookInfo,
                 bookItemInfo: BookItemInfo, 
                 rack: Rack):
        super(BookItem, self).__init__(bookInfo)
        self.__bookItemInfo = bookItemInfo
        self.__rack = rack
    
    def checkout(self):
        pass