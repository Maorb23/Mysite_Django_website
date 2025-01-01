from django.shortcuts import render

from django.http import HttpResponse
import calendar
from calendar import HTMLCalendar
from datetime import datetime

# def main_index(request):
    # return render(request, 'main_index.html')

def cv_view(request):
    return render(request, 'cv.html')
    
def articles_view(request):
    return render(request, 'articles.html')

def main_index(request, year=None, month=None):
    now = datetime.now()
    
    if year is None:
        year = now.year
    if month is None:
        month = now.month
    else:
        month = month.title()
        month_number = list(calendar.month_name).index(month)
        month = int(month_number)

    cal = HTMLCalendar().formatmonth(year, month)
    time = now.strftime("%H:%M")

    return render(request, 'main_index.html', {
        'cal': cal,
        'current_year': year,
        'current_month': month,
        'time': time
    })


