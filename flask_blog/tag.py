import MySQLdb
from collections import defaultdict
def requestConnection():
    mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='test')
    return mydb

def requestCursor(conn):
    return conn.cursor()

def sort_tag_by_frequency():
    conn = requestConnection()
    cursor = requestCursor(conn)
    l = cursor.execute('SELECT tags FROM Tag')
    l = cursor.fetchall()
    tag_list = []
    d = defaultdict(lambda:0)
    for k in range(0,len(l)):
        a=l[k][0]
        b=len(a)
        c=a[1:b-1]
        tag_list.append(c)
    for tag in tag_list:
        d[tag] += 1
    Sort = []         # List store (frequency , tag)
    for i in d:
        Sort.append((d[i],i))
    Sort.sort(reverse = True)
    Answer_list_tag = []
    for i in Sort:
        Answer_list_tag.append(i[1])
    return Sort

def get_tags(offset=0,per_page=5):
    p=sort_tag_by_frequency()
    n=len(p)
    # print(offset,per_page)
    # conn = requestConnection()
    # cursor=requestCursor(conn)
    # l=cursor.execute('SELECT tags FROM Tag')
    # l=cursor.fetchall()
    # tag_list=[]
    # for k in range(0,len(l)):
    #     a=l[k][0]
    #     b=len(a)
    #     c=a[1:b-1]
    #     tag_list.append(c)
    # col1=offset+per_page
    if offset+per_page<n:
      post=p[offset:offset+per_page]
    else:
        post=p[offset:min(offset+per_page,n)]
    # cursor.close()
    # conn.close()
    if (post==[]) or (post is None):
      abort(404)
    return post,n



# print(sort_tag_by_frequency()[300*6:])