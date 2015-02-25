from django.conf.urls import patterns, url
from listFeeds import views

urlpatterns = patterns('',
    url(r'^(?P<feed_id>\d+)/activate/$', views.activate, name='activate_feed'),
    url(r'^(?P<feed_id>\d+)/deactivate/$', views.deactivate, name='deactivate_feed'),
    url(r'^add/$', views.add, name='add'),
)