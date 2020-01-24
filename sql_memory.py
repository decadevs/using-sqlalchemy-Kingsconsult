from sqlalchemy import create_engine
from config import DATABASE_URI
from sqlalchemy.orm import sessionmaker
from sql_interface import Sqlnterface
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
from model import Book, Base


# Base = declarative_base()

# Session = sessionmaker()

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


Session.configure(bind=engine)
session = Session()


class PostgresStorage(Sqlnterface):
    
    def create(self, **kwargs):
        new_book = Book(**kwargs)
        session.add(new_book)
        return session.commit()

    def fetch(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass

    def all(self):
        pass


kk = PostgresStorage()
kk.create(id=2, title='Sql class', author='kings')
