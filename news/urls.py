from django.conf.urls import url

from . import views

# url routes 
urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^today/$', views.news_of_day , name='newsToady'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})$', views.past_days_news , name='pastNews'),
]