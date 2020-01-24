from abc import ABC, abstractmethod


class Sqlnterface(ABC):
    # def __init__(self, dbtype):
    #     self.dbtype = dbtype
    #     self.storage = []

    @abstractmethod
    def create(self):
        pass
    
    @abstractmethod
    def fetch(self):
        pass
    
    @abstractmethod
    def delete(self):
        pass
    
    @abstractmethod
    def all(self):
        pass