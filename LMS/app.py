import sys
import os

script_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(script_dir, "../"))

from LMS.constants import *
from LMS.actor import *
from LMS.model import *
from LMS.service import *
from LMS.dataloader import *

if __name__ == '__main__':
    p = Person(1,2,3,4)
    x = Librarian(1,2,3,4)
    my_copy = BookItem(author="JK Rowling", 
                       title='Harry Potter2', 
                       bookStatus=BookStatus.LOANED)
    print(my_copy.title)
    print(LibraryRule.MAX_BOOKS_ISSUED_TO_A_USER)
    
    bl_detail = BookLending.fetchLendingDetail("1234567")
    print(bl_detail.bookItemBibNum)

    dataset = Dataset(DatasetInfo)
    dataset.load()
    BookItemsFactory(dataset).create()
    library = LibraryFactory(dataset, Address()).create()
    
