from django.conf.urls import patterns, include, url

from listFeeds import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rssFeeds.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^feeds/', include('listFeeds.urls')),
    url(r'^$', views.index, name='index'),
)
