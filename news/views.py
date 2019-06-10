from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt

from .models import Article

# ustom method
def convert_date(dates):
    # get weekday number
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]
    day = days[day_number]
    return day

# Create your views here.
def news_of_day(request):
    date = dt.date.today()
    news = Article.todays_news()
    return render(request, 'all-news/todays-news.html',{"date": date, "news":news})

def past_days_news(request, past_date):
    try:
        # convert date from string input
        date =dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        assert False
        raise Http404()
    
    if date == dt.date.today():
        return redirect(news_of_day)

    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html', {"date": date, "news":news})