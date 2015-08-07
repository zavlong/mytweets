from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from user_profile.models import User
from models import Tweet
from forms import TweetForm, SearchForm
from hashtag.models import HashTag
from django.template import Context
from django.template.loader import render_to_string
import json
# Create your views here.

# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('I am called from a get Request')
#     elif request.method == 'POST':
#         return HttpResponse('I am called from a post Request')

class Index(View):
    def get(self, request):
        params = {}
        # user = User.objects.get(username=username)
        # tweets = Tweet.objects.filter(user=user)
        # params["tweets"] = tweets
        # params["user"] = user
        return render(request, 'base.html', params)

class Profile(View):
    """User Profile page reachable from /user/<username> URL"""
    def get(self, request, username):
        params = dict()
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter(user=user)
        params["tweets"] = tweets
        params["user"] = user
        return render(request, 'profile.html', params)

class PostTweet(View):
    """Tweet Post form available on page /user/<username> URL"""
    def post(self, request, username):
        form = TweetForm(self.request.POST)
        if form.is_valid():
            user = User.objects.get(username=username)
            tweet = Tweet(text=form.cleaned_data['text'])
            user=user
            country=form.cleaned_data['country']
            tweet.save()
            words = form.cleaned_data['text'].split(" ")
            for word in words:
                if word[0] == "#":
                    hashtag, created = HashTag.objects.get_or_create(name=word[1:])
                    hashtag.tweet.add(tweet)
        return HttpResponse()

class Search(View):
    """Search all tweets with query /search/?query=<query> URL"""
    def get(self, request):
        form = SearchForm()
        params = dict()
        params["search"] = form
        return render(request, 'search.html', params)

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid:
            query = form.cleaned_data['query']
            tweets = Tweet.objects.filter(text__icontains=query)
            context = Context({"query"})
            return_str = render_to_string('partials/_tweet_search.html', context)
            return HttpResponse(json.dumps(return_str), content_type="application/json")
        else:
            HttpResponseRedirect("/search")