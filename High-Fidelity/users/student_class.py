from users.user_class import User
from users.database import update_users

class Student(User):
    """
    student class
    =============
    Student(id, name, email, password, faculty, promotion, **alldetails)
    **alldetails: use to recreate a user when details comes from the database.
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def update_student_score(self, new_score):
        if self is not None:
            self.score += int(new_score)
        else:
            raise TypeError(f"score {new_score} must be an integer")

    # level

    def save_student_data(self, data={}):
        if self is not None:
            update_users.update_users(self.email, data)
