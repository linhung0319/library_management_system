import sys
import os

script_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(script_dir, "../"))

from library_manage_system.constants import *
from library_manage_system.actor import *
from library_manage_system.model import *

if __name__ == '__main__':
    p = Person(1,2,3,4)
    x = Librarian(1,2,3,4)
    hp_info = BookInfo(authors=["JK Rowling"], title='Harry Potter2')
    hp_item_info = BookItemInfo(BookStatus.LOANED)
    my_copy = BookItem(hp_info, hp_item_info, Rack())
    print(my_copy.title)
    print(LibraryRule.MAX_BOOKS_ISSUED_TO_A_USER)
    
    
