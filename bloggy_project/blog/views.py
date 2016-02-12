from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from .models import Post
from .forms import PostForm


def encode_url(url):
	"""Clean up the url for more readable output"""
	return url.replace(' ', '_')

def index(request):
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
			return redirect(index)
		else:
			form.errors
	form = PostForm()
	return render_to_response('blog/add_post.html', {'form': form}, context)