import unittest
from in_memory import InMemoryStorage


class InMemoryStorageTest(unittest.TestCase):

    def test_create(self):
        books = InMemoryStorage()
        books.create(id=2, title='Sql class', author='kings')
        self.assertEqual(books.fetch(id=2), {'id': 2, 'title': 'Sql class', 'author': 'kings'})

    def test_fetch(self):
        books = InMemoryStorage()
        books.create(id=2, title='Sql class', author='kings')
        self.assertEqual(books.fetch(id=2), {'id': 2, 'title': 'Sql class', 'author': 'kings'})
        self.assertEqual(books.fetch(title='Sql class'), {'id': 2, 'title': 'Sql class', 'author': 'kings'})
        self.assertEqual(books.fetch(author='kings'), {'id': 2, 'title': 'Sql class', 'author': 'kings'})

    def test_delete(self):
        books = InMemoryStorage()
        books.create(id=2, title='Sql class', author='kings')
        books.create(id=4, title='tutorial', author='king')
        books.delete(id=4)
        books.delete(title='tutorial')
        books.delete(author='king')
        self.assertEqual(books.fetch(id=2), {'id': 2, 'title': 'Sql class', 'author': 'kings'})
        self.assertEqual(books.fetch(title='Sql class'), {'id': 2, 'title': 'Sql class', 'author': 'kings'})
        self.assertEqual(books.fetch(author='kings'), {'id': 2, 'title': 'Sql class', 'author': 'kings'})

    def test_get_all(self):
        books = InMemoryStorage()
        books.create(id=2, title='Sql class', author='kings')
        books.create(id=4, title='tutorial', author='king')
        self.assertEqual(books.all(), [{'id': 2, 'title': 'Sql class', 'author': 'kings'}, {'id': 4, 'title': 'tutorial', 'author': 'king'}])





