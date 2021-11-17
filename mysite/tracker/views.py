from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from django.db.models import Max, Min, Sum
from .models import Entry, Tag
from django.template import loader

import datetime

# Given a date and a Tag id, get the total sum of Entries' durations.
def total_duration(date, tag_id):
    e = Entry.objects.filter(
        tags=Tag.objects.get(pk=tag_id),
        date__date=date
    ).aggregate(Sum('duration'))
    if(e['duration__sum'] is None):
        return 0
    return e['duration__sum']

# Table view
def index(request):
    template = loader.get_template('index.html')
    date_range = Entry.objects.aggregate(Min('date'), Max('date'))
    date_min = date_range['date__min']
    date_max = date_range['date__max']
    all_dates = [date_min + datetime.timedelta(days=i) for i in range((date_max-date_min).days+2)]
    listening_days = [total_duration(date,1) for date in all_dates]
    reading_days = [total_duration(date,2) for date in all_dates]
    anki_days = [total_duration(date,3) for date in all_dates]
    data = list(zip(all_dates, listening_days, reading_days, anki_days))
    context = {
        'data': data,
    }
    return HttpResponse(template.render(context, request))
