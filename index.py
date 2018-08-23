from flask import Flask, render_template, request, json, session
from collections import OrderedDict
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
import sys
sys.path.append('config/')
from dbConnect import dbConnect
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.secret_key = "zahra"
db = dbConnect(app)


@app.route("/cuDashboard")    
def cuDashboard():
    login_info = session.get('username', "guest")
    print login_info[1]
    conn, cursor = db.connect()
    user = OrderedDict() 
    user["useremail"]=login_info[0],
    user["username"]=login_info[1].encode("utf-8"),
    user["contact"]="",
    user["blood"]="",
    user["gender"]="",
    user["age"]="",
    user["location"]="",
    user["donate"]=""

    sql = "select * from users_profile where USEREMAIL='%s'" % (login_info[0])
    cursor.execute(sql)
    rows = cursor.fetchone()
    print rows
    conn.commit()
    db.disconnect(conn, cursor)
    if(rows):
        count = 0 
        for key in user:
            if key == "username":
                continue
            else:
                user[key] = rows[count].encode("utf-8")
                count = count +1
    user["username"]=user["username"][0]
    user_data = dict(user)
    
    return render_template('cuDashboard.html',data=user_data) 

@app.route("/signup",methods=['POST','GET'])    
def signUp():
    if request.method == 'POST':
        conn, cursor = db.connect()
        userName = request.form['nameUser']
        userEmail = request.form['emailUser']
        userPassword = request.form['passwordUser']
        dept = "Volunteer"
        sql = "select * from users where USERNAME='%s'" % (userEmail)
        cursor.execute(sql)
        rows = cursor.fetchone()
        conn.commit()
        if(rows):
            return json.dumps({'message':'User Already Exists. Please login'}) 
        else:
            encrypted_password = sha256_crypt.encrypt(userPassword)
            sql = "insert into users(USERNAME, NAME, PASSWORD, DEPARTMENT) values('%s','%s','%s', '%s')" % (userEmail, userName, encrypted_password, dept)
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
        sql = "select USERNAME,NAME,PASSWORD from users where USERNAME='%s'" % (userEmail)
        cursor.execute(sql)
        rows = cursor.fetchone()
        print rows
        conn.commit()
        db.disconnect(conn, cursor)
        if(rows):
            if(sha256_crypt.verify(userPassword, rows[2])):
                session['username'] = [rows[0],rows[1]]
                return json.dumps({'message':'success'}) 
            else:
                return json.dumps({'message':'Enter correct password'})   
        else:
            return json.dumps({'message':'Entered username is not registered'}) 
    else:
        return render_template('login.html')         
        
if __name__ == "__main__":
    app.run()    
