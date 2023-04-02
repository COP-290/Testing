from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_paginate import Pagination, get_page_args
import MySQLdb
from tag import get_tags, mydb

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/tag',methods=['GET'])
def tag_page():
    page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    total = 100
    pagination_users=get_tags(offset=offset,per_page=6)
    pagination = Pagination(page=page, per_page=6, total=total,css_framework='bootstrap5')
    return render_template('tag.html',tags=pagination_users,page=page,per_page=9,pagination=pagination)


@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True,port=5000)