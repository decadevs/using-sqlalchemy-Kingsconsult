from datetime import datetime

from sqlalchemy import create_engine
from model import Base, Book
from config import DATABASE_URI
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

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


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    recreate_database()
    # add_data()

    book = Book(
            title='Deep Learning',
            author='Ian Goodfellow',
            pages=775,
            published=datetime(2016, 11, 18)
    )
    with session_scope() as s:
        s.add(book)