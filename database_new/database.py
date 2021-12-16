import sqlite3

conn = sqlite3.connect('database_new/database.db',check_same_thread=False)

# conn.execute('CREATE TABLE IF NOT EXISTS user(user_id INTEGER PRIMARY KEY AUTOINCREMENT,user_fname TEXT,user_lname TEXT, user_email TEXT,user_phone TEXT, user_ig TEXT, user_faculty TEXT,user_pwd TEXT, user_gender TEXT,user_relationship TEXT,user_language TEXT)')
# conn.execute('CREATE TABLE IF NOT EXISTS contact(user1_id INTEGER PRIMARY KEY, user2_id INTEGER)')
# conn.execute(('CREATE TABLE IF NOT EXISTS unit(unit_id TEXT, unit_name TEXT)'))
# conn.execute('CREATE TABLE IF NOT EXISTS enrolment(user_email TEXT, unit_id TEXT, PRIMARY KEY(user_email,unit_id))')
# conn.execute('DROP TABLE todo')
# conn.execute('CREATE TABLE IF NOT EXISTS todo(user_email TEXT,task1 TEXT,task2 TEXT,task3 TEXT,task4 TEXT,task5 TEXT)')
# conn.close()

def safe_get_list(n,lst):
    try:
        return lst[n]
    except IndexError:
        return None
        
def insert_user(fname,lname,email,phone,ig,faculty,password,gender,relation,language):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    conn.execute('INSERT INTO user(user_fname,user_lname,user_email,user_phone,user_ig,user_faculty,user_pwd,user_gender,user_relationship,user_language) VALUES (?,?,?,?,?,?,?,?,?,?)' ,
    (fname,lname,email,phone,ig,faculty,password,gender,relation,language))
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

def insert_study_session(session_name,session_description,meeting_link,meeting_id,meeting_password,unit):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    conn.execute('INSERT INTO study_session(session_name,session_description,meeting_link,meeting_id,meeting_password,unit) VALUES (?,?,?,?,?,?)' ,(session_name,session_description,meeting_link,meeting_id,meeting_password,unit))
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
    c.execute('SELECT user_fname,user_lname,user_email,user_phone,user_ig,user_faculty,status,user_language,user_gender,user_relationship FROM user WHERE user_email=?',(email,))
    a = c.fetchall()
    conn.close()
    return a

def retrieve_unit_of_user(email):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    c= conn.cursor()
    c.execute('SELECT unit_id FROM enrolment WHERE user_email=?',(email,))
    a = c.fetchall()
    res=[]
    for i in a:
        res.append(i[0])
    conn.close()
    return res


def retrieve_movie_of_user(email):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    c= conn.cursor()
    c.execute('SELECT genre FROM movie WHERE user_email=?',(email,))
    a = c.fetchall()
    res=[]
    for i in a:
        res.append(i[0])
    conn.close()
    return res


def retrieve_music_of_user(email):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    c= conn.cursor()
    c.execute('SELECT genre FROM music WHERE user_email=?',(email,))
    a = c.fetchall()
    res=[]
    for i in a:
        res.append(i[0])
    conn.close()
    return res
    

def update_status(email,new_stat):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    conn.execute('UPDATE user SET status=? WHERE user_email=?',(new_stat,email))
    conn.commit()
    conn.close()

def update_gender(email,new_gender):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    conn.execute('UPDATE user SET user_gender=? WHERE user_email=?',(new_gender,email))
    conn.commit()
    conn.close()

def update_relationship(email,new_relationship):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    conn.execute('UPDATE user SET user_relationship=? WHERE user_email=?',(new_relationship,email))
    conn.commit()
    conn.close()

def update_language(email,new_language):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    conn.execute('UPDATE user SET user_language=? WHERE user_email=?',(new_language,email))
    conn.commit()
    conn.close()

def insert_unit(email,unit):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    units=unit.strip().lower().split(",")
    for i in units:
        conn.execute('INSERT into enrolment(user_email,unit_id) VALUES (?,?)',(email,i))
        conn.commit()
    conn.close()

def get_units(email):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    c = conn.cursor()
    c.execute('SELECT unit_id FROM enrolment WHERE user_email==?',(email,))
    data = c.fetchall()
    return data

def insert_movie(email,genre):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    for i in genre:
        conn.execute('INSERT into movie(user_email,genre) VALUES (?,?)',(email,i))
        conn.commit()
    conn.close()

def insert_music(email,genre):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    for i in genre:
        conn.execute('INSERT into music(user_email,genre) VALUES (?,?)',(email,i))
        conn.commit()
    conn.close()

def data_based_on_unit(unitname,email):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    c = conn.cursor()
    c.execute('SELECT user_fname,user_lname,user_phone,user_ig,user_faculty,user_gender,user_relationship,status FROM user INNER JOIN enrolment on user.user_email=enrolment.user_email WHERE unit_id=? and user.user_email!=?',(unitname,email))
    a=c.fetchall()
    conn.close()
    return a

def data_based_on_movie_interest(movie_genre,email):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    c = conn.cursor()
    c.execute('SELECT user_fname,user_lname,user_phone,user_ig,user_faculty,user_gender,user_relationship,status FROM user INNER JOIN movie ON user.user_email=movie.user_email WHERE genre=? AND user.user_email!=?',(movie_genre,email))
    a=c.fetchall()
    conn.close()
    return a

def data_based_on_music_interest(music_genre,email):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    c = conn.cursor()
    c.execute('SELECT user_fname,user_lname,user_phone,user_ig,user_faculty,user_gender,user_relationship,status FROM user INNER JOIN music ON user.user_email=music.user_email WHERE genre=? AND user.user_email!=?',(music_genre,email))
    a=c.fetchall()
    conn.close()
    return a

def data_based_on_name(name):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    c = conn.cursor()
    c.execute('SELECT user_fname,user_lname,user_phone,user_ig,user_faculty,user_gender,user_relationship,status FROM user WHERE user_fname LIKE ? OR user_lname LIKE ? ',
    ('{}%'.format(name),'{}%'.format(name)))
    a=c.fetchall()
    conn.close()
    return a

def session_based_on_unit(unit):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    c = conn.cursor()
    c.execute('SELECT * FROM study_session WHERE lower(unit) LIKE ?',('{}%'.format(unit),))
    a=c.fetchall()
    conn.close()
    return a

def session_based_on_name(name):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    c = conn.cursor()
    c.execute('SELECT * FROM study_session WHERE lower(session_name) LIKE ? or lower(session_description) LIKE ?',('%{}%'.format(name),'%{}%'.format(name),))
    a=c.fetchall()
    conn.close()
    return a

def data_for_explore(email):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    c = conn.cursor()
    c.execute('SELECT user_fname,user_lname,user_phone,user_ig,user_faculty,user_gender,user_relationship,status FROM user WHERE user_email!=?',(email,))
    a = c.fetchall()
    conn.close()
    return a

def initialize_to_do_list(user_email):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    conn.execute('INSERT INTO todo(user_email,task1,task2,task3,task4,task5) VALUES(?,?,?,?,?,?)',(user_email,None,None,None,None,None))
    conn.commit()
    conn.close()

def update_to_do_list(user_email,lst):
    task1= safe_get_list(0,lst)
    task2= safe_get_list(1,lst)
    task3= safe_get_list(2,lst)
    task4= safe_get_list(3,lst)
    task5= safe_get_list(4,lst)
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    conn.execute('UPDATE todo SET task1=?,task2=?,task3=?,task4=?,task5=? WHERE user_email=? ',(task1,task2,task3,task4,task5,user_email))
    conn.commit()
    conn.close()

def get_all_emails():
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    c = conn.cursor()
    c.execute('SELECT user_email FROM user')
    a = c.fetchall()
    conn.close()
    res=[]
    for i in a:
        res.append(i[0])
    conn.close()
    return res

def get_user_to_do(email):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    c = conn.cursor()
    c.execute('SELECT task1,task2,task3,task4,task5 FROM todo WHERE user_email=?',(email,))
    a = c.fetchall()
    conn.close()
    res=a[0]
    conn.close()
    return res

def get_to_do_check(email):
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    c = conn.cursor()
    c.execute('SELECT c1,c2,c3,c4,c5 FROM todo WHERE user_email=?',(email,))
    a = c.fetchall()
    conn.close()
    res=a[0]
    conn.close()
    return res

def update_to_do_check(email,lst):
    check1= "on" if "c1" in lst else ""
    check2= "on" if "c2" in lst else ""
    check3= "on" if "c3" in lst else ""
    check4= "on" if "c4" in lst else ""
    check5= "on" if "c5" in lst else ""
    conn = sqlite3.connect('database_new/database.db',check_same_thread=False)
    conn.execute('UPDATE todo SET c1=?,c2=?,c3=?,c4=?,c5=? WHERE user_email=? ',(check1,check2,check3,check4,check5,email))
    conn.commit()
    conn.close()