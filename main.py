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
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

current_user_email = None
app = Flask(__name__,template_folder='templates',static_folder='static')

@app.route('/',methods=["POST","GET"])
@app.route('/login',methods=["POST","GET"])
def login():
    if request.method=="GET":
        return render_template("login_fix.html")
    elif request.method=="POST":
        email = request.form['email']
        password = request.form['password']
        if db.login_validator(email,password):
            return redirect(url_for('home')) #this is supposed to be home, but no home.html yet
        else:
            msg="invalid email/password"
        return render_template("login_fix.html",message=msg)

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
        return render_template("signup_fix.html")
    elif request.method=="POST":
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        phone=request.form['phone']
        ig   =request.form['ig']
        faculty = request.form['faculty']
        password = request.form['password']
        if su.email_validator(email)==False:
            msg="not a valid email"
            return render_template('signup_fix.html',message=msg)
        else:
            try:
                db.insert_user(fname,lname,email,phone,ig,faculty,password,None,None,None)
            except sqlite3.IntegrityError:
                msg="email has been used before"
                return render_template('signup_fix.html',message=msg)
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
        return render_template("find_study_sessions.html", sessions = db.get_study_session())
    elif request.method=="POST":
        return render_template("find_study_sessions.html")

@app.route('/create_study_session',methods=["POST","GET"])
def create_study_session():
    if request.method=="GET":
        return render_template("create_session.html")
    elif request.method=="POST":
        session_name=request.form['session_name']
        session_description=request.form['session_description']
        meeting_link=request.form['meeting_link']
        meeting_id=request.form['meeting_id']
        meeting_password   =request.form['meeting_password']
        try:
            db.insert_study_session(session_name,session_description,meeting_link,meeting_id,meeting_password)
        except sqlite3.IntegrityError:
            return render_template('create_session.html')
        return redirect(url_for('find_study_sessions'))

if __name__ == '__main__':
    app.run(debug=True)