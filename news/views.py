from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime as dt

# ustom method
def convert_date(dates):
    # get weekday number
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]
    day = days[day_number]
    return day

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def news_of_day(request):
    date = dt.date.today()

    # convert date to day
    day = convert_date(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day} - {date.month} -{date.year}</h1>
            </body>
        </html>
    '''
    return HttpResponse(html)

def past_days_news(request, past_date):
    try:
        # convert date from string input
        date =dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        raise Http404()
    day = convert_date(date)

    html =html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
    '''
    return HttpResponse(html)