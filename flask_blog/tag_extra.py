
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_paginate import Pagination, get_page_args
import MySQLdb
app=Flask(__name__)

def requestConnection():
    mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='test')
    return mydb

def requestCursor(conn):
    return conn.cursor()

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
    

@app.route('/tag',methods=['GET'])
def tag_filter():
    s = request.form['s']
    a=filterbytag(s)
    total = len(a)
    pagination_users=get_tags(offset=0,per_page=len(a)%10)
    pagination = Pagination(page=1, per_page=total%10, total=total,css_framework='bootstrap4')
    return render_template('tag.html',tags=a,page=1,per_page=total%10,pagination=pageination)

@app.route('/score/question',methods=['GET'])
def showQuestion_byscore():
    conn=requestConnection()
    cursor=requestCursor(conn)
    l=cursor.execute('SELECT * FROM Question ORDER BY Score DESC')
    l=cursor.fetchall()
    n=len(l)
    return render_template('question.html',l=l,n=n)

def get_id_question(tag):
    conn = requestConnection()
    cursor = requestCursor(conn)
    tags = '"' + tag + '"'
    l = cursor.execute('SELECT ID FROM Tag where tags= ' + tags)
    l = cursor.fetchall()
    ans = []
    for i in range(len(l)):
        ans.append(l[i][0])
    return ans

def question_from_tag(tag,offset):
    Ans=[]
    conn=requestConnection()
    cursor=requestCursor(conn)
    tags = '"' + tag + '"'
    a=cursor.execute('select ID from Tag where tags = '+tags+' limit 3 offset '+str(offset))
    a=cursor.fetchall()
    for i in range(len(a)):
        l=cursor.execute('SELECT * FROM Question where id = ' + str(a[i][0]))
        l=cursor.fetchall()
        m = cursor.execute('SELECT tags FROM Tag where id = ' + str(a[i][0]))
        m = cursor.fetchall()
        M = []
        for i in range(len(m)):
            M.append( m[i][0])
        L = list(l)
        L.append(M)
        Ans.append(L)  
    cursor.close()
    conn.close()        
    return Ans

# print(question_from_tag("c++",0))
# print()
# print(question_from_tag('c++',1))

conn=requestConnection()
cursor=requestCursor(conn)
tag='"flex"'
a=cursor.execute('select count(ID) from Question ')
a=cursor.fetchall()
print(a)