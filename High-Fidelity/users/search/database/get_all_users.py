import requests
import json

def get_all_users():

    """
    get_all_users
    =============
    return a list of all users.
    return -1 when failed.
    """

    url = "https://api-career-dev-quizz.herokuapp.com/users"
    


    request = requests.get(url = url)

    if request.status_code == 200:
        return json.loads(request.text)
    else:
        return -1
