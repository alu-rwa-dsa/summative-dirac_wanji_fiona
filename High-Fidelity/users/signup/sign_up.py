import requests
import sys
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

    role = 1

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
            return Student(**dict)
        elif request.status_code == 400:
            print("Sorry, the user already exists.")
        else:
            return -1
    else:
        print(">>> Error")
        sys.exit()



