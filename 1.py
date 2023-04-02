# from _future_ import print_function
# import csv
import MySQLdb

print("Enter  File  To Be Export")
mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='kaipoche',
    db='test')
cursor = mydb.cursor()
#sql = 'CREATE DATABASE test1'
# sql1 ='''DROP TABLE IF EXISTS `Answer`; CREATE TABLE Answer (ID int, Owner_User_Id int,Creation_Date datetime,Parent_Id int,Score int,Body varchar(8000) )'''
# sql2 = '''DROP TABLE IF EXISTS `Question`; CREATE TABLE Question (ID int, Owner_User_Id int,Creation_Date datetime,Score int,Body varchar(8000),title varchar(500) )'''
# sql3 = '''DROP TABLE IF EXISTS `User`; CREATE TABLE User (ID int, Display_name varchar(800),Creation_Date datetime,About_me varchar(8000),Score int,Body varchar(8000) )'''
# cursor.execute(sql1)
# cursor.execute(sql2)
# cursor.execute(sql3)


# with open('C:/Users/Desktop/Code/python/sample.csv') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter = ',')
#     for row in reader:
#         print(row['policyID'], row['statecode'], row['county'])
#         # insert
#         conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="", db="database")
#         sql_statement = "INSERT INTO test1(policyID ,statecode,county) VALUES (%s,%s,%s)"
#         cur = conn.cursor()
#         cur.executemany(sql_statement,[(row['policyID'], row['statecode'], row['county'])])
#         conn.escape_string(sql_statement)
#         conn.commit()