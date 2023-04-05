
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

def question_from_id(id): # output list of all questions from a given id
    conn=requestConnection()
    cursor=requestCursor(conn)
    l=cursor.execute('SELECT * FROM Question where id = ' + str(id))
    l=cursor.fetchall()
    M = []
    for i in l:
        M.append(i)
    cursor.close()
    conn.close()
    return list(M)
def questionTag_from_id(id): # list of tag from question id
    conn=requestConnection()
    cursor=requestCursor(conn)
    l=cursor.execute('SELECT tags FROM Tag where id = ' + str(id))
    l=cursor.fetchall()
    tag_list=[]
    # print(l)
    for k in range(0,len(l)):
        tag_list.append(l[k][0])
    cursor.close()
    conn.close()
    return tag_list

def particular_que_from_id(id):
    b=question_from_id(id)
    tag=questionTag_from_id(id)
    ans=[]
    ans.append(b)
    ans.append(tag)

    return ans
# print(answer_from_id())
# print(particular_que_from_id(80))

def answer_from_parent_id(id):
    conn = requestConnection()
    cursor = requestCursor(conn)
    l = cursor.execute('SELECT * FROM Answer where Parent_ID = ' + str(id))
    l = cursor.fetchall()
    Answer_list = []
    for k in range(len(l)):
        Answer_list.append(l[k])
    return Answer_list

# print(answer_from_parent_id(80))
@app.route('/')
def particular_question():
    conn = requestConnection()
    cursor = requestCursor(conn)
    l=cursor.execute(
        "SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate FROM Orders INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;")
    l=particular_que_from_id(80)
    n=1
    ans_list=answer_from_parent_id(80)
    # print(ans_list)
    m=len(ans_list)
    return render_template('particular_question.html',l=l,n=n,ans_list=ans_list,m=m)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=7015)