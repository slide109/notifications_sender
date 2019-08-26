from abc import ABC, abstractmethod
from typing import Dict

class Validator(ABC):

    @property
    @abstractmethod
    def is_valid(self):
        pass
    
    @property
    @abstractmethod
    def error_message(self):
        pass
    
    @abstractmethod
    def validate(self, data: Dict[str, str]) -> None:
        pass