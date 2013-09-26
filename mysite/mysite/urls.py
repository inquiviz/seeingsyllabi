from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, bacon

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^bacon/$', bacon),
    url(r'^time/$', current_datetime),
)
