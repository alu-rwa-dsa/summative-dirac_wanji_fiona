import requests
import json
from users.user_class import User
from users.administrator_class import Administrator
from users.student_class import Student


# we create a student menu that is displayed after logging in
def student_menu():
    print("=" * 100)
    print("Welcome! What would you like to do today?")
    print("Press 1: To Play our new Resume Prep Quiz")
    print("Press 2: To See your Score")
    print("Press 3: Logout")

# we create an administrator menu that is displayed after logging in


def admin_menu():
    print("=" * 100)
    print("Welcome! What would you like to do today?")
    print("Press 4: To Add a new Question")
    print("Press 5: To Add a new Administrator")
    print("Press 6: To Remove a User")
    print("Press 7: To Search for a particular user to see their progress")
    print("Press 8: Logout")


def login():
    """login"""
    """find user in the database"""
    """create new user class depending on the class"""
    """return users details"""

    url = "https://api-career-dev-quizz.herokuapp.com/login"
    # url = "http://localhost:3000/login"

    email = input("Please type in your email: ")
    password = input("Please type in your password: ")

    request = requests.get(url=url, data={"email": email, "password": password})

    if request.status_code == 200:
        user = json.loads(request.text)
        user.pop("_id", "__v")
        user.pop("__v")
        user["password"] = password
        print(user)
        if user["userClassification"] == "student" or user["userClassification"] == "Student":
            student_menu()
            return Student(**user)
        else:
            admin_menu()
            return Administrator(**user)
    elif request.status_code == 500:
        return 0
    else:
        return -1
