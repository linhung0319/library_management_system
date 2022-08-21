import pandas as pd

from LMS.constants import DatasetInfo, Address
from LMS.model import Library, BookItem

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
    def __init__(self, dataset: Dataset, address: Address=Address(), name='Seattle Public Library'):
        self.__dataset = dataset
        self.__name = name
        self.__address = address

    def create(self):
        book_items = BookItemsFactory(self.__dataset).create()
        return Library(name=self.__name, 
                       address=self.__address, 
                       book_items=book_items) 

class BookItemsFactory():
    def __init__(self, dataset: Dataset):
        self.__dataset = dataset

    def create(self):
        book_items = {}
        for _, row in self.__dataset.df.iterrows():
            book_item = self.parse_data_to_bookItem(row)
            book_items[book_item.bib_num] = book_item
        return book_items

    def parse_data_to_bookItem(self, row):
        args = {}
        for k, v in self.__dataset.COLUMNS.items():
            args[k] = row[v]
        return BookItem(**args)
        



