from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),
    url(r'^randomword$', views.randomword),
    url(r'^reset$', views.reset)
]
