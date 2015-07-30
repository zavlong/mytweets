from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from user_profile.models import User
from models import Tweet
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