# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import connection
from django.db import models
from django.contrib.auth.models import AbstractUser
from random import randint

class users_profile(models.Model):
    USEREMAIL = models.CharField(max_length = 100)
    CONTACT = models.IntegerField()
    BLOOD_GP = models.CharField(max_length = 100)
    GENDER = models.CharField(max_length = 100)
    AGE = models.IntegerField()
    LOCATION = models.CharField(max_length = 100)
    DONATE_Bf = models.CharField(max_length = 100)
    class Meta:
      db_table = "users_profile"

class users(models.Model):
    USERNAME = models.CharField(max_length = 100)
    NAME = models.CharField(max_length = 100)
    PASSWORD = models.CharField(max_length = 100)
    DEPARTMENT = models.CharField(max_length = 100)
    class Meta:
      db_table = "users"
    
class userOTP(models.Model):
    OTP_PURPOSE_CHOICES = (('FP', 'Forgot Password'),('AA', 'Activate Account'));
    user = models.ForeignKey(users)
    otp = models.CharField(max_length = 4)
    purpose = models.CharField(max_length = 2, choices = OTP_PURPOSE_CHOICES)
    created_on = models.DateTimeField(auto_now_add = True)
    class Meta:
        db_table = "userOTP"
        unique_together= ['user', 'purpose']

def create_otp(user = None, purpose = None):
    choices = []
    for choice_purpose, verbose in userOTP.OTP_PURPOSE_CHOICES:
        choices.append(choice_purpose)
    if not purpose in choices:
        raise ValueError('Invalid Arguments');
    if userOTP.objects.filter(user = user, purpose = purpose).exists():
        old_otp = userOTP.objects.get(user = user, purpose = purpose)
        old_otp.delete()
    otp = randint(1000, 9999)
    otp_object = userOTP.objects.create(user = user, purpose = purpose, otp = otp)
    return otp

def get_valid_otp_object(user = None, otp= None, purpose = None):
    if not user:
        raise ValueError("Invalid Arguments");
    choices = []
    for choice_purpose, verbose in userOTP.OTP_PURPOSE_CHOICES:
        choices.append(choice_purpose)
    if not purpose in choices:
        raise ValueError('Invalid Arguments');
    try:
        otp_object = userOTP.objects.get(user = user, purpose=purpose, otp=otp)
        return otp_object
    except userOTP.DoesNotExist:
        return None
    
def verifyLogin(userEmail):
    try:
        login_object = users.objects.get(USERNAME=userEmail)
    except login_object.DoesNotExist:
        login_object = None
    return login_object

def checkUser(userName):
    try:
        login_object = users.objects.get(USERNAME=userName)
    except login_object.DoesNotExist:
        login_object = None
    return login_object
    
def signUpUser(userEmail, userName, encrypted_password, dept):
    users = users(USERNAME=userEmail, NAME=userName, PASSWORD=encrypted_password, DEPARTMENT=dept)
    cursor.close()
    
def GetUserDetails(userEmail):
    try:
        user_object = users_profile.objects.get(USEREMAIL=userEmail)
    except user_object.DoesNotExist:
        user_object = None
    return user_object