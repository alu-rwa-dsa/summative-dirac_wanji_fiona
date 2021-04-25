import requests
import json

def add_new_question(question):

    url_questions = "https://api-career-dev-quizz.herokuapp.com/questions"
    
    """
    get all questions
    =================
    return a list of all questions when succesed.
    return -1 when failed.
    """
    if question is None:
        pass
    else:
        request = requests.post(url = url_questions, data=question)

        if request.status_code == 200:
            print("added a new element successfuly")
        else:
            print("did not add a new question")
            return -1
