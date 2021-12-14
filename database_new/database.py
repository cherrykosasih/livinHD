import sqlite3

# from functions.signup import email_validator

conn = sqlite3.connect('database_new/database.db',check_same_thread=False)

# conn.execute('CREATE TABLE IF NOT EXISTS user(user_id INTEGER PRIMARY KEY AUTOINCREMENT,user_fname TEXT,user_lname TEXT, user_email TEXT,user_phone TEXT, user_ig TEXT, user_faculty TEXT,user_pwd TEXT, user_gender TEXT,user_relationship TEXT,user_language TEXT)')
# conn.execute('CREATE TABLE IF NOT EXISTS contact(user1_id INTEGER PRIMARY KEY, user2_id INTEGER)')
# conn.execute(('CREATE TABLE IF NOT EXISTS unit(unit_id TEXT, unit_name TEXT)'))
# conn.execute(('CREATE TABLE IF NOT EXISTS enrolment(user_id INTEGER, unit_id INTEGER, PRIMARY KEY(user_id,unit_id))'))
# conn.close()

def insert_user(fname,lname,email,phone,faculty,ig,password,gender,relation,language):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    conn.execute('INSERT INTO user(user_fname,user_lname,user_email,user_phone,user_ig,user_faculty,user_pwd,user_gender,user_relationship,user_language) VALUES (?,?,?,?,?,?,?,?,?,?)' ,(fname,lname,email,phone,ig,faculty,password,gender,relation,language))
    conn.commit()
    conn.close()

def login_validator(email,password):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    c= conn.cursor()
    c.execute("SELECT count(*) FROM user WHERE user_email= ? AND user_pwd= ?",(email,password))
    a=c.fetchone()
    return True if a[0]>=1 else False 

def password_login_validator(email,password):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    c= conn.cursor()
    c.execute("SELECT count(*) FROM user WHERE user_email= ?",(email,))

def insert_study_session(session_name,session_description,meeting_link,meeting_id,meeting_password):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    conn.execute('INSERT INTO study_session(session_name,session_description,meeting_link,meeting_id,meeting_password) VALUES (?,?,?,?,?)' ,(session_name,session_description,meeting_link,meeting_id,meeting_password))
    conn.commit()
    conn.close()

def get_study_session():
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT * FROM study_session")
    data = c.fetchall()
    return data

def retrieve_user_data(email):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    c= conn.cursor()
    c.execute('SELECT user_fname,user_lname,user_email,user_phone,user_ig,user_faculty FROM user WHERE user_email=?',(email,))
    a = c.fetchall()
    conn.close()
    return a
    
# insert_user('cherry','kosasih','ckos0005','09138013','soit','ck','lala','f','jones','indo')
# insert_user('cherry','kosasih','ckos0005','09138013','soit','ck','lala','f','jones','indo')
# print("jancok")

# conn.execute('DROP TABLE user')
# conn.execute('CREATE TABLE IF NOT EXISTS user(user_id INTEGER PRIMARY KEY AUTOINCREMENT,user_fname TEXT,user_lname TEXT, user_email TEXT UNIQUE,user_phone TEXT, user_ig TEXT, user_faculty TEXT,user_pwd TEXT, user_gender TEXT,user_relationship TEXT,user_language TEXT)')
# conn.close()

# conn.execute("ALTER TABLE user ADD viewed INTEGER DEFAULT 0")
# conn.close()
# print(login_validator("ckos0005","lala"))
# print(login_validator("ckos0005","gege"))
# conn.close()

# conn.execute("UPDATE user SET user_pwd= 'user' WHERE user_fname='jane'")
# conn.commit()
# conn.close()