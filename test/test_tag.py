import unittest
import csv
import MySQLdb

mydb = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='root',
    db='testing')

cursor = mydb.cursor()

with open("tag.csv", 'r') as file:
  csvreader = list(csv.reader(file))
  for row in csvreader[1:100]:
    r = list(row)
    cursor.execute('INSERT INTO Tag (tags,ID) VALUES("%s", "%s")',((r[1]),int(r[0])))


mydb.commit()
cursor.close()
print ("Done")


from flask_blog.tag import get_tags
print(get_tags())

class TestTags(unittest.TestCase):
    def test_tags(self):
        x = get_tags()
        self.assertEqual(([(5, 'Java'), (4, 'Python'), (3, 'C++'), (2, 'MySQL'), (1, 'JavaScript')], 5),x)
