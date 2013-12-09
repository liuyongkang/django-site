from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from mysite.views import hello, current_time

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    ('^hello/$', hello),
    ('^time/$', current_time),
    ('^another-time-page/$', current_time),
)

