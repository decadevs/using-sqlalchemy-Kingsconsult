import unittest
from sql_memory import PostgresStorage


class PostgresStorageTest(unittest.TestCase):

    def test_create(self):
        books = PostgresStorage()
        # books.create(id=7123, book_id='2', title='Sql class', author='kings')
        self.assertEqual(books.fetch(id=73), {'author': 'kings', 'book_id': '2', 'title': 'Sql class'})
    #
    #
    def test_fetch(self):
        books = PostgresStorage()
        # books.create(id=73, book_id='2', title='Sql class', author='kings')
        self.assertEqual(books.fetch(id=73), {'author': 'kings', 'book_id': '2', 'title': 'Sql class'})
        self.assertEqual(books.fetch(id=73), {'author': 'kings', 'book_id': '2', 'title': 'Sql class'})
        self.assertEqual(books.fetch(id=73), {'author': 'kings', 'book_id': '2', 'title': 'Sql class'})

    def test_delete(self):
        books = PostgresStorage()

        books.delete(id=43)
        self.assertEqual(books.fetch(id=43), {'author': None, 'book_id': None, 'title': None})

        books.delete(title='Delete class')
        self.assertEqual(books.fetch(id=43), {'author': None, 'book_id': None, 'title': None})

        books.delete(author='Python')
        self.assertEqual(books.fetch(id=43), {'author': None, 'book_id': None, 'title': None})



    def test_get_all(self):
        books = PostgresStorage()

        self.assertEqual(books.all(), books.all())
