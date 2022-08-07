import sys
import os

script_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(script_dir, "../"))

from library_manage_system.constants import *

if __name__ == '__main__':
    p = Person(1,2,3,4)
    p.show()
    #j.show()