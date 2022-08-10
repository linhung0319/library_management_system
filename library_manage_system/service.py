class BookLending():
    def __init__(self, creationDate=None, dueDate=None, 
                 returnDate=None, bookItemBibNum=-1, memberId=''):
        self.__creationData = creationDate
        self.__dueDate = dueDate
        self.__returnDate = returnDate
        self.__bookItemBibNum = bookItemBibNum
        self.__memberId = memberId

    @property
    def returnDate(self):
        return self.__returnDate

    @property
    def bookItemBibNum(self):
        return self.__bookItemBibNum

    @classmethod
    def fetchLendingDetail(cls, bookItemBibNum):
        return cls(bookItemBibNum=bookItemBibNum)
