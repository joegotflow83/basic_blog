from django.conf.urls import url, patterns

from blog import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<post_url>\w+.+)/$', views.post, name='post')
]