import requests
import json

def add_new_questions(lst_questions):

    questions = "https://api-career-dev-quizz.herokuapp.com/questions"
    
    """
    get all questions
    =================
    return a list of all questions when succesed.
    return -1 when failed.
    """
    if lst_questions is None:
        pass
    elif type(lst_questions) is not "list":
        raise TypeError("argument must be a list")
    else:
        for question in lst_questions:
            request = requests.post(url = questions, data=question)

            if request.status_code == 200:
                print("added a new element successfuly")
            else:
                return -1
