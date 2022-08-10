from library_manage_system.constants import Address, BookStatus

class Library():
    def __init__(self, name, address: Address, bookItems: list):
        self.__name = name
        self.__address = address
        self.__bookItems = bookItems

class Book():
    def __init__(self, author='', ISBN='', 
                 title='', subjects='', publisher=''):
        self.__author = author
        self.__ISBN = ISBN
        self.__title = title
        self.__subjects = subjects
        self.__publisher = publisher
     
    @property
    def title(self):
        return self.__title

class BookItem(Book):
    def __init__(self, author='', ISBN='', 
                 title='', subjects='', publisher='',
                 bibNum='', publicationYear=None,
                 borrowed=None, dueDate=None, 
                 bookStatus: BookStatus=BookStatus.NONE):
        super(BookItem, self).__init__(author, ISBN, title, 
                                       subjects, publisher)
        
        self.__bibNum = bibNum
        self.__publicationYear = publicationYear
        
        self.__borrowed = borrowed
        self.__dueDate = dueDate
        self.__bookStatus = bookStatus

    @property
    def bibNum(self):
        return self.__bibNum

    def checkout(self):
        pass