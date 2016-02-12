from django.db import models


class Post(models.Model):


	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=128)
	content = models.TextField()

	def __str__(self):
		"""Prettify output"""
		return self.title