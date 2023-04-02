from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_paginate import Pagination, get_page_args
import MySQLdb
app=Flask(__name__)
mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='kaipoche',
    db='test')
cursor = mydb.cursor()

def get_id_question(tag): # output list of id from a given tag
    ans=[]
    s=tag
    l=cursor.execute('SELECT * FROM Tag')
    l=cursor.fetchall()
    tag_list=[]
    for k in range(0,len(l)):
        a=l[k][0]
        b=len(a)
        c=a[1:b-1]
        if s==c:
         tag_list.append(l[k][1])
    return tag_list

def get_question(id): # output list of all questions from a given id
    l=cursor.execute('SELECT * FROM Question where id = ' + str(id))
    l=cursor.fetchall()
    M = []
    for i in l:
        M.append(i)
    return list(M)
# print(get_question(80))
# print(get_question("'flex'"))
def get_tag(id): # list of tag from question id
    l=cursor.execute('SELECT tags FROM Tag where id = ' + str(id))
    l=cursor.fetchall()
    tag_list=[]
    # print(l)
    for k in range(0,len(l)):
        tag_list.append(l[k][0])
    return tag_list

# print(get_tag(80))
@app.route('/')
def index():
    a=get_id_question('flex') # list of id for particular tag
    l=[]
    for i in a: 
        b = get_question(i) # all question corresponding to a particular id
        c = get_tag(i)
        if b!=[]:
            b.append(c)
            l.append(b)
    n=len(l)
    return render_template('question.html',l=l,n=n)
# print(index())
# print('hi')
@app.route('/<string:tag>/question',methods=['GET'])
def display_question(tag): 
    a=get_id_question(tag) # list of id for particular tag
    l=[]
    for i in a: 
        b = get_question(i) # all question corresponding to a particular id
        c = get_tag(i)
        if b!=[]:
            b.append(c)
            l.append(b)
    n=len(l)
    return render_template('question.html',l=l,n=n)

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
    app.run(host='0.0.0.0',debug=True,port=8000)
