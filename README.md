# R<sup>5</sup> ASSIST

This repository includes the website team **Constant Variables** is making for the ***[CODECAMP HACKATHON](https://codecamphackathon.netlify.app/) by SRM Institute of Science and Technology.***<br>

## Project’s Overview<br>
### Theme-Name : Education<br>
### Application-Type : Website<br>
**Tech Stack**: HTML | CSS | Bootstrap4 | MaterializeCSS | Javascript | Python | SQlite3 | Flask
### Idea-Description
Since the advent of digital platforms for learning, and their tremendous use due to the current scenario, the students are getting bombarded with a lot of data, making it difficult for them to understand, digest, reproduce the content and even analyze their progress.

To tackle this problem, our project, R<sup>5</sup> Assist is a balance of a classroom-based teaching-learning website and an Analytics based tool beneficial for both students as well as teachers. We propose a comprehensive product website with the following features:<br>
1. Login/SignUp facility for teachers as well as students. A teacher will be able to view any activity that a student in his/her class does.<br> 
2. Summarization of various lecture notes provided by the teachers or even uploaded by the student for his/her reference. <br>
3. Exhaustive revision tests to validate the performance of candidates based on the topics covered to date using the Fibonacci Study and Revision Plan. <br>
4. An interactive dashboard where the students can see their progress and the teacher can view the progress of all the students of the class.<br>

***The significance of 5 R’s in R<sup>***5***</sup> Assist<br>***
* Resource
* Remember
* Reproduce
* Review
* Reflect<br>

Our project proves to be a resource for the students, where teachers can upload assignments, notes, and many more things. It also eases the process of revising and remembering important things for students by summarising the content so that students can easily revise what’s most important. Our practice tests help students reproduce what they have already learned. Students can review their performance from our analytics dashboard, not only that our project also helps teachers review their students’ performance, their schedule, and compare results. In the end, after reviewing their performance the students can reflect and improve by taking our periodic review practice tests.

***What is the Fibonacci Study Plan?***<br>
It is a comprehensive study plan based on the Fibonacci Series(0, 1, 1, 2, 3, 5, 8, .....). This series or any similar one can help in increasing the remembrance of a particular topic. In this plan, a portion of the syllabus is revised at regular intervals of times say, first time after 1 day, then on the 2<sup>nd</sup> day, then on the 3<sup>rd</sup>, then on the 5<sup>th</sup>, and so on. After some sessions of revision, it becomes a part of the subconscious memory and is easy to recollect. This can be done for some important facts, formulae, dates, and anything which requires through and continuous revision.

Overall we aim to provide a complete platform where we bridge the gap between the traditional classrooms and the online teaching-learning process.

### Website flow for a teacher<br>

1.  On visiting the landing page the teacher can see the benefits/features that we have to provide to him/her.<br>
2.  Upon clicking the login/SignUp button the user will be directed to the Login and Signup Module, where he/she can register as a teacher if not done already or simply login to his/her profile.<br>
3.  Upon Logging in to the portal, the features teacher will get are as follows:<br>
&nbsp;&nbsp;&nbsp;**3.1. Upload PDF notes**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.1. This tool will be used by the teacher to upload PDF notes to a particular class or a group of students as per his/her discretion<br>
&nbsp;&nbsp;&nbsp;**3.2. Tests**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.2.1. The teacher can set MCQ based tests for the students and send a notification for the students to attempt it.<br>
&nbsp;&nbsp;&nbsp;**3.3. Send Notifications to Students**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.3.1 The teachers can send any notification to students.<br>
&nbsp;&nbsp;&nbsp;**3.4. Comprehensive Dashboard**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.4.1. This comprehensive dashboard will include numerous analyses based on the performance of students of his/her class or even reports of an individual student. He/she can also view the number of classes taught by him/her and their progress.<br>
&nbsp;&nbsp;&nbsp;**3.5. Adding Students to Class**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.5.1. The teacher can add and remove students from his/her class based on her discretion.<br>
&nbsp;&nbsp;&nbsp;**3.6. Profile**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.6.1. He/she would be able to access his/her profile to modify or alter some personal information and view other personal information, view the classes he/she is teaching <br>


### Website flow for a student<br>

1.  On visiting the landing page the student can see the benefits/features that we have to provide to him/her.<br>
2.  Upon clicking the login/SignUp button the user will be directed to the Login and Signup Module, where he/she can register as a student if not done already or simply login to his/her profile.<br>
3.  Upon Logging in to the portal, the features student will get are as follows:<br>
&nbsp;&nbsp;&nbsp;**3.1. Summarizer tool**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.1.1. This tool will help the student to summarize the PDF notes sent by the teacher/uploaded by himself or herself for quick reference.<br>
&nbsp;&nbsp;&nbsp;**3.2. Tests**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.2.1. The student can solve the tests assigned to him by the teacher<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.2.2. The student can also appear for the tests programmatically generated using the summary of the PDFs shared.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.2.3. Our custom made tests based on the combination of the teacher's tests, tests generated via the summary of PDF's with the use of the Fibonacci Study and Revision Technique.<br>
&nbsp;&nbsp;&nbsp;**3.3. Notifications by Teachers**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.3.1 The student can see any notifications sent by the teachers teaching him and respond to them.<br>
&nbsp;&nbsp;&nbsp;**3.4. Comprehensive Dashboard**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.4.1. This comprehensive dashboard will include numerous analyses based on the tests given, marks scored, time taken on various questions, heat-map of activity, etc.<br>
&nbsp;&nbsp;&nbsp;**3.5. Profile**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.5.1. He/she would be able to access his/her profile to modify or alter some personal information and view other personal information<br>

### Modules and Functionalities added

**1. [Login and SignUp Module](/Login%20And%20Signup%20Module)**<br>

**Instructions for usage:** Copy all the 3 files, index.html, style.css, script.js in the same folder, and then open index.html on your browser.<br>
&nbsp;&nbsp;&nbsp;a. [index.html](/Login%20And%20Signup%20Module/index.html)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This file includes the HTML for Login and SignUp module<br>
&nbsp;&nbsp;&nbsp;a. [script.js](/Login%20And%20Signup%20Module/script.js)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This file includes the Javascript for Login and SignUp module<br>
&nbsp;&nbsp;&nbsp;a. [style.css](/Login%20And%20Signup%20Module/style.css)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This file includes the CSS for Login and SignUp module<br>

**Issues:** No potential issue visible till now
<br>
<br>

**2. [UI for Giving Tests](/Giving%20Tests/UI)**<br>

This module will be useful to students for giving tests on the platform<br>

**Instructions for usage:** Copy all the 3 files, index.html, style.css, script.js in the same folder, and then open index.html on your browser.<br>
&nbsp;&nbsp;&nbsp;a. [index.html](/Giving%20Tests/UI/index.html)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This file includes the HTML for Giving Tests module<br>
&nbsp;&nbsp;&nbsp;a. [script.js](/Giving%20Tests/UI/script.js)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This file includes the Javascript for Giving Tests module<br>
&nbsp;&nbsp;&nbsp;a. [style.css](/Giving%20Tests/UI/style.css)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This file includes the CSS for Giving Tests module<br>

**Issues:** Some more comments to be written in CSS and JS, this page is not completely optimized for mobile devices.
<br>
<br>


**3. [UI for Uploading Tests](/Uploading%20Tests/UI)**<br>

This module will be useful for teachers for setting MCQ questions for students.<br>

**Instructions for usage:** Copy index.html to a folder and open it on your browser.<br>
&nbsp;&nbsp;&nbsp;a. [index.html](/Uploading%20Tests/index.html)<br>

**Issues:** Not well commented, some problem with id's for adding options to new questions and UI has to be improved.
<br>
<br>


**4. [Backend Files](/backend%20files)**<br>
&nbsp;&nbsp;&nbsp;4.1. [create_questions.py](/backend%20files/create_questions.py)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1.1. This is the backend for generating questions from the summarized text from the PDFs<br>
&nbsp;&nbsp;&nbsp;4.2. [display_questions.py.py](/backend%20files/display_questions.py)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.2.1. This is the backend for displaying questions from the summarized text from the PDFs and making a connection with the database<br>

**Issues:** No potential issue visible till now
<br>
<br>



### Installing Dependencies for backend

```bash

A) Clone the repository
> git clone https://github.com/rxhxt/R5-Educate-App.git ### Fetch the code

> cd R5-Educate-App/ ### Change to root directory

B) Install Python packages
> python3 -m pip install -r requirements.txt

```
