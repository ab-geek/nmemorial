from django.conf.urls import url
from django.contrib import admin

from backend.views import *


urlpatterns = [
    url(r'^$',home,name='home'),
    url(r'^api/$', home,name='home'),

    #url(r'^api/(?P<string>\w+)/get/', views.get_data),
    url(r'^api/login/', login),
    url(r'^api/register/', register),
    url(r'^api/forgot_pw/',forgot_pw),
    #url(r'^api/get_pins/', views.get_pins),
    #url(r'^api/add_pins/', views.add_pins),
    url(r'^api/search/(?P<memorial_name>[\w+\s+]+)',search),
    url(r'^api/add_story/',add_story),
    url(r'^api/edit_story/(?P<memorial_id>\w+)',edit_story),
    url(r'^api/delete_story/(?P<memorial_id>\w+)',delete_story)

]
