from django.conf.urls import patterns, include, url

from foods.views import ItemAdd, testform

urlpatterns = patterns('',
#    url(r'^$', ItemAdd.as_view(), name='index'),
#    url(r'^testform/$', testform, name='testform'),
    url(r'^$', testform, name='index'),
    url(r'^testform/$', ItemAdd.as_view(), name='testform'),
)
