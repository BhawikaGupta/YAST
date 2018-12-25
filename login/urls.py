from django.conf.urls import *
from django.contrib import admin
from login.views import *


urlpatterns = [url(r'^profile/$', UserList.as_view(), name='All Users'),
               url(r'^(?P<blood_group>[a-zA-Z+-]{2,3})/$', UserBloodList.as_view(), name='All Blood Group Users'),
               url(r'^campaign/$', CreateCampaignView.as_view(), name='Add Campaigns'),
               url(r'^campaign/(?P<id>[C]{1}(\d+))/$', CreateCampaignView.as_view(), name='Update Campaigns'),
               url(r'^login/$', loginTokenGeneration, name='Create Token')
               ]