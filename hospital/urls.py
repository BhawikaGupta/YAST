from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^topDonors/', views.topDonors, name='topDonors'),
    url(r'^sendemail/', views.sendemail, name='topDonors')
]