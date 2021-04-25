import requests
import json

def remove_user(user):

    url = "https://api-career-dev-quizz.herokuapp.com/users"
    # url = "http://localhost:3000/users"
    
    """
    remove_user
    ===========
    return -1 when failed.
    """

    if user is None:
        return -1
    else:

        request = requests.delete(url = url, data=user)

        if request.status_code == 200:
            print("removed a new user")
        else:
            print("didn't remove the user")
            return -1
