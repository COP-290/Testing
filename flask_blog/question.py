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

# def get_id_question(tag):
#     conn = requestConnection()
#     cursor = requestCursor(conn)
#     tags = '"' + tag + '"'
#     l = cursor.execute('SELECT ID FROM Tag where tags= ' + tags)
#     l = cursor.fetchall()
#     ans = []
#     for i in range(len(l)):
#         ans.append(l[i][0])
#     return ans


def questionTag_from_id(id): # list of tag from question id
    conn=requestConnection()
    cursor=requestCursor(conn)
    l=cursor.execute('SELECT tags FROM Tag where id = ' + str(id))
    l=cursor.fetchall()
    tag_list=[]
    for k in range(0,len(l)):
        tag_list.append(l[k][0])
    cursor.close()
    conn.close()
    return tag_list

def question_from_tag(tag,offset):
    Ans=[]
    conn=requestConnection()
    cursor=requestCursor(conn)
    tags = '"' + tag + '"'
    f = str(offset)
    a=cursor.execute('select ID from Tag where tags = '+ tags +' limit 3 offset '+ f  )
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

def tag_list_from_listof_id(l,n):
    ans=[]
    for i in range(0,n):
        a=l[i][0]
        b=questionTag_from_id(a)
        c=[]
        c.append(l[i])
        c.append(b)
        ans.append(c)
    return ans


def question_page(val): # took care when question is less than 3
    conn=requestConnection()
    cursor=requestCursor(conn)
    page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    per_page=3
    offset=(page-1)*per_page
    if val==0:
        l=cursor.execute('SELECT * FROM Question ORDER BY Creation_Date ASC limit 3 offset '+str(offset))
    elif val==1:
        l=cursor.execute('SELECT * FROM Question ORDER BY Score limit 3 offset '+str(offset))
    l=cursor.fetchall()
    n=len(l)
    ans=tag_list_from_listof_id(l,n)
    p=cursor.execute('SELECT count(ID) FROM Question')
    p=cursor.fetchall()
    total = (p[0][0])
    pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap5')
    n=0
    if (total)<3*(page):
        n=total % 3
    else:
        n=3
    cursor.close()
    conn.close()
    return (ans,n,page,3,pagination)

def showQuestion_byscore_help():
    a=question_page(1)
    return a

def sort_que_by_time():
    b=question_page(0)
    return b

# # print(sort_que_by_time())
# if __name__=="__main__":
#     app.run(host='0.0.0.0',debug=True,port=7000)

def pagefunction(tag='flex'):
    conn = requestConnection()
    cursor = requestCursor(conn)
    page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    per_page=3
    offset=(page-1)*per_page
    l=question_from_tag(tag,offset)
    tags='"'+tag+'"'
    p=cursor.execute('SELECT count(id) FROM Tag where tags='+str(tags))
    p=cursor.fetchall()
    total = (p[0][0])
    pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap5')
    n=0
    if (total)<3*(page):
        n=total % 3
    else:
        n=3
    cursor.close()
    conn.close()
    return (l,n,page,3,pagination)
    