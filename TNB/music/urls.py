from django.conf.urls import url
from . import views

urlpatterns = [
    #default view for .com/music/
    url(r'^$', views.index, name='index'),

    #.com/music/725/
    #.com/music/128/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]