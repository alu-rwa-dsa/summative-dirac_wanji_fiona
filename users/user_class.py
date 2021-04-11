from users.search.database import get_all_questions
from users.search import search_one_user


class User:
    """
    Class User
    """

    def __init__(self, *args, **kwargs):

        if kwargs:
            """ recreate user when data comes from the cloud"""
            for key, value in kwargs.items():
                setattr(self, key, value)

    def find_questions_by_level(self, level=1):
        questions = get_all_questions.get_all_questions()
        if questions == -1:
            return []
        else:
            # print(questions)
            # return binary_search.binary_search(questions, level, )
            pass
