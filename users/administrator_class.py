import sys
import json
import time
import user_class
from database import add_question
from database import add_users
from database import remove_users


class Administrator(user_class.User):

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)



    def add_question(self, dict={}):
        """
        add_question
        ============
        add new question on the db
        """

        myQuestion = {}

        if dict == {} or dict is None:
            hints = input('Enter the hints fot this question: ')
            if hints != "" and hints != " ":
                myQuestion["hint"] = hints.split()
            options = input(' Enter options of the question: ')
            if options != "" and options != " ":
                myQuestion["options"] = options.split()
            myQuestion["question"] = input("Enter the question: ")
            myQuestion["weight"] = 1
            try:
                myQuestion["answer"] = int(input("Which option is the correct answer: "))
            except TypeError:
                print(">>> Please enter a number <<<")
                myQuestion["answer"] = int(input("Which option is the correct answer: "))
            except RuntimeError:
                sys.exit()
    
        else:
            myQuestion = dict

        add_question.add_new_question(myQuestion) 


    def add_new_administrator(self, dict = {}) :
        """
        add_new_administrator
        ====================
        receive a user datat by default
        create a new administrator
        """
        myAdmin = {}
        if dict == {}:
            myAdmin["firstName"] = input("Enter your first name: ")
            myAdmin["lastName"] = input("Enter your last name: ")
            myAdmin["password"] = input("Enter your password: ")
            myAdmin["userClassification"] =  "administrator"
        else:
            myAdmin = dict

        add_users.add_new_user(myAdmin)


    def remove_user(self, dict={}):
        myUser = {}
        if dict == {} or dict is None:
       
            myUser["email"] = str(input("Enter the email addres of the user to delete: "))
            myUser["firstName"] = input("Enter the first name of the user to delete: ")
            myUser["lastName"] = input("Enter the last name of the user to delete: ")
        else:
            myUser = dict
        
        confirmation_password = str(input("Enter your password for confirmation: "))

        if confirmation_password == self.password:
            remove_users.remove_user(myUser)
        else:
            print("Your password is incorrect")

