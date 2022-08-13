from abc import ABC, abstractmethod
import datetime
import logging
logger = logging.getLogger(__name__)

class Clock(ABC):
    @classmethod
    @abstractmethod
    def now(cls):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def n_day_pass(cls, n:int):
        raise NotImplementedError

class VirtualClock(Clock):
    """VirtualClock gets the real time when the
       object instantiates. However, the time will
       never elapse until n_day_pass() is called.

    Attributes:
        __now (datetime.date): We store the time here

    """
    __now = datetime.date.today()

    @classmethod
    def now(cls):
        return cls.__now

    @classmethod
    def n_day_pass(cls, n:int):
        """The time passes n days.

        Args:
            n (int): n days
        """
        cls.__now = cls.__now + datetime.timedelta(days=n)
class RealClock(Clock):
    
    @classmethod
    def now(self):
        return datetime.date.today()

    @classmethod
    def n_day_pass(self, n:int):
        msg = "Nothing happens. RealClock does not have this method"
        logger.warning(msg)

class ClockInterface():
    """Use strategy pattern for different types of Clock.
    """
    __clock = RealClock

    @classmethod
    def setClock(cls, clock):
        cls.__clock = clock

    @classmethod
    def now(cls):
        return cls.__clock.now()

    @classmethod
    def n_day_pass(cls, n:int):
        cls.__clock.n_day_pass(n)

class Search(ABC):
    def __init__(self, library):
        self.__library = library
    
    @abstractmethod
    def searchByTitle(self, query):
        pass

    @abstractmethod
    def searchByAuthor(self, query):
        pass

    @abstractmethod
    def searchBySubject(self, query):
        pass

    @abstractmethod
    def searchByPubDate(self, pubDate):
        pass


class Catalog(Search):
    def searchByTitle(self, query):
        print("")

    def searchByAuthor(self, query):
        print("")

    def searchBySubject(self, query):
        print("")

    def searchByPubDate(self, pubDate):
        print("")
