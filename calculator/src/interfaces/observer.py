"""
this interface create by MR.ROBOT-AG at June(6/4/2020)
this interface for Observer(Child)
"""


from abc import abstractmethod, ABC


class Observer(ABC):

    @abstractmethod
    def notify(self, message: dict):
        pass

    @abstractmethod
    def class_name(self):
        pass