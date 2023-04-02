
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_paginate import Pagination, get_page_args
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='kaipoche',
    db='test')
cursor = mydb.cursor()

def filterbytag(s): # to use in question api
    ans=[]
    s="'"+s+"'"
    l=cursor.execute('SELECT id FROM Tag where tags='+s)
    l=cursor.fetchall()
    print(l)
    # tag_list=[]
    # for k in range(0,len(l)):
    # tag_list.append(l[k][0])
    # for k in tag_list:    
    #     if k==s:
    #         ans.append(k)
    # if ans==[]:
    #     abort(404)
    return l
print(filterbytag("flex"))
def get_question(tag): # using string tag output list of all questions containing this tag
    
    return l

# print(get_question("'flex'"))
def get_tag(id):
    l=cursor.execute('SELECT tags FROM Tag where id = ' + str(id))
    l=cursor.fetchall()
    tag_list=[]
    for k in range(0,len(l)):
        tag_list.append(l[k][0])
    return tag_list

@app.route('/<string:tag>/question',methods=['GET'])
def display_question(tag):
    a=get_question(tag)
    b=a[0]
    c=get_tag(b)
    return render_template('question.html',a=a,b=b,)