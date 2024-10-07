from django.shortcuts import render
from .models import Performance
import calendar
from datetime import datetime

def calendar_view(request, year=None, month=None):
    if year and month:
        year = int(year)
        month = int(month)
    else:
        today = datetime.today()
        year = today.year
        month = today.month

    cal = calendar.monthcalendar(year, month)
    performances = Performance.objects.filter(date__year=year, date__month=month)
    
    performance_dict = {}
    for p in performances:
        day = p.date.day
        if day in performance_dict:
            performance_dict[day].append(p)
        else:
            performance_dict[day] = [p]

    return render(request, 'calendar_site/calendar_site.html', {
        'calendar': cal,
        'year': year,
        'month': month,
        'performance_dict': performance_dict,
        'prev_month': (year, month-1 if month > 1 else 12),
        'next_month': (year, month+1 if month < 12 else 1),
    })
