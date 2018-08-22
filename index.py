from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
import sys
sys.path.append('config/')
from dbConnect import dbConnect
from passlib.hash import sha256_crypt

app = Flask(__name__)
db = dbConnect(app)

@app.route("/cuDashboard")    
def cuDashboard():
    return render_template('cuDashboard.html') 

@app.route("/signup",methods=['POST','GET'])    
def signUp():
    if request.method == 'POST':
        conn, cursor = db.connect()
        userName = request.form['nameUser']
        userEmail = request.form['emailUser']
        userPassword = request.form['passwordUser']
        sql = "select * from users where USERNAME='%s'" % (userEmail)
        cursor.execute(sql)
        rows = cursor.fetchone()
        conn.commit()
        if(rows):
            return json.dumps({'message':'User Already Exists. Please login'}) 
        else:
            encrypted_password = sha256_crypt.encrypt(userPassword)
            sql = "insert into users(USERNAME, NAME, PASSWORD) values('%s','%s','%s')" % (userEmail, userName, encrypted_password)
            cursor.execute(sql)
            conn.commit()
            return json.dumps({'message':'success'}) 
        db.disconnect(conn, cursor)
    else:
        return render_template('signup.html')    


@app.route("/",methods=['POST','GET'])
def main():
    if request.method == 'POST':
        conn, cursor = db.connect()
        userEmail = request.form['userEmail']
        userPassword = request.form['userPassword']
        sql = "select PASSWORD from users where USERNAME='%s'" % (userEmail)
        cursor.execute(sql)
        rows = cursor.fetchone()
        conn.commit()
        db.disconnect(conn, cursor)
        if(rows):
            if(sha256_crypt.verify(userPassword, rows[0])):
                return json.dumps({'message':'success'}) 
            else:
                return json.dumps({'message':'Enter correct password'})   
        else:
            return json.dumps({'message':'Entered username is not registered'}) 
    else:
        return render_template('login.html')         
        
if __name__ == "__main__":
    app.run()    
