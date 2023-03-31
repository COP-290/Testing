# # # import mysql
# # # # import pandas as pd
# # # # import numpy as np
# import csv

# # # connection = mysql.connect('database.db')

# from flask import Flask, render_template, request
# from flask_mysqldb import MySQL
# app = Flask(__name__)


# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'kaipoche'
# app.config['MYSQL_DB'] = 'test'

# mysql = MySQL(app)


# # # with open('schema.sql') as f:
# #     # mysql.connection.execute(f.read())
# # cur = mysql.connection.cursor()
# cur = mysql.connection.cursor()
# # input = pd.read_csv("/home/baadalvm/repos/tags.csv")
# # X = input[input.columns[0:]]
# # X = np.array(X)
# with open("/home/baadalvm/repos/tags.csv", 'r') as file:
#   csvreader = csv.reader(file)
#   for row in csvreader:
#     cur.execute("INSERT INTO Tag (id,tags) VALUES (?, ?)", (row[0], row[1]) )
# mysql.connection.commit()
# mysql.connection.close()
# # cur.execute("INSERT INTO Tags (id, tags) VALUES (?, ?)",
# #             ('2', 'avascript')
# #             )
# # cur.execute("INSERT INTO Tags (id,tags) VALUES (?, ?)",
# #             ('3', 'ython')
# #             )

# # cur.execute("INSERT INTO Tags (id, tags) VALUES (?, ?)",
# #             ('4', 'java')
# #             )
# # cur.execute("INSERT INTO Tags (id,tags) VALUES (?, ?)",
# #             ('5', 'Py')
# #             )

# # cur.execute("INSERT INTO Tags (id, tags) VALUES (?, ?)",
# #             ('6', 'script')
# #             )

# # cur.execute("INSERT INTO Tags (id,tags) VALUES (?, ?)",
# #             ('7', 'Python')
# #             )

# # cur.execute("INSERT INTO Tags (id, tags) VALUES (?, ?)",
# #             ('8', 'avascript')
# #             )
# # cur.execute("INSERT INTO Tags (id,tags) VALUES (?, ?)",
# #             ('9', 'ython')
# #             )

# # cur.execute("INSERT INTO Tags (id, tags) VALUES (?, ?)",
# #             ('10', 'java')
# #             )
# # cur.execute("INSERT INTO Tags (id,tags) VALUES (?, ?)",
# #             ('11', 'Py')
# #             )

# # cur.execute("INSERT INTO Tags (id, tags) VALUES (?, ?)",
# #             ('12', 'script')
# #            )
# # cur.execute("INSERT INTO Tags (id, tags) VALUES (?, ?)",
# #             ('13', 'script')
# #            )


import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='kaipoche',
    db='test')
cursor = mydb.cursor()

with open("/home/baadalvm/repos/tags.csv", 'r') as file:
  csvreader = list(csv.reader(file))
  for row in csvreader[1:]:
    print(row)
    cursor.execute('INSERT INTO Tag (id, tags ) VALUES("%s", "%s")',row)
#close the connection to the database.
mydb.commit()
cursor.close()
print ("Done")