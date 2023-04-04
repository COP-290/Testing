import unittest

from flask_blog.tag import get_tags
print(get_tags())

class TestTags(unittest.TestCase):
    def test_tags(self):
        x = get_tags()
        self.assertEqual(([(5, 'Java'), (4, 'Python'), (3, 'C++'), (2, 'MySQL'), (1, 'JavaScript')], 5),x)
