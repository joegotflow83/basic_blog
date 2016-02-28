from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Post


class PostForm(forms.ModelForm):


	class Meta:


		model = Post
		fields = ['title', 'content', 'tag', 'image']


class UserForm(UserCreationForm):


	email = forms.EmailField(required=True)


	class Meta:


		model = User
		fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', ]

		def save(self, commit=True):
			"""Override save method to save data to User model"""
			data = self.cleaned_data
			user = User(email=data['email'])
			user.save()