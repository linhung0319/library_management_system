from abc import ABC, abstractmethod
import datetime
import logging
logger = logging.getLogger(__name__)

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return  cls._instances[cls]
class Clock(ABC):
    @abstractmethod
    def now(cls):
        raise NotImplementedError

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
class ClockInterface(metaclass=Singleton):
    """Use strategy pattern for different types of Clock.
       The ClockInterface need to be shared among different 
       object and we need to keep the clock synchronized, so 
       singleton is used.
    """
    def __init__(self):
        self.__clock = RealClock()
    
    def setClock(self, clock):
        self.__clock = clock

    def now(self):
        return self.__clock.now()

    def n_day_pass(self, n:int):
        self.__clock.n_day_pass(n)

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
