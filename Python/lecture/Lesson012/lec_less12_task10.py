import sqlite3


class DB:
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.cursor = None

    def __enter__(self): # Метод входа
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb): # Метод выхода
        self.connection.commit()
        self.connection.close()
        self.cursor = self.connection = None

db = DB('Python\lecture\Lesson012\sqlite.db')
with db as cur: 
    cur.execute("""create table if not exists users(name, age);""")
    cur.execute("""insert into users values ('Гвидо', 66);""")