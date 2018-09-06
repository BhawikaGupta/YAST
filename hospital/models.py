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
       
       
class hospital_info(models.Model):
    HOSPITAL_ID = models.IntegerField(primary_key=True)
    CHAIN_ID = models.IntegerField()
    HOSPITAL_NAME = models.CharField(max_length = 100)
    CHAIN_NAME = models.CharField(max_length = 100)
    ZIP = models.CharField(max_length = 100)
    ADDRESS = models.CharField(max_length = 100)
    CITY = models.CharField(max_length = 100)
    STATE = models.CharField(max_length = 120)
    COUNTRY = models.CharField(max_length = 100)
    LONGITUDE = models.CharField(max_length = 100)
    LATITUDE = models.CharField(max_length = 100)
    CONTACT_NO = models.CharField(max_length = 100)
    EMAIL = models.CharField(max_length = 100)   
    HOSPITAL_OWNERSHIP = models.CharField(max_length = 100)   
    HOSPITAL_TYPE = models.CharField(max_length = 100)       
    BLOOD_COLL_FACILITY = models.CharField(max_length = 100)
    APositive = models.IntegerField()
    ABPositive = models.IntegerField()
    OPositive = models.IntegerField()
    BPositive = models.IntegerField()
    ANegative = models.IntegerField()
    ABNegative = models.IntegerField()
    ONegative = models.IntegerField()
    BNegative = models.IntegerField()
    TOTAL_BEDS = models.IntegerField()
    SPECIALITY = models.CharField(max_length = 100)
    STAFF_COUNT = models.IntegerField()
    DOCTOR_COUNT = models.IntegerField()
    FOOTFALL = models.IntegerField()


    
    def __str__(self):
       return '%s (%s)' % (str(self.HOSPITAL_NAME),self.CITY)       
       
       
class blood_bank_master(models.Model):
    BLOOD_ID = models.IntegerField(primary_key=True)
    HOSPITAL_ID = models.IntegerField()
    DONOR_OP_ID = models.IntegerField()
    BLOOD_QTY = models.IntegerField()
    DONATION_DATE = models.CharField(max_length = 100)
    DONATION_TIME = models.CharField(max_length = 100)
    BLOOD_STATUS = models.CharField(max_length = 100)
    SYSPHILIS = models.CharField(max_length = 100)
    HIV_POS = models.CharField(max_length = 100)
    HEPATITUS_POS = models.CharField(max_length = 100)
    OTHER_DISEASE = models.CharField(max_length = 100)
    BLOOD_COLL_METHOD = models.CharField(max_length = 100)
    BLOOD_DON_TYPE = models.CharField(max_length = 100)    
    BLOOD_INTEND_USE = models.CharField(max_length = 100)    
    def __str__(self):
       return '%s' % (str(self.BLOOD_ID))              

