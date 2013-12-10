from django.template.loader import get_template
from django.template import Context
from django.http import Http404, HttpResponse
import datetime

def hello(request) :
    return HttpResponse("hello world")

def current_time(request) :
    now = datetime.datetime.now()
    t = get_template('current_date.html')
    html = t.render(Context({'current_date' : now}))
    return HttpResponse(html)

def hours_ahead(request, offset) :
    try :
        offset = int(offset)
    except ValueError :
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

