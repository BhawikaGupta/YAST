# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from models import *
from passlib.hash import sha256_crypt
import json
from django.template import RequestContext
from collections import OrderedDict
from django.core.mail import send_mail
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import resolve
   

def homePage(request):
    return render(request, 'homePage.html', {})

def reset_password(request, id, otp):
    user = {}
    if request.method == 'GET':
        rows, time_model = get_valid_otp_object(id, otp)
        if(rows):
            return render(request, 'resetPassword.html', {})
        else:
            user["message"] = "You entered an Invalid Link"
            return render(request, 'errorPage.html', {"data":user})
    elif request.method == 'POST':
        rows, time_model = get_valid_otp_object(id, otp)
        if(rows):
            resetPassword = request.POST['resetPassword']
            encrypted_password = sha256_crypt.encrypt(resetPassword)
            if(sha256_crypt.verify(resetPassword, time_model.PASSWORD)):
                return HttpResponse(str(json.dumps({'message':'Old Password and New Password are same. Try another password'})))
            else:
                set_password_otp(time_model, encrypted_password)
                return HttpResponse(str(json.dumps({'message':'Password reset successfully! Please Login!'})))
        else:
            user["message"] = "You entered an Invalid Link"
            return render(request, 'errorPage.html', {"data":user})
            
def resetUser(request):
    if request.method == 'GET':
        return render(request, 'resetUser.html', {})
    elif request.method == 'POST':
        userEmail = request.POST['userEmailConfirm']
        rows = checkUser(userEmail)
        if(rows):
            id, otp, userName = create_otp(user = userEmail, purpose = 'FP')
            HOST_METHOD = getattr(settings, "HOST_METHOD", None)
            HOST_ADDRESS = getattr(settings, "HOST_ADDRESS", None)
            HOST_PORT = getattr(settings, "HOST_PORT", None)
            link = HOST_METHOD + '://' + HOST_ADDRESS + ':' + HOST_PORT + '/accounts/reset/%s/%s/' % (id,otp)
            msg_html = render_to_string('passwordRestMailTemplate.html', { 'username': userName, 'link':link})
            send_mail('Password Reset Request',"Hi",None,[userEmail],html_message=msg_html)
            return HttpResponse(str(json.dumps({'message':'Password reset Email has been sent to your link. Please reset and login!'})))
        else:
            return HttpResponse(str(json.dumps({'message':'Entered username is not registered! Please Signup!'})))
        

def cuDashboard(request):
    login_info = request.session.get('username', 'guest')
    user = OrderedDict() 
    user["useremail"]=login_info[0].encode("utf-8"),
    user["username"]=login_info[1].encode("utf-8"),
    user["contact"]="".encode("utf-8"),
    user["blood"]="".encode("utf-8"),
    user["gender"]="".encode("utf-8"),
    user["age"]="".encode("utf-8"),
    user["location"]="".encode("utf-8"),
    user["donate"]="".encode("utf-8")
    rows = GetUserDetails(login_info[0])
    if(rows):
        count = 0 
        for key in user:
            if key == "username":
                continue
            else:
                user[key] = rows[count].encode("utf-8")
                count = count +1
    user["username"]=user["username"][0]
    print user
    return render(request, 'cuDashboard.html', {"data":user})

def login(request):
    if request.method == 'GET':
        return render(request, "login.html", {})
    elif request.method == 'POST':
        userEmail = request.POST['userEmail']
        userPassword = request.POST['userPassword']
        rows = verifyLogin(userEmail)
        if(rows):
            if(sha256_crypt.verify(userPassword, rows.PASSWORD)):
                request.session['username'] = [rows.USERNAME,rows.NAME]
                return  HttpResponse(str(json.dumps({'message':'success'}) ))
            else:
                return HttpResponse(str(json.dumps({'message':'Enter correct password'})))
        else:
            return HttpResponse(str(json.dumps({'message':'Entered username is not registered'})))
   
   
def signup(request):
    if request.method == 'GET':
        return render(request, "signup.html", {})
    elif request.method == 'POST':
        userName = request.POST['nameUser']
        userEmail = request.POST['emailUser']
        userPassword = request.POST['passwordUser']
        dept = "Volunteer"
        row = checkUser(userEmail)
        if(row):
            return HttpResponse(str(json.dumps({'message':'User Already Exists. Please login'})))
        else:
            encrypted_password = sha256_crypt.encrypt(userPassword)
            signUpUser(userEmail, userName, encrypted_password, dept)
            return HttpResponse(str(json.dumps({'message':'success'})))
    
