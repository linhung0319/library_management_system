import unittest
from LMS.dataloader import *
from LMS.constants import DatasetInfo, Address

class Test_BookItemsFactory(unittest.TestCase):
    def test_create(self):
        dI = DatasetInfo
        dataset = Dataset(dI)
        dataset.load()
        oneBookData = dataset.df.iloc[[0]]

        TRUE_bib_num = oneBookData[dI.COLUMNS["bib_num"]].values[0]
        TRUE_ISBN = oneBookData[dI.COLUMNS["ISBN"]].values[0]
        TRUE_title = oneBookData[dI.COLUMNS["title"]].values[0]
        TRUE_author = oneBookData[dI.COLUMNS["author"]].values[0]
        TRUE_subjects = oneBookData[dI.COLUMNS["subjects"]].values[0]
        TRUE_publisher = oneBookData[dI.COLUMNS["publisher"]].values[0]
        TRUE_publication_year = oneBookData[dI.COLUMNS["publication_year"]].values[0]
        
        bIF= BookItemsFactory(dataset)
        oneBook = bIF.create()[TRUE_bib_num]
        self.assertEqual(oneBook.bib_num, TRUE_bib_num)
        self.assertEqual(oneBook.ISBN, TRUE_ISBN)
        self.assertEqual(oneBook.title, TRUE_title)
        self.assertEqual(oneBook.author, TRUE_author)
        self.assertEqual(oneBook.subjects, TRUE_subjects)
        self.assertEqual(oneBook.publisher, TRUE_publisher)
        self.assertEqual(oneBook.publication_year, TRUE_publication_year)
        