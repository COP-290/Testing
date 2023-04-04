def filterbytag(s): # to use in question api
    # conn=get_db_connection()
    # cursor.execute('SELECT question FROM Question WHERE tags="%s',s)
    # post=cursor.fetchall()
    # cursor.close
    # if post is None:
    #     abort(404)
    ans=[]
    s="'"+s+"'"
    for k in tag_list:
        # print(k[0]==s,k[0])
        if k==s:
            ans.append(k)
    if ans==[]:
        abort(404)
    return ans
    

@app.route('/tag',methods=['GET'])
def tag_filter():
    s = request.form['s']
    a=filterbytag(s)
    total = len(a)
    pagination_users=get_tags(offset=0,per_page=len(a)%10)
    pagination = Pagination(page=1, per_page=total%10, total=total,css_framework='bootstrap4')
    return render_template('tag.html',tags=a,page=1,per_page=total%10,pagination=pageination)
""
<form action="{{ url_for('delete', id=post['id']) }}" method="POST">
    <input type="submit" value="Delete Post"
            class="btn btn-danger btn-sm"
            onclick="return confirm('Are you sure you want to delete this post?')">
</form>