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
import datetime
mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='kaipoche',
    db='test')
cursor = mydb.cursor()

with open("/home/baadalvm/repos/answers.csv", 'r') as file:
  csvreader = list(csv.reader(file))
  for row in csvreader[1:-1]:
    try:
      r = list(row)
      # a = r[2]
      # b = a[:10]
      # c = a[11:-1]
      # # print(a,b,c)
      # d = str(b) + " , " + str(c)
      # # print(d)
      # r1 = int(row[0])
      # r2 = int(row[1])
      # r3 = int(row[4])
      # r5 = row[5]
      # r6 = row[6]
      # print((int(a[0:4]),int(a[5:7]),int(a[8:10]),int(a[11:13]),int(a[14:16]),int(a[17:-1])))
      # timestamp = datetime.datetime(int(a[0:4]),int(a[8:10]),int(a[5:7]),int(a[11:13]),int(a[14:16]),int(a[17:-1]))
      # t = timestamp.strftime('%Y-%m-%d %H:%M:%S')
      # print(t)
      # print(r1,r2,r3,r5,r6)
      cursor.execute('INSERT INTO Answer (ID,Owner_User_Id,Parent_Id,Score,Body) VALUES("%s", "%s", "%s", "%s", "%s")',(int(r[0]),int(r[1]),int(r[3]),int(r[4]),r[5]))
    except:
      continue
#close the connection to the database.

mydb.commit()
cursor.close()
print ("Done")