"""
create by MR.ROBOT-AG at June(6/4/2020)
this class for Handle  Concentrate
"""

from interfaces.subjects import Subject
from interfaces.observer import Observer

from typing import Set


class ConcentrateHandler(Subject):
    _observers: Set = set()

    def __init__(self):
        pass

    def notification(self, message: dict, to: str):
        for item in self._observers:
            if item.class_name == to:
                item.notify(message)

    def inject(self, observer: Observer):
        for item in self._observers:
            if item == observer:
                return
        self._observers.add(observer)

    def dispose(self, observer: Observer):
        pass
