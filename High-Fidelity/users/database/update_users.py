import requests

def update_users(user_email, data):

    """
    update_users
    =============
    return -1 when failed.
    """

    url = "https://api-career-dev-quizz.herokuapp.com/users/" + user_email 
    # url = "http://localhost:3000/users/" + user_email

    if data is None:
        return -1
    else:
        request = requests.put(url = url, data=data)

        if request.status_code == 200:
            print(f"updated the user {user_email}")
        else:
            print(request.text)
            return -1

