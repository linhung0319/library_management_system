import unittest
from LMS.dataloader import *
from LMS.constants import DatasetInfo, Address

class Test_BookItemsFactory(unittest.TestCase):
    def test_create(self):
        dI = DatasetInfo
        dataset = Dataset(dI)
        dataset.load()
        oneBookData = dataset.df.iloc[[0]]

        TRUE_bibNum = oneBookData[dI.COLUMNS["bibNum"]].values[0]
        TRUE_ISBN = oneBookData[dI.COLUMNS["ISBN"]].values[0]
        TRUE_title = oneBookData[dI.COLUMNS["title"]].values[0]
        TRUE_author = oneBookData[dI.COLUMNS["author"]].values[0]
        TRUE_subjects = oneBookData[dI.COLUMNS["subjects"]].values[0]
        TRUE_publisher = oneBookData[dI.COLUMNS["publisher"]].values[0]
        TRUE_publicationYear = oneBookData[dI.COLUMNS["publicationYear"]].values[0]
        
        bIF= BookItemsFactory(dataset)
        oneBook = bIF.create()[0]
        self.assertEqual(oneBook.bibNum, TRUE_bibNum)
        self.assertEqual(oneBook.ISBN, TRUE_ISBN)
        self.assertEqual(oneBook.title, TRUE_title)
        self.assertEqual(oneBook.author, TRUE_author)
        self.assertEqual(oneBook.subjects, TRUE_subjects)
        self.assertEqual(oneBook.publisher, TRUE_publisher)
        self.assertEqual(oneBook.publicationYear, TRUE_publicationYear)
        