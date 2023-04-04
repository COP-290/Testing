from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_paginate import Pagination, get_page_args
import MySQLdb

def requestConnection():
    mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='test')
    return mydb

def requestCursor(conn):
    return conn.cursor()
    # return conn.cursor(db.cursors.DictCursor)
app=Flask(__name__)

def get_id_question(tag): # output list of id from a given tag
    s=tag
    conn=requestConnection()
    cursor=requestCursor(conn)
    l=cursor.execute('SELECT * FROM Tag')
    l=cursor.fetchall()
    tag_list=[]
    for k in range(0,len(l)):
        a=l[k][0]
        b=len(a)
        c=a[1:b-1]
        if s==c:
         tag_list.append(l[k][1])
    cursor.close()
    conn.close()
    return tag_list

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
# print(question_from_id(80))


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

# print(questionTag_from_id(80))

def question_from_tag(tag): # Time complexity is O(n2) think of modifying it.
    a=get_id_question(tag) # list of id for particular tag
    l=[]
    for i in a: 
        b = question_from_id(i) # all question corresponding to a particular id
        c = questionTag_from_id(i)
        if b!=[]:
            b.append(c)
            l.append(b)
    return l

# print(question_from_tag('flex'))

def question_per_page(offset=0,per_page=3,tag='flex'):
    l=question_from_tag(tag)
    n=len(l)
    if offset+per_page< n:
     post=l[offset:offset+per_page]
    else:
        post=l[offset:]
    return (post,min(n,offset+per_page))

# a=(question_per_page(0,3,'flex'))
# print(a[0],a[1])
# # print(questionTag_from_id(80))
@app.route('/')
def index():
    l=question_from_tag('flex')
    n=len(l)
    return render_template('ask_question.html',l=l,n=n)

@app.route('/<string:tag>/question',methods=['GET'])
def question_page(tag): # took care when question is less than 3
    # page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    tag='flex'
    t=question_per_page(offset=offset,per_page=per_page,tag=tag)
    total = (t[1])
    pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap5')
    return render_template('ask_question.html',l=t[0],n=offset+per_page)

@app.route('/<string:tag>/question',methods=['GET'])
def display_question(tag): 
    l=question_from_tag(tag)
    n=len(l)
    return render_template('ask_question.html',l=l,n=n)

@app.route('/ask/question', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        tag = request.form['tag']
        if not title:
            flash('Title is required!')
        elif not content:
            flash('Body is required!')
        elif not tag:
            flash('Tag is required')
        else:
            # conn = get_db_connection()
            # cursor.execute('INSERT INTO posts (title, content) VALUES ("%s", "%s")',(title, content))
            # cursor.commit()
            return redirect(url_for('index'))
    return render_template('ask_question.html')

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True,port=8001)

