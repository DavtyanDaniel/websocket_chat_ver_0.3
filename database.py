import sqlite3

con = sqlite3.connect('users.db')


def table_creation():
    try:
        con.execute('''
        CREATE TABLE USER(
        ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        SURNAME TEXT NOT NULL,
        NICKNAME TEXT NOT NULL;''')
        print('created table successfully')
    except Exception:
        print('smth went wrong in table_creation function')



