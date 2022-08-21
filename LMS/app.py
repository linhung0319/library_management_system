import logging
import sys
import os

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
script_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(script_dir, "../"))

from LMS.constants import *
from LMS.actor import *
from LMS.model import *
from LMS.service import *
from LMS.dataloader import *
from LMS.utils import *

if __name__ == '__main__':
    clock = ClockInterface()
    clock.setClock(VirtualClock)
    
    dataset = Dataset(DatasetInfo)
    dataset.load()

    library_factory = LibraryFactory(dataset)
    library = library_factory.create()
    library_service = IssueService(library)

    #member1 = Member(library_service, "Account", "1234")
    #member1.checkout_book(1)
