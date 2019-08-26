from .....abstracts.Subject import Subject
from .....abstracts.Observer import Observer

from ...entities import MainFormData as FormData
from typing import List

class MainFormSubject(Subject):

    _state: FormData = None
    _observers: List[Observer] = []

    @property
    def username(self):
        return self._state.username
    
    @property
    def email(self):
        return self._state.email
    
    @property
    def message(self):
        return self._state.message
    
    @property
    def url(self):
        return self._state.url
    
    @property
    def phone(self):
        return self._state.phone
    
    @property
    def productName(self):
        return self._state.productName

    @property
    def price(self):
        return self._state.price


    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)


    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)


    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)


    def updateFormData(self, form_data: FormData):
        self._state = form_data
        self.notify()