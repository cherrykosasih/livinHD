#pip3 install virtualenv
#virtualenv flask
#cd flask
#source bin/activate
#pip3 install flask
#python3 main.py
from os import stat
from flask import Flask,render_template,url_for,request,flash,redirect,session
import database_new.database as db
import sqlite3
import functions.signup as su
#from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

current_user_email = None
app = Flask(__name__,template_folder='templates',static_folder='static')
app.secret_key='lmao'
@app.route('/',methods=["POST","GET"])
@app.route('/login',methods=["POST","GET"])
def login():
    if request.method=="GET":
        return render_template("login_fix.html")
    elif request.method=="POST":
        email = request.form['email']
        password = request.form['password']
        session["session_email"]=email
        if db.login_validator(email,password):
            return redirect(url_for('home',home_email=str(email))) #this is supposed to be home, but no home.html yet
        else:
            msg="Invalid email/password"
        return render_template("login_fix.html",message=msg)
    else : 
        return render_template("login_fix.html")

@app.route('/home/<home_email>',methods=["GET","POST"])
def home(home_email):
    current_email=session.get("session_email",None)
    if request.method=="POST":
        return redirect(url_for('profile',profile_email=current_email))
    elif request.method=="GET":
        # [0][0] fname
        # [0][1] lname
        # [0][2] email
        # [0][3] phone
        # [0][4] ig
        # [0][5] faculty
        current_data=db.retrieve_user_data(current_email)
        fname = current_data[0][0]
        lname = current_data[0][1]
        phone = current_data[0][3]
        ig = current_data[0][4]
        faculty = current_data[0][5]
        fullname= fname+" "+lname
        return render_template("home_fix_2.html",fullname=fullname,user_email=current_email,phone=phone,ig=ig,faculty=faculty)

@app.route('/profile/<profile_email>',methods=["POST","GET"])
def profile(profile_email):
    current_email = session.get("session_email",None)
    current_data=db.retrieve_user_data(current_email)
    fname = current_data[0][0]
    lname = current_data[0][1]
    phone = current_data[0][3]
    ig = current_data[0][4]
    faculty = current_data[0][5]
    status = current_data[0][6]
    fullname= fname+" "+lname
    if request.method=="GET":
        return render_template("profile.html",fullname=fullname,user_email=current_email,phone=phone,ig=ig,faculty=faculty,stats=status)
    elif request.method=="POST":
        status = str(request.form['status'])
        db.update_status(current_email,status)
        return render_template("profile.html",fullname=fullname,user_email=current_email,phone=phone,ig=ig,faculty=faculty,stats=status)
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
            msg="Not a valid email"
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
    current_email = session.get("session_email",None)
    return render_template("find_friend_new.html",user_email=current_email)

@app.route('/find_study_sessions',methods=["POST","GET"])
def find_study_sessions():
    current_email = session.get("session_email",None)
    if request.method=="GET":
        return render_template("find_study_sessions.html", sessions = db.get_study_session(),user_email=current_email)
    elif request.method=="POST":
        return render_template("find_study_sessions.html",user_email=current_email)

@app.route('/create_study_session',methods=["POST","GET"])
def create_study_session():
    current_email=session.get("session_email",None)
    if request.method=="GET":
        return render_template("create_session.html",user_email=current_email)
    elif request.method=="POST":
        session_name=request.form['session_name']
        session_description=request.form['session_description']
        meeting_link=request.form['meeting_link']
        meeting_id=request.form['meeting_id']
        meeting_password   =request.form['meeting_password']
        try:
            db.insert_study_session(session_name,session_description,meeting_link,meeting_id,meeting_password)
        except sqlite3.IntegrityError:
            return render_template('create_session.html',user_email=current_email)
        return redirect(url_for('find_study_sessions'))

if __name__ == '__main__':
    app.run(debug=True)