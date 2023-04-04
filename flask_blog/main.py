from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_paginate import Pagination, get_page_args
import MySQLdb
from tag import get_tags
from question import get_id_question,question_from_id,questionTag_from_id,showQuestion_byscore_help,sort_que_by_time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/tag',methods=['GET'])
def tag_page():
    page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    per_page=6
    offset = (page - 1) *per_page
    pagination_users,total=get_tags(offset=offset,per_page=6)
    pagination = Pagination(page=page, per_page=6, total=total,css_framework='bootstrap5')
    return render_template('tag.html',tags=pagination_users,page=page,per_page=6,pagination=pagination)

# print(get_tag(80))
@app.route('/question',methods=['GET'])
def index_question():
    a=get_id_question('flex') # list of id for particular tag
    l=[]
    for i in a: 
        b = question_from_id(i) # all question corresponding to a particular id
        c = questionTag_from_id(i)
        if b!=[]:
            b.append(c)
            l.append(b)
    n=len(l)
    return render_template('question.html',l=l,n=n)

@app.route('/<string:tag>/question',methods=['GET'])
def display_question(tag): 
    a=get_id_question(tag) # list of id for particular tag
    l=[]
    for i in a: 
        b = question_from_id(i) # all question corresponding to a particular id
        c = questionTag_from_id(i)
        if b!=[]:
            b.append(c)
            l.append(b)
    n=len(l)
    print(l)
    return render_template('question.html',l=l,n=n)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question',methods=['POST'])
def after_posting_question():
    return render_template('particular_question.html')

@app.route('/score/question',methods=['GET'])
def showQuestion_byscore():
    l=showQuestion_byscore_help()
    n=len(l)
    return render_template('question.html',l=l,n=n)

@app.route('/time/question',methods=['GET'])
def sort_que_by_time_main():
    l=sort_que_by_time()
    n=len(l)
    return render_template('question.html',l=l,n=n)

@app.route('/ask/question', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        tag = request.form['tag']
            # conn = get_db_connection()
            # cursor.execute('INSERT INTO posts (title, content) VALUES ("%s", "%s")',(title, content))
            # cursor.commit()
        return redirect(url_for('index'))
    return render_template('new_question.html')

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True,port=5010)