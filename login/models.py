# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import connection
from django.db import models
from django.contrib.auth.models import AbstractUser
from random import randint

class users_profile(models.Model):
    USEREMAIL = models.CharField(max_length = 100)
    USERNAME = models.CharField(max_length = 100)
    CONTACT = models.CharField(max_length = 100)
    BLOOD_GP = models.CharField(max_length = 100)
    GENDER = models.CharField(max_length = 100)
    AGE = models.IntegerField()
    ADDRESS = models.CharField(max_length = 100)
    CITY = models.CharField(max_length = 100)
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
    user = models.CharField(max_length = 100)
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
    otp_object = userOTP(user = user, purpose = purpose, otp = otp)
    otp_object.save()
    otp_object_user = users.objects.get(USERNAME = user)
    return otp_object.id , otp, otp_object_user.NAME

def get_valid_otp_object(id= None, otp = None):
    try:
        otp_object = userOTP.objects.get(id=id, otp=otp)
        obj = users.objects.get(USERNAME=otp_object.user)
        return otp_object, obj
    except userOTP.DoesNotExist:
        return None, None

def set_password_otp(otp_object, encrypted_password):
    emailAddress = otp_object.USERNAME
    obj = users.objects.get(USERNAME=emailAddress)
    obj.PASSWORD = encrypted_password
    obj.save()
  
def verifyLogin(userEmail):
    try:
        login_object = users.objects.get(USERNAME=userEmail)
    except users.DoesNotExist:
        login_object = None
    return login_object

def checkUser(userName):
    try:
        login_object = users.objects.get(USERNAME=userName)
    except users.DoesNotExist:
        login_object = None
    return login_object
    
def signUpUser(userEmail, userName, encrypted_password, dept):
    userAccount = users(USERNAME=userEmail, NAME=userName, PASSWORD=encrypted_password, DEPARTMENT=dept)
    userAccount.save()

def enterUserDetails(USEREMAIL, USERNAME, CONTACT,BLOOD_GP,GENDER,AGE,ADDRESS,CITY,DONATE_Bf):
    print USEREMAIL, USERNAME, CONTACT,BLOOD_GP,GENDER,AGE,ADDRESS,CITY,DONATE_Bf
    userAccount = users_profile(USEREMAIL = USEREMAIL, USERNAME = USERNAME, CONTACT = CONTACT,BLOOD_GP = BLOOD_GP,GENDER = GENDER,AGE = AGE,ADDRESS = ADDRESS,CITY = CITY,DONATE_Bf = DONATE_Bf)
    userAccount.save()
    
def GetUserDetails(userEmail):
    try:
        user_object = users_profile.objects.get(USEREMAIL=userEmail)
    except users_profile.DoesNotExist:
        user_object = None
    return user_object