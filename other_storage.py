from abc import ABC, abstractmethod


class Sqlnterface(ABC):
    def __init__(self):
        # self.storage = []
        self.storage = {}


    def create(self, id, title, author):
        self.storage['id'] = id
        self.storage['title'] = title
        self.storage['author'] = author
        

    
    def fetch(self):
        pass
    
    def delete(self):
        pass
    
    def all(self):
        pass
    
hi = Sqlnterface()

# hi.create(3, 'Sql class')
hi.create(2, 'Sql class', 'kings')

print(hi.storage)
