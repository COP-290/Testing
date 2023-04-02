
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_paginate import Pagination, get_page_args
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='kaipoche',
    db='test')
cursor = mydb.cursor()
l=cursor.execute('SELECT tags FROM Tag')
l=cursor.fetchall()
tag_list=[]
for k in range(0,len(l)):
    tag_list.append(l[k][0])

# def get_db_connection():
#     # conn = sqlite3.connect('database.db')
#     # conn.row_factory = sqlite3.Row
#     return mydb

def filterbytag(s): # to use in question api
    # conn=get_db_connection()
    # cursor.execute('SELECT question FROM Question WHERE tags="%s',s)
    # post=cursor.fetchall()
    # cursor.close
    # if post is None:
    #     abort(404)
    ans=[]
    s="'"+s+"'"
    for k in tag_list:
        # print(k[0]==s,k[0])
        if k==s:
            ans.append(k)
    if ans==[]:
        abort(404)
    return ans
# print(filterbytag('algorithm'))
def get_tags(offset=0,per_page=5):
    # conn = get_db_connection()
    col1=offset+per_page
    post=tag_list[offset:offset+per_page]
    # post = cursor.execute('SELECT tags FROM Tag limit 6 offset '+str(col1))
    # post=cursor.fetchall()
    # l=[]
    # for k in post:
    #     l.append(k[0])
    # #cursor.close()
    # if post is None:
    #     abort(404)
    return post

# print(a[0])
# for c in a:
#     print(c[0])
# print("hello")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# @app.route('/')
# def prit():
#     b=get_tags(1)
#     return render_template('tag.html',b=b)

@app.route('/tag',methods=['GET'])
def tag_filter():
    s = request.form['s']
    a=filterbytag(s)
    total = len(a)
    # pagination_users = get_users(offset=offset, per_page=per_page)
    pagination_users=get_tags(offset=0,per_page=len(a)%10)
    pagination = Pagination(page=1, per_page=total%10, total=total,css_framework='bootstrap4')
    return render_template('tag.html',tags=a,page=1,per_page=total%10,pagination=pageination)

@app.route('/',methods=['GET'])
def tag_page(id=1):
    # print(b,"hello")
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = 100
    # pagination_users = get_users(offset=offset, per_page=per_page)
    pagination_users=get_tags(offset=offset,per_page=9)
    pagination = Pagination(page=page, per_page=9, total=total,css_framework='bootstrap4')
    # return render_template('index.html',users=pagination_users,page=page,per_page=per_page,pagination=pagination  )
    return render_template('tag.html',tags=pagination_users,page=page,per_page=9,pagination=pagination)

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
