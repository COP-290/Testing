import MySQLdb

mydb = MySQLdb.connect(

    user='root',
    passwd='root',
    db='test')


def get_tags(offset=0,per_page=5):
    cursor = mydb.cursor()
    l=cursor.execute('SELECT tags FROM Tag')
    l=cursor.fetchall()
    tag_list=[]
    for k in range(0,len(l)):
        a=l[k][0]
        b=len(a)
        c=a[1:b-1]
        tag_list.append(c)
    col1=offset+per_page
    post=tag_list[offset:offset+per_page]
    return post