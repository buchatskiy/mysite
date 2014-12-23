# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
import datetime



def hello(request):
    return HttpResponse("Hello World")


def current_datetime(request):
    now = datetime.datetime.now()

    return render_to_response('current_datetime.html',{'current_date':now})



def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False

    return render_to_response('hours_ahead.html',{'hour_offset':offset,'next_time':dt})


def display_meta(request):
    values = request.META
    values['request.path']=request.path
    values=values.items()
    values.sort()
    return render_to_response('display_meta.html',{'values':values})
