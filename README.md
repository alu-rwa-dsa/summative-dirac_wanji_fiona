# ALU Career Readiness App

* [Project Title](#project-title)
* [Team Members](#team-members)
* [Data Structures and Algorithms Used](#data-structures-and-algorithms-used)
* [Project Description](#project-description)
* [Motivation behind the Project](#motivation)
* [Bibliography/References](#bibliography)


## Project Title

ALU Career Readiness App

## Team Members

  + Wanjiru Wang'ondu
  + Dirac Murairi
  + Fiona Ng'ang'a
## Data Structures and Algorithms used

 - Binary search - we’re using this to enable a search feature in our app for different users and questions later on with the finished app.
 - Quick sort - we’re using this to rank users according to their scores

## Project Description

Our project is a quiz application, similar to duolingo and quizlet in that user's answer questions on different topics. In our case, all our topics are career development related as it is a project inspired by our own career development experiences and journeys.

The application has these features: 
  + A sign up and login feature: this is for users to sign up and be able to have their progress and scores tracked
  + A database: this stores the user's scores and details
  + A ranking and sorting system: this is to help administrators (like career development personnel and interns) check different users progress and scores, in order to see   how well their doing and whether they need any help. They can also use this to determine what score corresponds to what career readiness stamp
  + A basic GUI for users to interact with when they answer questions, which displays the questions and gives their score for the particular quiz they are doing 

The application has different question sets, with different topics and content. As career development content is generally the same for different years, we decided to make all the types of content available for all students, so the questions and students are not divided into years.

This gives career development the freedom to assign different sections each semester for different years or assign all years the same content, whatever they feel would be the most beneficial for the students. This application would not replace career development content, but it would work together with the content, in order to make it as easy and understandable for students, as well as comprehensive and useful. In an article of the benefits of Duolingo, author Jules Kirchner said she ‘would recommend using Duolingo in combination with a teacher-led (language) course’, which is why we are making it clear that career development content would not be replaced, just  integrated.


## Motivation

Our motivation for this application was to make career development content easier to learn and understand. 

A lot of students complain about the amount of career development content and how hard it is to take in all of it. This application was our solution to that; we wanted to present the content in a way that made it easier for students to understand and take it in, especially because of the heavy workload students have from their coursework and other extracurricular activities.

Looking at applications like quizlet and duolingo, we see that they divide content into different, small sections and allow students to study the larger topic section by section. That is what we wanted our application to do for ALU students.

## Correctness of Algorithms and Time/Space complexity Analysis

### 1. The Login function

![login-image](https://user-images.githubusercontent.com/70945471/116002638-ff62bc80-a5fa-11eb-9753-02dc014b1da9.png)

The login function interacts with our student and administration database, as it let’s people login and interact with the application. 

This function works with an if condition, which checks for a status code of 200, which means the request has been received and understood, and if it receives this code, it goes ahead and gets the user information. Then it checks whether the password that was input is the same as the user password and whether the user is actually classified as a student. If the user meets this criteria, then the code directs them to the student menu, where they can do various things, like take quizzes and view their scores. This works in all cases because each user has a specific password, so if it's correct then we are sure the right user is logged in.

If the password is correct, but the user isn’t classified as a student, they’re taken to the admin menu, and this works in all situations, because there are only two classifications: students and admin.

Lastly, the elif and else condition check for other status codes, the elif for code 500, which is a generic error code and the else for any other code, and the numbers they return would let us know there’s an error and we should check it out.



## Bibliography

+ Review of the Language Learning App "Duolingo" – Specialist Language Courses (2016). Available at: https://specialistlanguagecourses.com/review-language-learning-app-duolingo/  (Accessed: 7 April 2021).

  
