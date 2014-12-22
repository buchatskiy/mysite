# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse
import datetime



def hello(request):
    return HttpResponse("Hello World")


def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>Сейчас %s.</body></html>' % now
    return HttpResponse(html)



def hours_ahead(request, offset):
    
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>Через %s часов будет %s.</body></html>" % (offset, dt)
    return HttpResponse(html)