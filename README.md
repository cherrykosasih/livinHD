# LivinHD

## Team 15: Ciwiks-Ciwiks
1. Cherry
2. Jessica
3. Lionie
4. Monica

## Background
In the past two years, online learning has been a culture for students all around the world, introducing new ways to study and interactions. As students, we’ve found several day-to-day problems during online learning we believe others have encountered as well.

## Problems
### Two main problems we are going to address are:
#### 1. Scheduling
Scheduling is an inevitable part of our lives. About 70% of adults make use of a digital calendar to schedule their activities. As a student, we often find it difficult to keep track of our schedules, especially in this online era where interactions are limited and done on multiple platforms. Forgetting to attend a schedule is also a common issue, due to many reasons such as lack of efficient reminders and confusing timetable.
#### 2. Social interaction
In an online learning situation, finding a group of friends is pretty difficult, this applies to both casual social interaction and situations in finding teammates for group projects.
 
Having automation can be beneficial for different aspects of learning in the perspective of productivity and social life. Our app, Livin HD, is built to help students automate and tackle these issues.

## Solutions 
Features implemented and brief explaination
 
[Log in and sign in page, profile, and questionnaire]
Students will create an account and fill out data to complete their profile account, this will be followed by a set of questions to determine student’s interest, which will be stored in the database and utilized to connect students with common interest.

After signing in, we have a main home page to handle scheduling.
[Home page]
- Scheduling
Timetable: calendar is integrated into a student's timetable, students can manually schedule task into the timetable
Reminder: built in reminder inside app to notify student to next schedule to encourage engagement and attendance 
To do list: personal to do list for student

[Find friend/study session page]
- Social interaction
Find a friend and study session: dedicated page to connect students.
Allow students to search and find new friends to socialize by using our previous customised questions to filter people with similar interests. 
Aside from finding friends, we can join or arrange a study session according to units or preferences. 


## Future Implementation
### 1. Server deployment and saving database in server
Currently, our web application product is not deployed yet and our database is still stored locally. We hope to expand by deploying a server to save databases and enable multiple users to connect with one another.
### 2. Integrate API
To ease communication between users without heavily depending on third party applications outside of web application, we would like to integrate API, specifically Zoom API in find session page and Whatsapp API in find friends page. We would also like to add Google Calendar API to automatically sync schedule in user's google calendar.

## Youtube
### Round 1: https://youtu.be/ZifimOcPcsQ 
### Round 2: https://youtu.be/sxWLLEDvG2M

## How to run in terminal
- pip3 install virtualenv
- virtualenv flask
- cd flask
- source bin/activate
- pip3 install flask
- python3 main.py

## Our website
You can find our web app here
Link: http://172.105.126.97:5000/
