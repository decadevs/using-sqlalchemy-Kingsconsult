# from .sql_interface import Sqlnterface
from sql_interface import Sqlnterface


class InMemoryStorage(Sqlnterface):
    def __init__(self):
        self.storage = []


    def create(self, **kwargs):
        self.storage.append(dict(kwargs))
                
    def fetch(self, **kwargs):
        my_list = [(k, v) for k, v in kwargs.items()]
        (key, value) = my_list[0]
        for d in self.storage:
            if d[key] == value:
                return d
   
    def delete(self, **kwargs):
        my_list = [(k, v) for k, v in kwargs.items()]
        (key, value) = my_list[0]
        for d in self.storage:
            if d[key] == value:
                ind = self.storage.index(d)
                self.storage.pop(ind)
                return self.storage
    
    def all(self):
        return self.storage
    
InMemoryStorage().create(id = 2, title = 'Sql class', author = 'kings')
    
hi = InMemoryStorage()

hi.create(id = 2, title = 'Sql class', author = 'kings')
# print(hi.storage)
hi.create(id = 3, title = 'python', author = 'kk')
hi.create(id = 4, title = 'tutorial', author = 'king')
hi.create(id = 5, title = 'python tutorial', author = 'aka')


print(hi.all())
# # print(hi.fetch(key='id', value=4))
# print(hi.fetch(id = 4))
print(hi.delete(author = 'aka', id=4))
# print(hi.all())


