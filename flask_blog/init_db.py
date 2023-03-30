import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO Tags (id,tags) VALUES (?, ?)",
            ('1', 'Python')
            )

cur.execute("INSERT INTO posts (id, tags) VALUES (?, ?)",
            ('2', 'avascript')
            )
cur.execute("INSERT INTO Tags (id,tags) VALUES (?, ?)",
            ('3', 'ython')
            )

cur.execute("INSERT INTO posts (id, tags) VALUES (?, ?)",
            ('4', 'java')
            )
cur.execute("INSERT INTO Tags (id,tags) VALUES (?, ?)",
            ('5', 'Py')
            )

cur.execute("INSERT INTO posts (id, tags) VALUES (?, ?)",
            ('6', 'script')
            )

cur.execute("INSERT INTO Tags (id,tags) VALUES (?, ?)",
            ('7', 'Python')
            )

cur.execute("INSERT INTO posts (id, tags) VALUES (?, ?)",
            ('8', 'avascript')
            )
cur.execute("INSERT INTO Tags (id,tags) VALUES (?, ?)",
            ('9', 'ython')
            )

cur.execute("INSERT INTO posts (id, tags) VALUES (?, ?)",
            ('10', 'java')
            )
cur.execute("INSERT INTO Tags (id,tags) VALUES (?, ?)",
            ('11', 'Py')
            )

cur.execute("INSERT INTO posts (id, tags) VALUES (?, ?)",
            ('12', 'script')
            )
connection.commit()
connection.close()
