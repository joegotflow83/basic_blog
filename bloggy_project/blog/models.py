from django.db import models
from django.contrib.auth.models import User
from uuslug import uuslug


class Post(models.Model):


	user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=128)
	content = models.TextField()
	tag = models.CharField(max_length=16, blank=True, null=True)
	views = models.IntegerField(default=0)
	slug = models.SlugField(max_length=128, unique=True)

	def __str__(self):
		"""Prettify output"""
		return self.title

	def save(self, *args, **kwargs):
		"""Save slug for unique urls"""
		self.slug = uuslug(self.title, instance=self,
			max_length=128)
		return super().save(*args, **kwargs)