import requests
import json

def get_all_questions():

    questions = "https://api-career-dev-quizz.herokuapp.com/questions"
    # url = "http://localhost:3000/questions"
    
    """
    get all questions
    =================
    return a list of all questions when succesed.
    return -1 when failed.
    """

    request = requests.get(url = questions)

    if request.status_code == 200:
        return json.loads(request.text)
    else:
        return -1
