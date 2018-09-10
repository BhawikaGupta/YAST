from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^topDonors/', views.topDonors, name='topDonors'),
    url(r'^dashboard/', views.hpDashboard, name='hpDashboard'),
    url(r'^bloodMonitor/', views.hpbloodMonitor, name='hpbloodMonitor'),
    url(r'^sendemail/', views.sendemail, name='topDonors'),
    url(r'^reward/', views.reward, name='reward'),
    url(r'^network/', views.network, name='network')
]