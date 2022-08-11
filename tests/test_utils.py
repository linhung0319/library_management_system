import unittest
import datetime
from LMS.utils import *

class Test_Clock(unittest.TestCase):
    def test_VirtualClock(self):
        clock = VirtualClock()
        now = clock.now()
        clock.n_day_pass(5)
        later = clock.now()
        delta = later - now
        self.assertEqual(delta.days, 5)

    def test_Clock(self):
        clock = RealClock()
        now = clock.now()
        clock.n_day_pass(5)
        later = clock.now()
        delta = later - now
        self.assertEqual(delta.days, 0)