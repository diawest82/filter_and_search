from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.mineral_list, name='list'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<letter>[a-zA-Z])/$', views.mineral_letter_list, name='letter'),
    url(r'^(?P<group>[a-zA-Z\s]+)/$', views.search_group, name='group'),
    url(r'^(?P<pk>\d+)/$', views.mineral_detail, name='detail'),
]
