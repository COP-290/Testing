from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_paginate import Pagination, get_page_args
import MySQLdb
from tag import get_tags
from question import pagefunction
from question import showQuestion_byscore_help,sort_que_by_time
from particular_question import particular_que_from_id,answer_from_parent_id
from user import check_login
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


@app.route('/<string:tag>/question',methods=['GET'])
def display_question(tag): # took care when question is less than 3
    ans=pagefunction(tag)
    print(ans[0])
    return render_template('question.html',l=ans[0],n=ans[1],page=ans[2],per_page=ans[3],pagination=ans[4])

@app.route('/question')
def zaurez():
    ans=pagefunction("flex")
    return render_template('question.html',l=ans[0],n=ans[1],page=ans[2],per_page=ans[3],pagination=ans[4])

@app.route('/')
def index():
    tag='flex'
    return render_template('index.html',tag=tag)

@app.route('/answer',methods=['POST'])
def after_posting_question():
    return render_template('particular_question.html')

@app.route('/score/question',methods=['GET'])
def showQuestion_byscore():
    ans=showQuestion_byscore_help()
    return render_template('question.html',l=ans[0],n=ans[1],page=ans[1],per_page=ans[3],pagination=ans[4])

@app.route('/time/question',methods=['GET'])
def sort_que_by_time_main():
    ans=sort_que_by_time()
    return render_template('question.html',l=ans[0],n=ans[1],page=ans[1],per_page=ans[3],pagination=ans[4])


@app.route('/<int:id>/answer',methods=['GET'])
def particular_question(id):
    l=particular_que_from_id(id)
    n=1
    ans_list=answer_from_parent_id(id)
    m=len(ans_list)
    return render_template('particular_question.html',l=l,n=n,ans_list=ans_list,m=m)

@app.route('/ask/question', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        if check_login:
            title = request.form['title']
            content = request.form['content']
            tag = request.form['tag']
        # conn = get_db_connection()
        # cursor.execute('INSERT INTO posts (title, content) VALUES ("%s", "%s")',(title, content))
        # cursor.commit()
            return redirect(url_for('index'))
        else:
            pass
    return render_template('new_question.html')

@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    conn = requestConnection()
    cursor = requestCursor(conn)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        cursor.execute('SELECT * FROM User WHERE Display_Name = %s AND password = %s', (username, password,))
        account = cursor.fetchall()
        account = list(account)
        print(account)
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            # print(account['Display_Name'])
            session['username'] = account[0][1]
            session['id'] = account[0][9]
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template('login.html', msg=msg)

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True,port=5012)