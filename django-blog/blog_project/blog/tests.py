from django.test import TestCase
from blog.models import Post

# Create your tests here.
class PostTests(TestCase):
  """docstring for PostTests"""
  def test_str(self):
    my_title = Post(title='This is a basic title for a basic test case')
    self.assertEquals(str(my_title), 'This is a basic title for a basic test case')
    