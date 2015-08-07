from django.conf.urls import patterns, include, url

from django.contrib import admin
from tweets.views import Index, Profile, PostTweet, Search
from hashtag.views import HashTagCloud
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytweets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',Index.as_view()),
    url(r'^user/(\w+)/$', Profile.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/(\w+)/post/$', PostTweet.as_view()),
    url(r'^hashTag/(\w+)/$', HashTagCloud.as_view()),
    url(r'^search/$', Search.as_view())

)

