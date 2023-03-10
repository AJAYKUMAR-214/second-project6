from app1.views import *
from django.urls import path
app_name='haroin'
urlpatterns=[
    path("powerstar/",powerstar,name="powerstar"),


]