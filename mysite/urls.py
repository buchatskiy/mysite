from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import hours_ahead, hello, current_datetime

urlpatterns = patterns('',

    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),


    (r'^admin/', include(admin.site.urls)),
)
