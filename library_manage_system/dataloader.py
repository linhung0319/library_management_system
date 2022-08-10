import pandas as pd

from library_manage_system.constants import DatasetInfo, Address
from library_manage_system.model import Library, BookItem

class Dataset():
    def __init__(self, info: DatasetInfo):
        self.__FILE_NAME = info.FILE_NAME
        self.__COLUMNS = info.COLUMNS
        self.__df = None

    def load(self):
        self.__df = pd.read_csv(self.__FILE_NAME)

    @property
    def df(self):
        return self.__df

    @property
    def FILE_NAME(self):
        return self.__FILE_NAME

    @property
    def COLUMNS(self):
        return self.__COLUMNS

class LibraryFactory():
    def __init__(self, dataset: Dataset, address: Address, name='Seattle Public Library'):
        self.__dataset = dataset
        self.__name = name
        self.__address = address

    def create(self):
        bookItems = BookItemsFactory(self.__dataset).create()
        return Library(name=self.__name, 
                       address=self.__address, 
                       bookItems=bookItems) 

class BookItemsFactory():
    def __init__(self, dataset: Dataset):
        self.__dataset = dataset

    def create(self):
        bookItems = []
        for _, row in self.__dataset.df.iterrows():
            bookItem = self.parseDataToBookItem(row)
            bookItems.append(bookItem)
        return bookItems

    def parseDataToBookItem(self, row):
        args = {}
        for k, v in self.__dataset.COLUMNS.items():
            args[k] = row[v]
        return BookItem(**args)
        



