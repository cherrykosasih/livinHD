#pip3 install virtualenv
#virtualenv flask
#cd flask
#source bin/activate
#pip3 install flask
#python3 main.py
from flask import Flask,render_template,url_for,request,flash,redirect
import database_new.database as db
import sqlite3
import functions.signup as su
import webbrowser

current_user_email = None
app = Flask(__name__,template_folder='templates',static_folder='static')

@app.route('/',methods=["POST","GET"])
@app.route('/login',methods=["POST","GET"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    elif request.method=="POST":
        email = request.form['email']
        password = request.form['password']
        if db.login_validator(email,password):
            return redirect(url_for('home')) #this is supposed to be home, but no home.html yet
        return render_template("login.html")

@app.route('/home',methods=["POST","GET"])
def home():
    if request.method=="POST":
        return render_template("new_home.html")
    elif request.method=="GET":
        return render_template("new_home.html")

@app.route('/profile',methods=["POST","GET"])
def profile():
    return render_template("profile.html")

@app.route('/signup/',methods=["POST","GET"])
def signup():
    if request.method=="GET":
        return render_template("signup.html")
    elif request.method=="POST":
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        phone=request.form['phone']
        ig   =request.form['ig']
        faculty = request.form['faculty']
        password = request.form['password']
        if su.email_validator(email)==False:
            return render_template('signup.html')
        else:
            try:
                db.insert_user(fname,lname,email,phone,ig,faculty,password,None,None,None)
            except sqlite3.IntegrityError:
                return render_template('signup.html')
        return render_template('sign_up_details.html')

@app.route('/signup_details',methods=["POST","GET"])
def sign_up_details():
    return render_template("sign_up_details.html")

@app.route('/find_friends',methods=["POST ","GET"])
def find_friend():
    return render_template("find-friend.html")

@app.route('/find_friends_new',methods=["POST","GET"])
def find_friends_new():
    return render_template("find_friend_new.html")

@app.route('/find_study_sessions',methods=["POST","GET"])
def find_study_sessions():
    if request.method=="GET":
        return render_template("find_study_sessions.html")
    elif request.method=="POST":
        return render_template("find_study_sessions.html")

@app.route('/create_study_session',methods=["POST","GET"])
def create_study_session():
    return render_template("create_session.html")
if __name__ == '__main__':
    app.run(debug=True)