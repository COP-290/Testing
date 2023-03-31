
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='kaipoche',
    db='test')
cursor = mydb.cursor()

# def get_db_connection():
#     # conn = sqlite3.connect('database.db')
#     # conn.row_factory = sqlite3.Row
#     return mydb

def filterbytag(s): # to use in question api
    # conn=get_db_connection()
    cursor.execute('SELECT question FROM Question WHERE tags="%s',s)
    post=cursor.fetchall()
    cursor.close
    if post is None:
        abort(404)
    return post

def get_tags(id1):
    # conn = get_db_connection()
    col1=(id1-1)*6+1
    col2=col1+5
    # post = cursor.execute('SELECT tags FROM Tag limit 6 offset "%s" ',
    #                     (col2))
    post = cursor.execute('SELECT tags FROM Tag limit 6 offset '+str(col1))
    post=cursor.fetchall()
    l=[]
    for k in post:
        l.append(k[0])
    #cursor.close()
    if post is None:
        abort(404)
    return l

# print(a[0])
# for c in a:
#     print(c[0])
# print("hello")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def prit():
    b=get_tags(2)
    return render_template('tag.html',b=b)

@app.route('/filter/question',methods=['GET'])
def tag_filter(s):
    a=filterbytag(s)
    return render_template('question.html',a=a)

@app.route('/<int:id>/tag',methods=['GET'])
def tag_page(id):
    # print(b,"hello")
    b=get_tags(id)
    return render_template('tag.html',b=b)

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
