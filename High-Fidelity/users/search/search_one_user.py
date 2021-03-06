import requests

# we use this code to find a particular user in our database
users_url = "https://api-career-dev-quizz.herokuapp.com/users"

# this is for the request that we send


def check_status_code(res):
    if res.status_code == 200:
        print(res.text)
        return res.text
    else:
        print("Sorry, the user you're looking for was not found")


# here we get the  user's details to look for in our database
def get_the_user():
    email = input("What is the email of the user you are looking for?")

    r = requests.get(url=users_url + "/" + email)
    check_status_code(r)
