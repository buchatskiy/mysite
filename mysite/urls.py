from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import hours_ahead, hello, current_datetime, display_meta
from books import views
from contacts.views import contact, contact_thanks

urlpatterns = patterns('',

    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^display_meta/$', display_meta),
    (r'^contacts/$', contact),
    (r'^contacts/thanks/$', contact_thanks),
    #(r'^search-form/$', views.search_form),
    (r'^search/$', views.search),
    (r'^admin/', include(admin.site.urls)),
)
