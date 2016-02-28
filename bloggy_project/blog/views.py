from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.views.generic.edit import FormView
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from .models import Post
from .forms import PostForm, UserForm


def encode_url(url):
	"""Clean up the url for more readable output"""
	return url.replace(' ', '_')

class Register(FormView):


	template_name = 'blog/register.html'
	form_class = UserForm
	fields = ['username', 'email', 'password1', 'password2',
			  'first_name', 'last_name']
	success_url = "/"

	def form_valid(self, form):
		"""Validate the form"""
		user = User.objects.create_user(form.cleaned_data['username'],
										form.cleaned_data['email'],
								   		form.cleaned_data['password1'])
		user.save()
		return super().form_valid(form)


class AuthLogin(View):


	def post(self, request):
		"""Verify user credentials and log in"""
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect(blog)
		else:
			return HttpResponse('Invalid Credentials')

	def get(self, request):
		"""Display the log in form"""
		return render(request, 'blog/login.html')


class AuthLogout(View):


	def get(self, request):
		"""Log a user out"""
		logout(request)
		return redirect('/')


def blog(request):
	"""Create home page and display posts in order of date creation"""
	latest_posts = Post.objects.all().order_by('-created_at')
	popular_posts = Post.objects.all().order_by('-views')[:5]
	for post in latest_posts:
		post.url = encode_url(post.title)
	for popular_post in popular_posts:
		popular_post.url = encode_url(popular_post.title)
	return render(request, 'blog/blog.html', {'latest_posts': latest_posts, 
											  'popular_posts': popular_posts})

def post(request, slug):
	"""View a post in detail"""
	single_post = get_object_or_404(Post, slug=slug)
	single_post.views += 1
	single_post.save()
	return render(request, 'blog/single_post.html', {'single_post': single_post})

def add_post(request):
	"""Allow a user to create a post"""
	context = RequestContext(request)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save(commit=True)
			return redirect(blog)
		else:
			form.errors
	form = PostForm()
	return render_to_response('blog/add_post.html', {'form': form}, context)