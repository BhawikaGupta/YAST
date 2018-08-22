from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash


app = Flask(__name__)

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'YAST'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

master_data = None

@app.route("/")
def main():
    return render_template('login.html')

@app.route("/signup")    
def signUp():
    return render_template('signup.html') 

@app.route("/cuDashboard")    
def cuDashboard():
    return render_template('cuDashboard.html') 
    

if __name__ == "__main__":
    app.run()    