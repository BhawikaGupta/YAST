# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import donor_predict

class DonorAdmin(admin.ModelAdmin):
    list_display = ('OP_ID', 'BLOOD_GROUP','EMAIL' ,'NET_SCORE', 'NET_RANK','TARGET_STATUS')


# Register your models here.
admin.site.register(donor_predict,DonorAdmin)