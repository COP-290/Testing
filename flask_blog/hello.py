import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def filterbytag(s): # to use in question api
    conn=get_db_connection()
    post=conn.execute('SELECT question FROM Question WHERE tags=?', (s,)).fetchall
    conn.close
    if post is None:
        abort(404)
    return post

def get_tags(id):
    conn = get_db_connection()
    col1=(id-1)*6
    col2=col1+6
    post = conn.execute('SELECT tags FROM Tags WHERE id  between col1=? and col2=? ' ,
                        (col1,col2)).fetchall()
    conn.close()
    if post is None:
        abort(404)
    return post



app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def prit():
    b=get_tags(0)
    return render_template('tag.html',b)

@app.route('/filter/question',methods=('GET'))
def tag_filter(s):
    a=filterbytag(s)
    return render_template('question.html',a)

@app.route('/id/tag',methods=('GET'))
def tag_page(id):
    b=get_tags(id)
    return render_template('tag.html',b)

