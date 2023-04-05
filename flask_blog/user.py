from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb
import re
app = Flask(__name__)


def check_login():
    # if 'loggedin' in session:
    #     return True
    # else:
    #     return False
    return True
# @app.route('/ask/question')
# def ask_question():
#     print("hello")
# def requestConnection():
#     mydb = MySQLdb.connect(host='localhost',
#     user='root',
#     passwd='root',
#     db='test')
#     return mydb

# def requestCursor(conn):
#     return conn.cursor()


# def get_details(id): # return all the detail of the user from given id
#     l=cursor.execute('SELECT * FROM Question where id = ' + str(id))
#     l=cursor.fetchall()
#     M = []
#     for i in l:
#         M.append(i)
#     return list(M)


# @app.route('/')
# def user():
#     return render_template('profile.html')

# if __name__=='__main__':
#     app.run(host='0.0.0.0',debug=True,port=3930)