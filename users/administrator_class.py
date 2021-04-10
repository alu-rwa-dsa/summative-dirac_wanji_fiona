from users.user_class import User

class Administrator(User):

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)


    # add new questions

    # add new administrator

    # remove administrator

    # remove user

    # do the ranking

    # do the search
