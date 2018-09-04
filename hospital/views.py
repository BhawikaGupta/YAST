# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
import json
from models import *

# Create your views here.


def topDonors(request):
    if request.method == 'GET':
        rows = GetDonorPredict()
        return render(request, 'hpDonorList.html', {"data":rows})

def sendemail(request):        
    if request.method == 'GET':
        msg_html = render_to_string('DonorReachOut.html', { 'email': request.GET['email'], 'bloodgroup':request.GET['bloodgroup']})
        send_mail('Blood Required Urgently',"Hi",None,[request.GET['email']],html_message=msg_html)
        return HttpResponse(str(json.dumps({'message':'Donor Reachout Email has been sent!'})))    