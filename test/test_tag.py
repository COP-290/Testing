import unittest

from flask_blog.tag import get_tags
print(get_tags())

class TestCircle(unittest.TestCase):
    def test_circle_instance_of_shape(self):
        x = get_tags()
        self.assertIsInstance(["'flex'", "'actionscript-3'", "'air'", "'svn'", "'tortoisesvn'"],list)
