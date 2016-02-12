from django.test import TestCase
from .models import Post


class PostTests(TestCase):


	def test_str(self):
		"""Test that title is saved and returned"""
		my_title = Post(title="This is my test title")
		self.assertEquals(str(my_title), "This is my test title")