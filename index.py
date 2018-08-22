from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
import sys
sys.path.append('config/')
from dbConnect import dbConnect

app = Flask(__name__)
db = dbConnect(app)

@app.route("/signup")    
def signUp():
<<<<<<< HEAD
    return render_template('signup.html') 

@app.route("/cuDashboard")    
def cuDashboard():
    return render_template('cuDashboard.html') 
    
=======
    if request.method == 'POST':
        conn, cursor = db.connect()
        
    else:
        return render_template('signup.html')    
>>>>>>> 094af240fc0a7c62aca7ba6d09e4cfee96bc134e

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
            print rows[0]
            print userPassword
            if(rows[0] == userPassword):
                return json.dumps({'message':'success'}) 
            else:
                return json.dumps({'message':'Enter correct password'})   
        else:
            return json.dumps({'message':'Entered username is not registered'}) 
    else:
        return render_template('login.html')         
        
if __name__ == "__main__":
    app.run()    
