from django.db import models
from django.utils.translation import ugettext as _

class Feed(models.Model):
    feed_url = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.feed_url
    

class FeedEntry(models.Model):
    feed = models.ForeignKey(Feed)
    title = models.CharField(max_length=255)
    description = models.TextField()
    

class Word(models.Model):
    word = models.CharField(max_length=45, unique=True)
    

class WordStats(models.Model):
    ENTRY = 0
    FEED = 1
    TOTAL = 2
    STAT_TYPE_CHOICES = (
        (ENTRY, _('Entry')),
        (FEED, _('Feed')),
        (TOTAL, _('Total')),
    )
    
    word = models.ForeignKey(Word)
    stat_type = models.PositiveSmallIntegerField(choices = STAT_TYPE_CHOICES)
    item_id = models.PositiveIntegerField()
    count = models.PositiveIntegerField(default=1)
    
    class Meta:
        unique_together = ('stat_type', 'item_id')