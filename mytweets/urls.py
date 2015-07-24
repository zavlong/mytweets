from django.conf.urls import patterns, include, url

from django.contrib import admin
from tweets.views import Index, Profile
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytweets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',Index.as_view()),
    url(r'^user/(\w+)/$', Profile.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)

