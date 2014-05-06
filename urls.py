from django.conf.urls import patterns, include, url

from foods.views import ItemAdd

urlpatterns = patterns('',
    url(r'^$', ItemAdd.as_view(), name='index'),
)
