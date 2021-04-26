# ALU Career Readiness App

* [Project Title](#project-title)
* [Team Members](#team-members)
* [Data Structures and Algorithms Used](#data-structures-and-algorithms-used)
* [Project Description](#project-description)
* [Motivation behind the Project](#motivation)
* [Bibliography/References](#bibliography)
* [Presentation Slides + Video Demo](#presentation)


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

#### Time complexity: O(1) - the login function takes only one user’s information at a time
#### Space complexity: O(1) - because the information is picked one at a time specifically for the login and it isn't stored afterwards, because it's already in the database


### 3. The Sign Up function

![signup-image](https://user-images.githubusercontent.com/70945471/116002679-28834d00-a5fb-11eb-960a-4330f2ca2b94.png)

![signup-image](https://user-images.githubusercontent.com/70945471/116002687-3042f180-a5fb-11eb-8cbd-dfc5c3c5cef3.png)

![signup-image](https://user-images.githubusercontent.com/70945471/116002698-3afd8680-a5fb-11eb-8f4b-12a02512b9e9.png)

The signup function comes in two forms: one for students and one for admin, and it basically asks for the users information and password, then stores it in the database. The user classification specifies whether the user is a student or an administrator.This piece of code is pretty straightforward, but to ensure we can catch any potential error, we added a if else statement to check the status codes, so we can catch any error, for example, if a user tries to sign up with an email that's already being used. We can see the correctness because our code ensures no user has the same email.

#### Time complexity: O(1) - one user is signed up at a time
#### Space complexity: O(1) - user info is only stored for a short while before its sent to the database

### 3. The Add New Question function

![add-new-question](https://user-images.githubusercontent.com/70945471/116002760-86179980-a5fb-11eb-8e7d-ddd2152eef75.png)

The add_new_question() function takes in a question/ questions, which are stored in a list that is passed into the function. The function then loops through the list and adds each question to the database. This code is correct because of the conditions put in place to check that the questions are added correctly. The code first checks whether the list item is empty or not, and then checks if it is a list item, before proceeding. This ensures that when the list item is looped through, it is a non-empty list. In addition, there is also an inner if else statement that checks for the status code to ensure that the questions are successfully added to the database.

#### Time complexity: O(n) - depending on how many questions are in the list item and have to be looped through

#### Space complexity: O(1) - this is because only one list item is stored with all the questions before they’re sent to the database

### 4. The Binary Search for the Users

![binary-search](https://user-images.githubusercontent.com/70945471/116002796-a8111c00-a5fb-11eb-9d54-56477a62ea14.png)

This function looks for users in the database using the binary search algorithm. This algorithm splits the list in two and searches the portion that the search term is most likely to be in. As it is a recursion formula, we have an initial if statement to ensure that the code only works if the high point of the array is higher than the low point. Moreover, it keeps changing the midpoint as we move to different sections of the split array to ensure we keep dividing the portions in half. With these conditions, the correctness is implemented.

#### Time complexity: O(log n) - this is dependent on how many times the list is split before the search item is found
#### Space complexity: O(n) - this is because the list of users has to be stored as it is being searched.

### 3. The Quick Sorting Scores function

![quick-sort](https://user-images.githubusercontent.com/70945471/116002835-cbd46200-a5fb-11eb-9e15-6a279305affb.png)

![quick-sort](https://user-images.githubusercontent.com/70945471/116002844-d0991600-a5fb-11eb-8b8a-099570fd6d4b.png)

![quick-sort](https://user-images.githubusercontent.com/70945471/116002887-fd4d2d80-a5fb-11eb-9113-67490c175adb.png)

Our quick sort function arranges the user scores in ascending and then returns the sorted list. 
To check the correctness, we first look at the initial if condition that makes sure that our function, which is a recursive function, stops when the array it is trying to divide contains no element. Next, we look at the if and elif conditions in the for loop. They all use the same pivot index because our quicksort method uses the first element in every list as the pivot point. This is useful as we can keep track of our pivot element at every iteration and every list (low, high and same).

We also print out the sorted list at the end to check for ourselves whether the quicksort function worked.

#### Time complexity: O(log n) - this is because the array is constantly being divided until all the arrays are sorted and can be put together to give the complete sorted list

#### Space complexity: O(n) - this is because we have to store the scores as we sort them

### 6. The Ranking function

![ranking](https://user-images.githubusercontent.com/70945471/116002887-fd4d2d80-a5fb-11eb-9113-67490c175adb.png)

In our ranking function, we use the sorted list from the quick sort function, reverse it and then use the indexes to rank the student’s scores. Firstly, to ensure that the ranking is correct, we reverse the list, so that the highest scores are at the start of the list, which ensures that our rank formula (rank = item_index + 1) gives the correct rank. We set up the rank formula like this because list indexing starts from 0, so after reversing, the highest score would be at position 0, and because rank starts at 1, we add one to the index. Furthermore, we also use an if condition that checks whether the score we’re looking for is in the sorted list, and only proceeds if it is in the list and otherwise, it gives an error. Resultantly, we know that the function is correct, because of all the conditions we’ve put in place.

#### Time complexity: O(1) - this is because the function simply prints a specific element from a given index, so it isn’t a complex or lengthy procedure

#### Space complexity: O(n) - this is because all the scores have to be stored because we ask the user to input their score so we can get their rank


## Solution 
Our solution’s aim was to make career development an easier process for students to go through as well as commit to. We developed the ALU Career Readiness Application for this specific purpose. The app has different categories of resume preparation, interview preparation, and professional skills development. Login is either as an administrator to monitor students’ progress or add new questions or remove a user, if one logs in as a student, one can play different quiz questions and see how they rank across the players who have played the game.

The purpose of this is to help university students have an easier time in their career development journey, being students ourselves, we understand how time-consuming university studies can be and we designed the game to be a fun, fast way, students can pop in and out of the app when they have time to do so.

## VIDEO

[![video-presentation](https://drive.google.com/file/d/1XVPPtR8Aug6aVjf1LMrZ4sSo-8PHGJJC/view?usp=sharing)](https://drive.google.com/file/d/1XVPPtR8Aug6aVjf1LMrZ4sSo-8PHGJJC/view?usp=sharing)

[link](https://drive.google.com/file/d/1XVPPtR8Aug6aVjf1LMrZ4sSo-8PHGJJC/view?usp=sharing)


## Bibliography

+ Review of the Language Learning App "Duolingo" – Specialist Language Courses (2016). Available at: https://specialistlanguagecourses.com/review-language-learning-app-duolingo/  (Accessed: 7 April 2021).


## Presentation

Slides Presentation :https://docs.google.com/presentation/d/1OqthQqHElSMhpjWW-6GFTQHb6COdHySAEFW8-ib6iMU/edit?usp=sharing
Video Link: 
  
