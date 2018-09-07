# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


class DonorAdmin(admin.ModelAdmin):
    list_display = ('OP_ID', 'BLOOD_GROUP','EMAIL' ,'NET_SCORE', 'NET_RANK','TARGET_STATUS')
    
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('HOSPITAL_ID', 'HOSPITAL_NAME' ,'CHAIN_NAME')    


# Register your models here.
admin.site.register(donor_predict,DonorAdmin)
admin.site.register(hospital_info,HospitalAdmin)