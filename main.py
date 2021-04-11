from users.signup.sign_up import sign_up
from login.login_module import login
from users.user_class import User
from users.student_class import Student
from users.administrator_class import Administrator
from questions.database.get_all_questions import get_all_questions
from users.search.search_one_user import get_the_user
import requests
import json

print("=" * 100)
print("Welcome to the ALU Career Readiness App\nWe are excited to be part of your journey as you further your career!!")
print("=" * 100)


# this is a function to call our main menu
def main_menu():
    print("=" * 100)
    print("Welcome! What would you like to do today?")
    print("Press 1: To Sign Up if you are a new user")
    print("Press 2: To Login if you're an existing user")
    print("Press 3: Exit")


while True:
    main_menu()
    choice = input("What number do you choose?").lower()
    if choice == "1" or choice == "one":
        sign_up()
    elif choice == "2" or choice == "two":
        login()
        option = input("What number do you choose?").lower()
        if option == "1" or choice == "one":
            get_all_questions()
        elif option == "2" or choice == "two":
            print("Your score is: ")
        elif option == "4" or choice == "four":
            dict1 = {}
            Administrator.add_question(dict1)
        elif option == "5" or choice == "five":
            dict2 = {}
            Administrator.add_new_administrator(dict2)
        elif option == "6" or choice == "six":
            dict3 = {}
            Administrator.remove_user(dict3)
        elif option == "7" or choice == "seven":
            get_the_user()
        elif option == "8" or choice == "eight" or choice == "3" or choice == "three":
            print("Thank you!")
            break
    elif choice == "3" or choice == "three":
        print("Thank you !")
    ask = input("Would you like to choose again? Choose 'yes' if you would like to and 'no' if not: ").lower()
    if ask == "yes":
        continue
    else:
        print("See you next time")
        break
print("\n")
print("Thanks for checking in and working on your career readiness!")
print("=" * 100)
