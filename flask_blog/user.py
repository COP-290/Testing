from flask import Flask, render_template, request, url_for, flash, redirect, session
from werkzeug.exceptions import abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_paginate import Pagination, get_page_args
import MySQLdb
from tag import get_tags
from question import pagefunction
from question import showQuestion_byscore_help,sort_que_by_time
# from particular_question import particular_que_from_id,answer_from_parent_id,score_question,score_answer,sort_ans_by_time
# from user import check_login
import re
app = Flask(__name__)

def requestConnection():
    mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='test')
    return mydb

def requestCursor(conn):
    return conn.cursor()
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
    if 'logged' in session:
        id=session['id']
        l=particular_que_from_id(id)
        n=1
        ans_list=answer_from_parent_id(id)
        m=len(ans_list)
        return render_template('particular_question.html',l=l,n=n,ans_list=ans_list,m=m)
    else:
        redirect(url_for('login'))

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
    if 'loggedin' in session:
        print(session['id'])
        if request.method == 'POST':
            # if check_login: # how he checked here login by zaurez
            title = request.form['title']
            content = request.form['content']
            tag = request.form['tag'] # take care of how to get particular tag from list of tags
            conn = requestConnection()
            cursor = requestCursor(conn)
            cursor.execute('INSERT INTO Question (title, body,OwnerUserId) VALUES ("%s", "%s")',(title, content,session['id']))
            # cursor.execute('INSERT INTO Tag (ID,tags) VALUES ("%s", "%s")',(session['id'],"Python"))
            cursor.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('after_posting_question'))
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
        # password=check_password_hash(user.password, password) working but need to increase password size
        # username = '"' + username + '"'
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
            # password=generate_password_hash(password, method='sha256')
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

def dis_user(id):
        conn = requestConnection()
        cursor = requestCursor(conn)
        cursor.execute('SELECT Creation_Date from User where ID = ' + str(id))
        date = cursor.fetchone()
        # cursor.execute('SELECT website_url  from User where ID = ' + str(id))
        # websiteurl = cursor.fetchone()
        # cursor.execute('SELECT profile_image_url  from User where ID = ' + str(id))
        # profile = cursor.fetchone()
        # cursor.execute('SELECT About_me  from User where ID = ' + str(id))
        # about=cursor.fetchone()
        detail=cursor.execute('SELECT * from User where ID = ' + str(id))
        detail=cursor.fetchone()
        date = date[0]
        d = date.day
        mth = date.month
        ye = date.year
        # print(profile[0])
        date = str(d) + "/" + str(mth) + "/"+ str(ye)
        cursor.close()
        conn.close()
        return (date,detail)

@app.route('/user')
def show_user():
    if 'loggedin' in session:
        # print('hello')
        conn = requestConnection()
        cursor = requestCursor(conn)
        cursor.execute('SELECT Creation_Date from User where ID = ' + str(session['id']))
        date = cursor.fetchone()
        cursor.execute('SELECT website_url  from User where ID = ' + str(session['id']))
        websiteurl = cursor.fetchone()
        cursor.execute('SELECT profile_image_url  from User where ID = ' + str(session['id']))
        profile = cursor.fetchone()
        date = date[0]
        d = date.day
        mth = date.month
        ye = date.year
        # print(profile[0])
        date = str(d) + "/" + str(mth) + "/"+ str(ye)
        return render_template('profile.html',id=session['id'],username = session['username'],date = date,websiteurl = websiteurl[0],profile = profile[0])
    else:
        # print('hi')
        msg = "Please login before"
        return redirect(url_for('login'))

@app.route('/<int:id>/upscore',methods=['PUT','GET'])
def up_score(id):
    if 'loggedin' in session:
        l,n,ans_list,m=score_question(1,id)
        return render_template('particular_question.html',l=l,n=n,ans_list=ans_list,m=m)
    else:
        return redirect(url_for('login'))

@app.route('/<int:id>/downscore',methods=['PUT','GET'])
def down_score(id):
    if 'loggedin' in session:
        l,n,ans_list,m=score_question(-1,id)
        return render_template('particular_question.html',l=l,n=n,ans_list=ans_list,m=m)
    else:
        return redirect(url_for('login'))

@app.route('/<int:id>/upans',methods=['PUT','GET'])
def up_ans(id):
    if 'loggedin' in session:
        l,n,ans_list,m=score_answer(1,id)
        return render_template('particular_question.html',l=l,n=n,ans_list=ans_list,m=m)
    else:
        return redirect(url_for('login'))

@app.route('/<int:id>/downans',methods=['PUT','GET'])
def down_ans(id):
    if 'loggedin' in session:
        l,n,ans_list,m=score_answer(-1,id)
        return render_template('particular_question.html',l=l,n=n,ans_list=ans_list,m=m)
    else:
        return redirect(url_for('login'))

@app.route('/<int:id>/score/ans',methods=['GET'])
def showAns_byscore(id):
    l,n,ans_list,m=sort_ans_by_time(id,0)
    return render_template('particular_question.html',l=l,n=n,ans_list=ans_list,m=m)

@app.route('/<int:id>/time/ans',methods=['GET'])
def sort_ans_by_time_main(id):
    l,n,ans_list,m=sort_ans_by_time(id,1)
    return render_template('particular_question.html',l=l,n=n,ans_list=ans_list,m=m)




if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True,port=5010)