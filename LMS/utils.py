from abc import ABC, abstractmethod
import datetime
import logging
logger = logging.getLogger(__name__)

class ClockDirector():
    # Use strategy pattern for different type of clock.
    # Use singleton because only one time-object is allowed
    def __init__(self, clock: Clock):
        self.__clock = clock

    def now(self):
        return self.__clock.now()

    def n_day_pass(self, n:int):
        self.__clock.n_day_pass(n)

class Clock(ABC):
    @abstractmethod
    def now(self):
        raise NotImplementedError

    @abstractmethod
    def n_day_pass(self, n:int):
        raise NotImplementedError

class VirtualClock(Clock):
    """VirtualClock gets the real time when the
       object instantiates. However, the time will
       never elapse until n_day_pass() is called.

    Attributes:
        __now (datetime.date): We store the time here

    """
    def __init__(self):
        self.__now = datetime.date.today()

    def now(self):
        return self.__now

    def n_day_pass(self, n:int):
        """The time passes n days.

        Args:
            n (int): n days
        """
        self.__now = self.__now + datetime.timedelta(days=n)

class RealClock(Clock):
    def now(self):
        return datetime.date.today()

    def n_day_pass(self, n:int):
        msg = "Nothing happens. RealClock does not have this method"
        logger.warning(msg)