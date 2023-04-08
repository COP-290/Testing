from werkzeug.exceptions import abort
from flask_paginate import Pagination, get_page_args
import MySQLdb
# app=Flask(__name__)
def requestConnection():
    mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='test')
    return mydb

def requestCursor(conn):
    return conn.cursor()

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
