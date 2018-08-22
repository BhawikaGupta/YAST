from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
import ConfigParser

mysql = MySQL()

class dbConnect: 
    def __init__(self, app):
        config = ConfigParser.ConfigParser()
        config.read('config/config.ini')
        app.config['MYSQL_DATABASE_USER'] = config.get('db', 'MYSQL_DATABASE_USER')
        app.config['MYSQL_DATABASE_PASSWORD'] = config.get('db', 'MYSQL_DATABASE_PASSWORD')
        app.config['MYSQL_DATABASE_DB'] = config.get('db', 'MYSQL_DATABASE_DB')
        app.config['MYSQL_DATABASE_HOST'] = config.get('db', 'MYSQL_DATABASE_HOST')        
        mysql.init_app(app)


    def connect(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        return conn, cursor
        
    def disconnect(self, conn, cursor):
        cursor.close() 
        conn.close()  