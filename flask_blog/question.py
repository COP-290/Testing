from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_paginate import Pagination, get_page_args
import MySQLdb
app=Flask(__name__)

def requestConnection():
    mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='test')
    return mydb

def requestCursor(conn):
    return conn.cursor()

# def get_id_question(tag):
#     conn = requestConnection()
#     cursor = requestCursor(conn)
#     tags = '"' + tag + '"'
#     l = cursor.execute('SELECT ID FROM Tag where tags= ' + tags)
#     l = cursor.fetchall()
#     ans = []
#     for i in range(len(l)):
#         ans.append(l[i][0])
#     return ans


def questionTag_from_id(id): # list of tag from question id
    conn=requestConnection()
    cursor=requestCursor(conn)
    l=cursor.execute('SELECT tags FROM Tag where id = ' + str(id))
    l=cursor.fetchall()
    tag_list=[]
    for k in range(0,len(l)):
        tag_list.append(l[k][0])
    cursor.close()
    conn.close()
    return tag_list



def question_from_tag(tag,offset):
    Ans=[]
    conn=requestConnection()
    cursor=requestCursor(conn)
    tags = '"' + tag + '"'
    f = str(offset)
    a=cursor.execute('select ID from Tag where tags = '+ tags +' limit 3 offset '+ f  )
    a=cursor.fetchall()
    for i in range(len(a)):
        l=cursor.execute('SELECT * FROM Question where id = ' + str(a[i][0]))
        l=cursor.fetchall()
        m = cursor.execute('SELECT tags FROM Tag where id = ' + str(a[i][0]))
        m = cursor.fetchall()
        M = []
        for i in range(len(m)):
            M.append( m[i][0])
        L = list(l)
        L.append(M)
        Ans.append(L)  
    cursor.close()
    conn.close()        
    return Ans

# print(question_from_tag("c++",0))

def tag_list_from_listof_id(l,n):
    ans=[]
    for i in range(0,n):
        a=l[i][0]
        b=questionTag_from_id(a)
        c=[]
        c.append(l[i])
        c.append(b)
        ans.append(c)
    return ans

# Not able to do unit test for this
def question_page(val): # took care when question is less than 3 
    conn=requestConnection()
    cursor=requestCursor(conn)
    page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    per_page=3
    offset=(page-1)*per_page
    if val==0:
        l=cursor.execute('SELECT * FROM Question ORDER BY Creation_Date ASC limit 3 offset '+str(offset))
    elif val==1:
        l=cursor.execute('SELECT * FROM Question ORDER BY Score limit 3 offset '+str(offset))
    l=cursor.fetchall()
    n=len(l)
    ans=tag_list_from_listof_id(l,n)
    p=cursor.execute('SELECT count(ID) FROM Question') # This is not giving correct answer why?
    p=cursor.fetchall()
    total = (p[0][0])
    pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap5')
    n=0
    if (total)<3*(page):
        n=total % 3
    else:
        n=3
    cursor.close()
    conn.close()
    return (ans,n,page,3,pagination)

# print(question_page(1))

def showQuestion_byscore_help():
    a=question_page(1)
    return a

def sort_que_by_time():
    b=question_page(0)
    return b
# print(question_page(1))
# # print(sort_que_by_time())
# if __name__=="__main__":
#     app.run(host='0.0.0.0',debug=True,port=7000)

def pagefunction(tag='flex'):
    conn = requestConnection()
    cursor = requestCursor(conn)
    page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    per_page=3
    offset=(page-1)*per_page
    l=question_from_tag(tag,offset)
    tags='"'+tag+'"'
    p=cursor.execute('SELECT count(id) FROM Tag where tags='+str(tags))
    p=cursor.fetchall()
    total = (p[0][0])
    pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap5')
    n=0
    if (total)<3*(page):
        n=total % 3
    else:
        n=3
    cursor.close()
    conn.close()
    return (l,n,page,3,pagination)

def pagefunction2(page,tag='flex'):
    conn = requestConnection()
    cursor = requestCursor(conn)
    per_page=3
    offset=(page-1)*per_page
    l=question_from_tag(tag,offset)
    tags='"'+tag+'"'
    p=cursor.execute('SELECT count(id) FROM Tag where tags='+str(tags))
    p=cursor.fetchall()
    total = (p[0][0])
    pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap5')
    n=0
    if (total)<3*(page):
        n=total % 3
    else:
        n=3
    cursor.close()
    conn.close()
    return l

def pagefunction_number(tag='flex'):
    conn = requestConnection()
    cursor = requestCursor(conn)
    per_page=3
    page = 1
    offset=(page-1)*per_page
    l=question_from_tag(tag,offset)
    tags='"'+tag+'"'
    p=cursor.execute('SELECT count(id) FROM Tag where tags='+str(tags))
    p=cursor.fetchall()
    total = (p[0][0])
    pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap5')
    n=0
    if (total)<3*(page):
        n=total % 3
    else:
        n=3
    cursor.close()
    conn.close()
    return total

# print(pagefunction('flex'))


# def search_question(search):
#     conn = requestConnection()
#     cursor = requestCursor(conn)
#     # search = request.form['search']
#     search  = '"' + search + '"'
#     cursor.execute("SELECT * from Question WHERE Body LIKE " + (search))
#     M = cursor.fetchall()
#     print(M)

# print(search_question("SQL"))
print(question_from_tag("c++",0))
print(questionTag_from_id(90))
l = ((74570, 7709, datetime.datetime(2023, 4, 4, 9, 42, 27), -1, "'CSS : Bad Gray Line to the side of the Navigation Bar on http://perl-begin.org/'", '\'<p>I\'m maintaining <a href="http://perl-begin.org/" rel="nofollow">the Perl Beginners\' Site</a> and used a modified template from Open Source Web Designs. Now, the problem is that I still have an undesired artifact: a gray line on the left side of the main frame, to the left of the navigation menu. Here\'s <a href="http://www.shlomifish.org/Files/files/images/Computer/Screenshots/perl-begin-bad-artif.png" rel="nofollow">an image</a> highlighting the undesired effect.</p>\n\n<p>How can I fix the CSS to remedy this problem?</p>\n\''), (151290, 13930, datetime.datetime(2023, 4, 4, 9, 42, 29), -1, "'What combination do you use for your polyglot solution?'", "'<p>Those of us who use multiple languages to solve problems can combine them in a lot of ways.  Personally I use PL/SQL, XSLT, JavaScript, and Java plus the pseudo languages HTML, XML, CSS, Ant, and Bash.  What do you use? </p>\n'"), (152670, 10422, datetime.datetime(2023, 4, 4, 9, 42, 29), -1, "'How to stop the Access 2007 Configuration Progress when switching versions'", '\'<p>Like many developers I need to run more than 1 version of MS Access.  I have just installed Access 2007.  If I open Access 2003 and then open Access 2007 I have to wait 3mins for the \'Configuring Microsoft Office Enterprise 2007..." dialog.  Then if I open Access 2003 again it takes another 30secs or so to configure that.  </p>\n\n<p>PLEASE NOTE: I am using shortcuts to open the files that include the full path to Access.  Eg to open Access 2007:</p>\n\n<pre><code> "C:\\program files\\microsoft office 12\\office12\\msaccess.exe" "C:\\test.accdb"\n</code></pre>\n\n<p>and for 2003:</p>\n\n<pre><code> "C:\\program files\\microsoft office 11\\office11\\msaccess.exe" "C:\\test.mdb"\n</code></pre>\n\n<p>Does anyone have a solution to avoid this?  </p>\n\''))
print(tag_list_from_listof_id(l,3))
