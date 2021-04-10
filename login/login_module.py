import requests
import json
from users.user_class import User
from users.administrator_class import Administrator
from users.student_class import Student


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
        if user["userClassification"] == "student":
            return Student(**user)
        else:
            return Administrator(**user)
    elif request.status_code == 500:
        return 0
    else:
        return -1
