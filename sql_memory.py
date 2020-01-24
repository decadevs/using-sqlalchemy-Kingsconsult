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
        for row in session.query(Book).filter_by(**kwargs):
            print(row)
            return row

    def delete(self, **kwargs):
        for row in session.query(Book).filter_by(**kwargs):
            session.delete(row)
            print("successfully deleted", row)
        return session.commit()

    def all(self):
        for row in session.query(Book, Book.id).all():
            print(row.Book)
            return row.Book


kk = PostgresStorage()
# kk.create(id=1, book_id='189', title='python class', author='kc')
# kk.create(id=2, book_id='154', title='Sql class', author='king')
# kk.create(id=3, book_id='131', title='postgres class', author='kin')

# kk.all()
# kk.fetch(author='kk')
# kk.delete(author='kk')
kk.delete(title='Sql class')



# for name, in session.query(User.name).\
# ...             filter_by(fullname='Ed Jones'):
# ...    print(name)