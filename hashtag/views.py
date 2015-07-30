from django.shortcuts import render
from django.views.generic import View
from models import HashTag
# Create your views here.

class HashTagCloud(View):
    """HashTag page reachable from /hashtag/<hashtag> URL"""
    def get(self, request, hashtag):
        params = dict()
        hashtag = HashTag.objects.get(name=hashtag)
        params["tweets"] = hashtag.tweet
        return render(request, 'hashtag.html', params)

