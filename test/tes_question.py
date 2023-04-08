
import unittest
import csv
import MySQLdb
import datetime

mydb = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
    db = 'test'
)

cursor = mydb.cursor()


question_from_tag_answer =[[(91, 62, datetime.datetime(2007, 8, 2, 15, 45, 37), 99, 'Python', 'Its body is not about SQL but about python'), ['C++']]]
# L = []
questionTag_from_id_answer = ['Python']
tag_list_from_listof_id_answer = []
from question import question_from_tag, questionTag_from_id, tag_list_from_listof_id

class TestQuestion(unittest.TestCase):
    def test_question_from_tag(self):
        x = question_from_tag("c++",0)
        # print(x)
        # print(List)
        self.assertEqual((question_from_tag_answer),x)
    
    def test_questionTag_from_id(self):
        x = questionTag_from_id(90)
        self.assertEqual((questionTag_from_id_answer),x)


    def test_tag_list_from_listof_id(self):
        l = ((74570, 7709, datetime.datetime(2023, 4, 4, 9, 42, 27), -1, "'CSS : Bad Gray Line to the side of the Navigation Bar on http://perl-begin.org/'", '\'<p>I\'m maintaining <a href="http://perl-begin.org/" rel="nofollow">the Perl Beginners\' Site</a> and used a modified template from Open Source Web Designs. Now, the problem is that I still have an undesired artifact: a gray line on the left side of the main frame, to the left of the navigation menu. Here\'s <a href="http://www.shlomifish.org/Files/files/images/Computer/Screenshots/perl-begin-bad-artif.png" rel="nofollow">an image</a> highlighting the undesired effect.</p>\n\n<p>How can I fix the CSS to remedy this problem?</p>\n\''), (151290, 13930, datetime.datetime(2023, 4, 4, 9, 42, 29), -1, "'What combination do you use for your polyglot solution?'", "'<p>Those of us who use multiple languages to solve problems can combine them in a lot of ways.  Personally I use PL/SQL, XSLT, JavaScript, and Java plus the pseudo languages HTML, XML, CSS, Ant, and Bash.  What do you use? </p>\n'"), (152670, 10422, datetime.datetime(2023, 4, 4, 9, 42, 29), -1, "'How to stop the Access 2007 Configuration Progress when switching versions'", '\'<p>Like many developers I need to run more than 1 version of MS Access.  I have just installed Access 2007.  If I open Access 2003 and then open Access 2007 I have to wait 3mins for the \'Configuring Microsoft Office Enterprise 2007..." dialog.  Then if I open Access 2003 again it takes another 30secs or so to configure that.  </p>\n\n<p>PLEASE NOTE: I am using shortcuts to open the files that include the full path to Access.  Eg to open Access 2007:</p>\n\n<pre><code> "C:\\program files\\microsoft office 12\\office12\\msaccess.exe" "C:\\test.accdb"\n</code></pre>\n\n<p>and for 2003:</p>\n\n<pre><code> "C:\\program files\\microsoft office 11\\office11\\msaccess.exe" "C:\\test.mdb"\n</code></pre>\n\n<p>Does anyone have a solution to avoid this?  </p>\n\''))
        x = tag_list_from_listof_id(l,3)
        self.assertEqual((tag_list_from_listof_id_answer),x)
