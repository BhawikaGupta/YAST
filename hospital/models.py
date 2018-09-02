# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import connection
from django.db import models
from django.contrib.auth.models import AbstractUser
from random import randint

# Create your models here.
class donor_predict(models.Model):
    OP_ID = models.IntegerField(primary_key=True)
    AGE = models.IntegerField()
    OCCUPATION = models.CharField(max_length = 100)
    GENDER = models.CharField(max_length = 100)
    MARRIED = models.CharField(max_length = 100)    
    CITY = models.CharField(max_length = 100)
    COUNTRY = models.CharField(max_length = 100)
    CHANNEL = models.CharField(max_length = 100)
    CONTACT = models.CharField(max_length = 100)
    EMAIL = models.CharField(max_length = 100)    
    EDU_LEVEL = models.CharField(max_length = 100)
    FAMILY_MEM = models.CharField(max_length = 100)
    TOTAL_HISTORICAL_DON = models.CharField(max_length = 100)
    LAST_DONATED = models.CharField(max_length = 100)
    OTHER_DONATION =  models.CharField(max_length = 100)
    WEIGHT = models.FloatField()
    HEIGHT = models.FloatField()
    BLOOD_GROUP = models.CharField(max_length = 100)
    NET_SCORE = models.FloatField()
    NET_RANK = models.IntegerField()
    TARGET_STATUS = models.CharField(max_length = 100)
    
    def __str__(self):
       return '%s (%s)' % (str(self.OP_ID),self.BLOOD_GROUP)