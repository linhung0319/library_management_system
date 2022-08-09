class BookLending():
    def __init__(self, creationDate=None, dueDate=None, 
                 returnDate=None, bookItemBarcode='', memberId=''):
        self.__creationData = creationDate
        self.__dueDate = dueDate
        self.__returnDate = returnDate
        self.__bookItemBarcode = bookItemBarcode
        self.__memberId = memberId

    @property
    def returnDate(self):
        return self.__returnDate

    @property
    def bookItemBarcode(self):
        return self.__bookItemBarcode

    @classmethod
    def fetchLendingDetail(cls, bookItemBarcode):
        return cls(bookItemBarcode=bookItemBarcode)
