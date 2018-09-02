from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^topDonors/', views.topDonors, name='topDonors')
]