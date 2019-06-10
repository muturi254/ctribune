from django.conf.urls import url

from . import views

# url routes 
urlpatterns = [
    url(r'^$', views.welcome, name='welcome')
]