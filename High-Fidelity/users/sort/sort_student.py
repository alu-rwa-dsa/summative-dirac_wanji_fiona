import requests

url = "https://api-career-dev-quizz.herokuapp.com/users/"

response = requests.get(url)
data = response.json()

dict_data = data[0]  # this gives us just the dictionary stored in the list structure from the db
print(dict_data)


# def get_score():
