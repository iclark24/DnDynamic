from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='index'),
    url(r'^races/', views.races, name='races'),
    url(r'^classes/', views.classes, name='classes'),
    url(r'^feats/', views.feats, name='feats'),
    url(r'^features/', views.features, name='features'),
    url(r'^spells/', views.spells, name='spells'),
    url(r'^creator/', views.creator, name='creator'),
    url(r'^contact/', views.contact, name='contact'),
]
