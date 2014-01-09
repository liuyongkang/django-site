from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
import datetime

def hello(request) :
    return HttpResponse("hello world")

def current_time(request) :
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())

def hours_ahead(request, offset) :
    try :
        offset = int(offset)
    except ValueError :
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours = offset)
    return render_to_response('hours_ahead.html', locals())

def display_meta(request) :
    values = request.META.items()
    values.sort()
    return render_to_response("index.html", locals())
