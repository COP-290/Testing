
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_paginate import Pagination, get_page_args
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='kaipoche',
    db='test')
cursor = mydb.cursor()

def get_question(tag): # using string tag output list of all questions containing this tag

def get_tag(id):
    l=cursor.execute('SELECT tags FROM Tag where id="%s"',(id))
    l=cursor.fetchall()
    tag_list=[]
    for k in range(0,len(l)):
        tag_list.append(l[k][0])

@app.route('/<string:tag>/question',methods=['GET'])
def display_question(tag):
    a=get_question(tag)
    b=a[0]
    c=get_tag(b)
    return render_template('question.html',a=a,b=b,)