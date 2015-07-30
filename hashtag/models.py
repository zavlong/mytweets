from django.db import models
from tweets.models import Tweet
# Create your models here.

class HashTag(models.Model):
    """Hashtag Model"""
    name = models.CharField(max_length=64, unique=True)
    tweet = models.ManyToManyField(Tweet)

    def __unicode__(self):
        return self.name