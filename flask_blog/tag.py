import MySQLdb

mydb = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='kaipoche',
    db='test')


def get_tags(offset=0,per_page=5):

    cursor = mydb.cursor()
    l=cursor.execute('SELECT tags FROM Tag')
    l=cursor.fetchall()
    tag_list=[]

    for k in range(0,len(l)):
        tag_list.append(l[k][0])

    col1=offset+per_page
    post=tag_list[offset:offset+per_page]
    return post
