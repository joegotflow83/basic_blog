from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
	"""Create home page and display posts in order of date creation"""
	latest_posts = Post.objects.all().order_by('-created_at')
	for post in latest_posts:
		post.url = post.title.replace(' ', '_')
	return render(request, 'blog/blog.html', {'latest_posts': latest_posts})

def post(request, post_url):
	"""View a post in detail"""
	single_post = get_object_or_404(Post,
	title=post_url.replace('_', ' '))
	return render(request, 'blog/single_post.html', {'single_post': single_post})