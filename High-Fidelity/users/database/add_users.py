import requests
import json

def add_new_user(user):

    """
    add_new_user
    =============
    return -1 when failed.
    """

    url = "https://api-career-dev-quizz.herokuapp.com/users"
    

    if user is None:
        return -1
    else:
        request = requests.post(url = url, data=user)

        if request.status_code == 200:
            print("added new user")
        else:
            print(" did not add a new user ")
            return -1
