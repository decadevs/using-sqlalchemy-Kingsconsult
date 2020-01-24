from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine
from config import DATABASE_URI

# import psycopg2

engine = create_engine(DATABASE_URI)


Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    book_id = Column(String)
    title = Column(String)
    author = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.book_id, self.title, self.author)
    
    
Base.metadata.create_all(engine)
    
    # def __repr__(self):
    #     return "<Book(book_id='{}', title='{}', author='{}', published={})>".format(self.book_id, self.title, self.author, self.published)