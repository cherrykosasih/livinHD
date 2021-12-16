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
import functions.unit as u

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
        if request.form.get("show_profile"):
            return redirect(url_for('profile',profile_email=current_email))
        elif request.form.get("savetodo"):
            todos=request.form.getlist('td')
            todoschecks=request.form.getlist('c')
            db.update_to_do_list(current_email,todos)
            db.update_to_do_check(current_email,todoschecks)
            return redirect(url_for('home',home_email=current_email))
    elif request.method=="GET":
        current_data=db.retrieve_user_data(current_email)
        fname = current_data[0][0]
        lname = current_data[0][1]
        phone = current_data[0][3]
        ig = current_data[0][4]
        faculty = current_data[0][5]
        fullname= fname+" "+lname
        todos = db.get_user_to_do(current_email)
        todoschecks = db.get_to_do_check(current_email)
        td1= u.unit_n(0,todos)
        td2= u.unit_n(1,todos)
        td3= u.unit_n(2,todos)
        td4= u.unit_n(3,todos)
        td5= u.unit_n(4,todos)
        c1=u.unit_n(0,todoschecks)
        c2=u.unit_n(1,todoschecks)
        c3=u.unit_n(2,todoschecks)
        c4=u.unit_n(3,todoschecks)
        c5=u.unit_n(4,todoschecks)
        
        return render_template("home_fix_2.html",fullname=fullname,user_email=current_email,phone=phone,ig=ig,faculty=faculty,td1=td1,td2=td2,td3=td3,td4=td4,td5=td5,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)

@app.route('/signup_details/<signup_email>',methods=["POST","GET"])
def signup_details(signup_email):
    current_email = session.get("session_email",None)
    if request.method=="GET":
        return render_template("sign_up_details.html",signup_email=current_email)
    elif request.method=="POST":
        gender = request.form['gender']
        relationship = request.form['relationship']
        language = request.form['language']
        unit = request.form['units']
        # unit = request.form['unit'].split(',')
        # club_and_org = request.form['club_and_org'].split(',')
        movie = request.form.getlist('movie')
        music = request.form.getlist('music')
        # celebrity =  request.form['celebrity'].split(',')
        # fandom =  request.form['fandom'].split(',')
        # game =  request.form['game'].split(',')
        # hobby =  request.form['hobby'].split(',')
        # interest = club_and_org + movie + music + celebrity + fandom + game + hobby
        db.update_gender(current_email,gender)
        db.update_relationship(current_email,relationship)
        db.update_language(current_email,language)
        db.insert_unit(current_email,unit)
        db.insert_movie(current_email,movie)
        db.insert_music(current_email,music)
        db.initialize_to_do_list(current_email)
        # db.update_unit(current_email,unit)
        # db.update_interest(current_email,interest)
        return redirect(url_for('login'))

@app.route('/profile/<profile_email>',methods=["POST","GET"])
def profile(profile_email):
    current_email = session.get("session_email",None)
    current_data=db.retrieve_user_data(current_email)
    # user_fname,user_lname,user_email,user_phone,user_ig,user_faculty,status
    fname = current_data[0][0]
    lname = current_data[0][1]
    phone = current_data[0][3]
    ig = current_data[0][4]
    faculty = current_data[0][5]
    status = current_data[0][6]
    language = current_data[0][7]
    gender =current_data[0][8]
    relationship=current_data[0][9]
    fullname= fname+" "+lname

    user_units = db.retrieve_unit_of_user(current_email)
    movies = db.retrieve_movie_of_user(current_email)
    musics = db.retrieve_music_of_user(current_email)
    user_interest = movies+musics
    if request.method=="GET":
        return render_template("profile.html",fullname=fullname,user_email=current_email,phone=phone,ig=ig,faculty=faculty,stats=status,lang=language,gender=gender,relationship=relationship,interest=user_interest,units=user_units)
    elif request.method=="POST":
        status = str(request.form['status'])
        db.update_status(current_email,status)
        return redirect(url_for('home',home_email=current_email))
        # return render_template("profile.html",fullname=fullname,user_email=current_email,phone=phone,ig=ig,faculty=faculty,stats=status)

@app.route('/signup/',methods=["POST","GET"])
def signup():
    # (fname,lname,email,phone,ig,faculty,password,gender,relation,language)
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
        session["session_email"]=email
        if su.email_validator(email)==False:
            msg="Not a valid email"
            return render_template('signup_fix.html',message=msg)
        else:
            try:
                db.insert_user(fname,lname,email,phone,ig,faculty,password,None,None,None)
            except sqlite3.IntegrityError:
                msg="email has been used before"
                return render_template('signup_fix.html',message=msg)
        return redirect(url_for('signup_details',signup_email=email))

# @app.route('/profile/<profile_email>',methods=["POST","GET"])
# def profile(profile_email):
#     current_email = session.get("session_email",None)
#     current_data=db.retrieve_user_data(current_email)
#     fname = current_data[0][0]
#     lname = current_data[0][1]
#     phone = current_data[0][3]
#     ig = current_data[0][4]
#     faculty = current_data[0][5]
#     status = current_data[0][6]
#     fullname= fname+" "+lname
#     if request.method=="GET":
#         return render_template("profile.html",fullname=fullname,user_email=current_email,phone=phone,ig=ig,faculty=faculty,stats=status)
#     elif request.method=="POST":
#         status = str(request.form['status'])
#         db.update_status(current_email,status)
#         return redirect(url_for('home',home_email=current_email))
        

@app.route('/find_friends_new',methods=["POST","GET"])
def find_friends_new():
    current_email = session.get("session_email",None)
    return render_template("find_friend_new.html",user_email=current_email)

@app.route('/find_friends_last/<find_friend_email>',methods=["POST","GET"])
def find_friends_last(find_friend_email):
    current_email = session.get("session_email",None)
    units = db.retrieve_unit_of_user(current_email)
    unit1 = u.unit_n(0,units)
    unit2 = u.unit_n(1,units)
    unit3 = u.unit_n(2,units)
    unit4 = u.unit_n(3,units)
    relevant_data =db.data_for_explore(current_email)
    if request.method=="GET":
        return render_template("find_friend_last.html",profiles=relevant_data,user_email=current_email,unit1=unit1,unit2=unit2,unit3=unit3,unit4=unit4)
    elif request.method=="POST":
        if request.form.get("name"):
            name_filter = request.form["name"]
            relevant_data= db.data_based_on_name(name_filter)
            return render_template("find_friend_last.html",profiles=relevant_data,user_email=current_email,unit1=unit1,unit2=unit2,unit3=unit3,unit4=unit4)
        elif request.form.get("unit"):
            unit_filter=request.form["unit"]
            relevant_data = db.data_based_on_unit(unit_filter,current_email)
            return render_template("find_friend_last.html",profiles=relevant_data,user_email=current_email,unit1=unit1,unit2=unit2,unit3=unit3,unit4=unit4)
        elif request.form.get("movie"):
            movie_filter=request.form["movie"]
            relevant_data=db.data_based_on_movie_interest(movie_filter,current_email)
            return render_template("find_friend_last.html",profiles=relevant_data,user_email=current_email,unit1=unit1,unit2=unit2,unit3=unit3,unit4=unit4)
        elif request.form.get("music"):
            music_filter=request.form["music"]
            relevant_data=db.data_based_on_music_interest(music_filter,current_email)
            return render_template("find_friend_last.html",profiles=relevant_data,user_email=current_email,unit1=unit1,unit2=unit2,unit3=unit3,unit4=unit4)
        else:
            return render_template("find_friend_last.html",profiles=relevant_data,user_email=current_email,unit1=unit1,unit2=unit2,unit3=unit3,unit4=unit4)

@app.route('/find_study_sessions/<find_study_email>',methods=["POST","GET"])
def find_study_sessions(find_study_email):
    current_email = session.get("session_email",None)
    units = db.retrieve_unit_of_user(current_email)
    unit1 = u.unit_n(0,units)
    unit2 = u.unit_n(1,units)
    unit3 = u.unit_n(2,units)
    unit4 = u.unit_n(3,units)
    sessions = db.get_study_session()
    if request.method=="GET":
        return render_template("find_study_sessions.html", sessions=sessions,unit1=unit1,unit2=unit2,unit3=unit3,unit4=unit4,user_email=current_email)
    elif request.method=="POST":
        if request.form.get("unit"):
            unit_filter=request.form["unit"]
            sessions = db.session_based_on_unit(unit_filter)
            return render_template("find_study_sessions.html",sessions=sessions,unit1=unit1,unit2=unit2,unit3=unit3,unit4=unit4,user_email=current_email)
        elif request.form.get("name"):
            name_filter = request.form["name"]
            sessions = db.session_based_on_name(name_filter)
            return render_template("find_study_sessions.html",sessions=sessions,unit1=unit1,unit2=unit2,unit3=unit3,unit4=unit4,user_email=current_email)
        else:
            return render_template("find_study_sessions.html",sessions=sessions,unit1=unit1,unit2=unit2,unit3=unit3,unit4=unit4,user_email=current_email)

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
        meeting_password =request.form['meeting_password']
        unit=request.form['unit']
        try:
            db.insert_study_session(session_name,session_description,meeting_link,meeting_id,meeting_password,unit)
        except sqlite3.IntegrityError:
            return render_template('create_session.html',user_email=current_email)
        return redirect(url_for('find_study_sessions',find_study_email=current_email))

if __name__ == '__main__':
    app.run(debug=True)