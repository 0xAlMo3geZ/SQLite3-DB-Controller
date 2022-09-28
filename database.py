import sqlite3


def show_all():

    conn = sqlite3.connect('databasename.db')

    c = conn.cursor()

    c.execute("SELECT rowid, * FROM tablename")

    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()

    conn.close()


def add_one(first, last, email):

    conn = sqlite3.connect('databasename.db')

    c = conn.cursor()

    c.execute("INSERT INTO tablename VALUES (?,?,?)", (first, last, email))

    conn.commit()

    conn.close()


def add_many(list):

    conn = sqlite3.connect('databasename.db')

    c = conn.cursor()

    c.executemany("INSERT INTO tablename VALUES (?,?,?)", (list))

    conn.commit()

    conn.close()


def delete_one(id):

    conn = sqlite3.connect('databasename.db')

    c = conn.cursor()

    c.execute("DELETE from tablename WHERE rowid = (?)", id)

    conn.commit()

    conn.close()
