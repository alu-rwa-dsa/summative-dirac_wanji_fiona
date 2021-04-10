import requests
import json


def add_new_users(lst_users):
    """
    add_new_users
    =============
    return -1 when failed.
    """

    url = "https://api-career-dev-quizz.herokuapp.com/users"

    if lst_users is None:
        return -1
    elif type(lst_users) is not "list":
        raise TypeError
    else:
        for user in lst_users:

            request = requests.post(url=url, data=user)

            if request.status_code == 200:
                print("added new user")
            else:
                return -1
