# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import connection


def verifyLogin(userEmail):
    cursor = connection.cursor()
    cursor.execute("select PASSWORD from users where USERNAME='%s'" % (userEmail))
    row = cursor.fetchone()
    cursor.close()
    return row

def checkUser(userName):
    cursor = connection.cursor()
    sql = "select * from users where USERNAME='%s'" % (userName)
    cursor.execute(sql)
    row = cursor.fetchone()
    cursor.close()
    return row
    
def signUpUser(userEmail, userName, encrypted_password, dept):
    cursor = connection.cursor()
    sql = "insert into users(USERNAME, NAME, PASSWORD, DEPARTMENT) values('%s','%s','%s', '%s')" % (userEmail, userName, encrypted_password, dept)
    cursor.execute(sql)
    cursor.close()