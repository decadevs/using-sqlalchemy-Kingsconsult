from sql_interface import Sqlnterface

import psycopg2 as pg
conn = pg.connect("host=localhost dbname=postgres user=postgres password=kings042")
cur = conn.cursor()

# cur.execute("""CREATE TABLE memory(
# id integer PRIMARY KEY,
# title text,
# author text)""")

conn.commit()

# from .sql_interface import Sqlnterface


class InMemoryStorage(Sqlnterface):
    def __init__(self):
        self.storage = []

    def create(self, **kwargs):
        cur = conn.cursor()
        cur.execute("INSERT INTO memory VALUES (%s, %s, %s)", (kwargs['id'], kwargs['title'], kwargs['author']))
        return conn.commit()

    def fetch(self, **kwargs):
        pass
   
    def delete(self, **kwargs):
        pass
    
    def all(self):
        conn = pg.connect("host=localhost dbname=postgres user=postgres password=kings042")
        cur = conn.cursor()
        cur.execute('SELECT * FROM memory')
        return conn.commit()
        # return cur.fetchone()


hi = InMemoryStorage()

# hi.create(id=2, title='Sql class', author='kings')
# hi.create(id = 3, title = 'python', author = 'kk')
# hi.create(id = 4, title = 'tutorial', author = 'king')
# hi.create(id = 5, title = 'python tutorial', author = 'aka')
print(hi.all())

