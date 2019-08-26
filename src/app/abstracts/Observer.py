from abc import ABC, abstractmethod
from . import Observer, Subject

class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass