import unittest
import datetime
from LMS.utils import *

class Test_Clock(unittest.TestCase):
    def test_VirtualClock(self):
        clock = VirtualClock
        now = clock.now()
        clock.n_day_pass(5)
        later = clock.now()
        delta = later - now
        self.assertEqual(delta.days, 5)

    def test_Clock(self):
        clock = RealClock
        now = clock.now()
        clock.n_day_pass(5)
        later = clock.now()
        delta = later - now
        self.assertEqual(delta.days, 0)

    def test_ClockInterface(self):
        clock1 = ClockInterface
        clock1.setClock(VirtualClock)
        now = clock1.now()
        clock1.n_day_pass(5)

        # clock2 is a new instance
        clock2 = ClockInterface
        later = clock2.now()
        delta = later - now
        self.assertEqual(delta.days, 5)