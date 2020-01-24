
from sqlalchemy import create_engine
from model import Base, Book
from config import DATABASE_URI
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from sql_interface import Sqlnterface
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


class InMemoryStorage(Base, Sqlnterface):
    __tablename__ = 'books'

    def create(self, **kwargs):
        with session_scope() as s:
            book = Book(**kwargs)
            s.add(book)

    def fetch(self, **kwargs):
        # my_list = [(k, v) for k, v in kwargs.items()]
        # (key, value) = my_list[0]
        # for d in self.storage:
        #     if d[key] == value:
        #         return d
        pass

    def delete(self, **kwargs):
        # my_list = [(k, v) for k, v in kwargs.items()]
        # (key, value) = my_list[0]
        # for d in self.storage:
        #     if d[key] == value:
        #         ind = self.storage.index(d)
        #         self.storage.pop(ind)
        #         return self.storage
        pass

    def all(self):
        # return self.storage
        pass


a = InMemoryStorage()
a.create(book_id="245", title="post", author="kc")
