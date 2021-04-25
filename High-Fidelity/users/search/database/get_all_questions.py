import requests
import json

<<<<<<< HEAD
def get_all_questions():

    questions = "https://api-career-dev-quizz.herokuapp.com/questions"
    # url = "http://localhost:3000/questions"
    
=======

def get_all_questions():
    questions = "https://api-career-dev-quizz.herokuapp.com/questions"
    # url = "http://localhost:3000/questions"

>>>>>>> aebacdb4e6cfd820547281f4c0ca1171f74d2356
    """
    get all questions
    =================
    return a list of all questions when succesed.
    return -1 when failed.
    """

<<<<<<< HEAD
    request = requests.get(url = questions)
=======
    request = requests.get(url=questions)
>>>>>>> aebacdb4e6cfd820547281f4c0ca1171f74d2356

    if request.status_code == 200:
        return json.loads(request.text)
    else:
        return -1
