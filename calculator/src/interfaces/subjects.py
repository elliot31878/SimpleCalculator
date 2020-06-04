"""
this interface create by MR.ROBOT-AG at June(6/4/2020)
this interface for Subject (Parent)
"""


from abc import abstractmethod, ABC

from .observer import Observer


class Subject(ABC):

    @abstractmethod
    def notification(self, message: dict, to: str):
        pass

    @abstractmethod
    def inject(self, observer: Observer):
        pass

    @abstractmethod
    def dispose(self, observer: Observer):
        pass