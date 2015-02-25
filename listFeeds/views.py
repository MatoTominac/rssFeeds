from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils.translation import ugettext as _
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse

from listFeeds.models import Feed


def index(request):
    feeds = Feed.objects.all()
    context = {'feeds': feeds}
    return render(request, 'listFeeds/index.html', context)

def activate(request, feed_id):
    feed = get_object_or_404(Feed, pk=feed_id)
    feed.active = True
    feed.save()
    return redirect('index')
    

def deactivate(request, feed_id):
    feed = get_object_or_404(Feed, pk=feed_id)
    feed.active = False
    feed.save()
    return redirect('index')
    