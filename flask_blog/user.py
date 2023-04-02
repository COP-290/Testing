from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_paginate import Pagination, get_page_args
import MySQLdb



mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='test')
cursor = mydb.cursor()


def get_details(id): # return all the detail of the user from given id
    l=cursor.execute('SELECT * FROM Question where id = ' + str(id))
    l=cursor.fetchall()
    M = []
    for i in l:
        M.append(i)
    return list(M)


@app.route('/<int:id>/user',methods=['GET'])
def 