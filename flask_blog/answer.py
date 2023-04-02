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
    s="'"+tag+"'"
    l=cursor.execute('SELECT * FROM Tag')
    l=cursor.fetchall()
    tag_list=[]
    for k in range(0,len(l)):
        if s==l[k][0]:
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
# @app.route('/')
# def index():
#     return render_template('question.html')
    
# @app.route('/<string:tag>/question',methods=['GET'])
@app.route('/')
# def display_question(tag): 
def display_question():
    a=get_id_question('python') # list of id for particular tag
    l=[]
    for i in a: 
        b = get_question(i) # all question corresponding to a particular id
        c = get_tag(i)
        if b!=[]:
            b.append(c)
            l.append(b)
    return render_template('question.html',l=l)

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True,port=8000)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['Body']
        tag = request.form['tags']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Body is required!')
        else:
            # conn = get_db_connection()
            cursor.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            cursor.commit()
            cursor.close()
            return redirect(url_for('index'))
        

#     return render_template('create.html')