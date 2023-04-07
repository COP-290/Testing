from flask import Flask, render_template, request, url_for, flash, redirect, session
from werkzeug.exceptions import abort
from flask_paginate import Pagination, get_page_args
import MySQLdb
from tag import get_tags
from question import pagefunction,pagefunction2,pagefunction_number
from question import showQuestion_byscore_help,sort_que_by_time
from particular_question import particular_que_from_id,answer_from_parent_id
from particular_question import particular_que_from_id,answer_from_parent_id,score_question,score_answer,sort_ans_by_time,put_answer
from tag_extra import one_ans

# from user import check_login
import re
# from flask_socketio import SocketIO
app = Flask(__name__)
# socketio=SocketIO(app)

def requestConnection():
    mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='test')
    return mydb

def requestCursor(conn):
    return conn.cursor()
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/tag/<int:per_page>/<int:page>',methods=['GET'])
def tag_page(per_page,page):
    offset = 6*(page-1)
    pagination_users,total=get_tags(offset=offset,per_page=6)
    return dict(enumerate(pagination_users))

@app.route('/tag/number',methods=['GET'])
def tag_page_number():
    pagination_users,total=get_tags()
    return str(total)


@app.route('/<string:tag>/<int:page>/question',methods=['GET'])
def display_question(tag,page): # took care when question is less than 3
    ans=pagefunction2(page,tag=tag)
    print(ans)
    return dict(enumerate(ans))

@app.route('/<string:tag>/question/number',methods=['GET'])
def display_question_number(tag): # took care when question is less than 3
    ans=pagefunction_number(tag=tag)
    return str(ans)

@app.route('/question')
def zaurez():
    ans=pagefunction("flex")
    print(ans[0])
    return dict(enumerate( ans[0]))

   

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
    return dict(enumerate(ans[0]))

@app.route('/time/question',methods=['GET'])
def sort_que_by_time_main():
    ans=sort_que_by_time()
    return dict(enumerate(ans[0]))


@app.route('/<int:id>/answer',methods=['GET'])
def particular_question(id):
    l=particular_que_from_id(id)
    n=1
    ans_list=answer_from_parent_id(id)
    m=len(ans_list)

    return dict(enumerate(l))

@app.route('/<int:id>/answers',methods=['GET'])
def particular_question_answer(id):
    l=particular_que_from_id(id)
    n=1
    ans_list=answer_from_parent_id(id)
    m=len(ans_list)
    return dict(enumerate( ans_list))

@app.route('/ask/question', methods=['GET','POST'])
def create():
    if 'loggedin' in session:
        print(session['id'])
        if request.method == 'POST':
            # if check_login: # how he checked here login by zaurez
            title = request.form['title']
            content = request.form['content']
            tag = request.form['tag']
            # conn = get_db_connection()
            # cursor.execute('INSERT INTO posts (title, content) VALUES ("%s", "%s")',(title, content))
            # cursor.commit()
            return redirect(url_for('index'))
            # else:
            #     pass
    else:
        return redirect(url_for('login'))
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
        username = '"' + username + '"'
        cursor.execute('SELECT * FROM User WHERE Display_Name = %s AND password = %s', (username, password,))
        account = cursor.fetchall()
        account = list(account)
        # print(account)
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            # print(account['Display_Name'])
            session['username'] = account[0][1]
            session['id'] = account[0][0]
            # Redirect to home page
            # return redirect(url_for('home'))
            return redirect(url_for("show_user"))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
        cursor.close()
        conn.close()
    return render_template('login.html', msg=msg)

@app.route('/pythonlogin/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))

# http://localhost:5000/pythinlogin/register - this will be the registration page, we need to use both GET and POST requests
@app.route('/pythonlogin/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    conn = requestConnection()
    cursor = requestCursor(conn)
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
            # Check if account exists using MySQL
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        username = '"' + username + '"'
        cursor.execute('SELECT * FROM User WHERE Display_Name = ' +  (username))
        # print("hello world")
        account = cursor.fetchone()
# Remember to remove duplicacy from account
#
#
    # If account exists show error and validation checks 
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        # elif not re.match(r'[A-Za-z0-9]+', username):
        #     msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
        # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO User (Display_Name, password) VALUES (%s, %s)', (username, password))
            conn.commit()
            msg = 'You have successfully registered!'
            return redirect(url_for('show_user'))
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    cursor.close()
    conn.close()
    return render_template('register.html', msg=msg)

# http://localhost:5000/pythinlogin/home - this will be the home page, only accessible for loggedin users
@app.route('/pythonlogin/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/user')
def show_user():
    if 'loggedin' in session:
        # print('hello')
        return render_template('profile.html',id=session['id'])
    else:
        # print('hi')
        msg = "Please login before"
        return redirect(url_for('login'))



@app.route('/<int:id>/upscore',methods=['PUT','GET'])
def up_score(id):
    # if 'loggedin' in session:
        l,n,ans_list,m=score_question(1,id)
        print(l[0][3])
        with open ('w.txt', 'w') as file:  
            file.write(str(l[0][3])) 
        return str(l[0][3])
    # else:
    #     return redirect(url_for('login'))

@app.route('/<int:id>/downscore',methods=['PUT','GET'])
def down_score(id):
    # if 'loggedin' in session:
        l,n,ans_list,m=score_question(-1,id) 
        return str(l[0][3])
    # else:
    #     return redirect(url_for('login'))    

@app.route('/<int:id>/upans',methods=['PUT','GET'])
def up_ans(id):

    # l,n,ans_list,m=score_answer(1,id)
    return str(one_ans(1,id))

@app.route('/<int:id>/downans',methods=['PUT','GET'])
def down_ans(id):

        # l,n,ans_list,m=score_answer(-1,id)
        return str(one_ans(-1,id))   

@app.route('/<int:id>/new_ans',methods=['POST','GET'])
def newanswer(id):
    # if 'loggedin' in session:
        if request.method == 'POST':
            content = request.form['Answer']
            l,n,ans_list,m=put_answer(id,content)
            # l,n,ans_list,m=put_answer(id,session['id'],content)
            # return redirect(url_for('particular_question',id=id))
        return "True"
    # else:
    #     return redirect(url_for('login'))


if __name__=="__main__":
    # socketio.run(app,host='0.0.0.0',debug=True,port=5003)
    app.run(host='0.0.0.0',debug=True,port=5004)