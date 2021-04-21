import requests
import json
from users.user_class import User
from users.administrator_class import Administrator
from users.student_class import Student


def sign_up():
    """ 
    sign_up
    =======
    sign_up(*details)
    *details is all information passed by the user.  
    """
    # to distinguish the students and administrators
    role = int(input("What role do you play at ALU\nAre you:\n1. A student\n2. An administrator.\nPlease pick a "
                     "number '1 or 2': "))

    # we get the user details dependent on their roles
    # sign up for students
    if role == 1:
        print("Please provide accurate information, any falsified details will lead to suspension from using the app")
        firstName = input("What is your First Name? ")
        lastName = input("What is your Last Name? ")
        email = input("What is your ALU email? ")
        password = input("What will your password be to access our App?")
        userClassification = "student"
        rank = "None"
        numberOfQuestionsAnswered = 0
        score = 0
        dict = {"firstName": firstName, "lastName": lastName, "email": email, "password": password,
                "userClassification": userClassification, "rank":rank, "numberOfQuestionsAnswered":
                numberOfQuestionsAnswered, "score": score}
        url = "https://api-career-dev-quizz.herokuapp.com/users"

        request = requests.post(url=url, data=dict)

        if request.status_code == 200:
            print("Created a new user.")
        elif request.status_code == 400:
            print("Sorry, the user already exists.")
        else:
            return -1

    # sign up for administrators
    elif role == 2:
        print("Please provide accurate information, any falsified details will lead to suspension from using the app")
        firstName = input("What is your First Name? ")
        lastName = input("What is your Last Name? ")
        email = input("What is your ALU email? ")
        password = input("What will your password be to access our App?")
        userClassification = "administrator"
        dict = {"firstName": firstName, "lastName": lastName, "email": email, "password": password,
                "userClassification": userClassification}
        url = "https://api-career-dev-quizz.herokuapp.com/users"

        request = requests.post(url=url, data=dict)

        if request.status_code == 200:
            print("Created a new user.")
        elif request.status_code == 400:
            print("Sorry, the user already exists.")
        else:
            return -1
    else:
        return -1



