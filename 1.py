# from _future_ import print_function
import csv
import MySQLdb

# print("Enter  File  To Be Export")
# conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="", db="database")
mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='test')
cursor = mydb.cursor()
# cursor = conn.cursor()
#sql = 'CREATE DATABASE test1'
# sql ='''DROP TABLE IF EXISTS `test1`; CREATE TABLE test1 (policyID int, statecode varchar(255), county varchar(255))'''
# sql = 'ALTER TABLE Question MODIFY COLUMN id INT AUTO_INCREMENT'
# sql = 'ALTER TABLE Question MODIFY COLUMN id INT PRIMARY KEY'
# sql = 'ALTER TABLE Question MODIFY COLUMN Creation_Date DATETIME DEFAULT NOW()'
sql1 = "'DROP TABLE IF EXISTS `User` ; CREATE TABLE User ( ID int,Display_Name varchar(500),,About_me TEXT,Creation_Date DATETIME default NOW(),Last_access_time DATETIME default NOW(), Location TEXT,reputation int default null,up_votes int default null, down_votes int default null, profile_image_url varchar(800),website_url varchar(100));'"
cursor.execute(sql1)

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
# mydb.commit()