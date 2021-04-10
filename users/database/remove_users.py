import requests
import json


def remove_users(lst_users):

    url = "https://api-career-dev-quizz.herokuapp.com/users"
    
    """
    remove_users
    =================
    return -1 when failed.
    """

    if lst_users is None:
        return -1
    elif type(lst_users) is not "list":
        raise TypeError
    else:
        for user in lst_users:

            request = requests.delete(url = url, data=user)

            if request.status_code == 200:
                print("removed a new user")
            else:
                return -1
