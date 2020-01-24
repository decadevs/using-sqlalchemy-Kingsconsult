from sqlalchemy import create_engine
from config import DATABASE_URI
from sqlalchemy.orm import sessionmaker
from sql_interface import Sqlnterface
from model import Book, Base

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
        my_dict = {'author': None, 'book_id': None, 'title': None}
        for row in session.query(Book).filter_by(**kwargs):
            my_dict['author'] = row.author
            my_dict['book_id'] = row.book_id
            my_dict['title'] = row.title
        print(my_dict)
        return my_dict

    def delete(self, **kwargs):
        for row in session.query(Book).filter_by(**kwargs):
            session.delete(row)
            print("successfully deleted", row)
        return session.commit()

    def all(self):
        book_all = []
        for row in session.query(Book).all():
            book_all.append(row)
        print(book_all)
        return book_all


kk = PostgresStorage()
# kk.create(id=1, book_id='189', title='python class', author='kc')
# kk.create(id=2, book_id='154', title='Sql class', author='king')
# kk.create(id=3, book_id='131', title='postgres class', author='kin')

kk.all()
# kk.fetch(id=113)
# kk.delete(author='kk')
# kk.delete(title='Sql class')