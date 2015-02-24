from django.http import HttpResponse
from listFeeds.models import Feed


def index(request):
    feeds = Feed.objects.all()
    output = ', '.join([f.feed_url for f in feeds])
    return HttpResponse(output)