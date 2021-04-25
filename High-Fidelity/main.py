import sys
from users.signup.sign_up import sign_up
from login.login_module import login
from questions.questions_answers import Quiz
from users.search.search_one_user import get_the_user


# this is a function to call our main menu
def main_menu():
    print("=" * 100)
    print("Welcome! What would you like to do today?")
    print("Press 1: To Sign Up if you are a new user")
    print("Press 2: To Login if you're an existing user")
    print("Press 3: Exit")

# we create a student menu that is displayed after logging in
def student_menu():
    print("=" * 100)
    print("Welcome! What would you like to do today?")
    print("Press 1: To Play our new Resume Prep Quiz")
    print("Press 2: To See your Score")
    print("Press 3: Logout")

# we create an administrator menu that is displayed after logging in


def admin_menu():
    print("=" * 100)
    print("Welcome! What would you like to do today?")
    print("Press 1: To Add a new Question")
    print("Press 2: To Add a new Administrator")
    print("Press 3: To Remove a User")
    print("Press 4: To Search for a particular user to see their progress")
    print("Press 5: To rank students by scores")
    print("Press 6: Logout")

print("=" * 100)
print("Welcome to the ALU Career Readiness App\nWe are excited to be part of your journey as you further your career!!")
print("=" * 100)


main_menu()
choice = input("What number do you choose?").lower()
if choice == "1" or choice == "one":
    user = sign_up()
elif choice == "2" or choice == "two":
    user = login()
else:
    sys.exit()

while (user != None):
    if user.userClassification == "student" or user.userClassification == "Student":
        student_menu()
        option = input("What number do you choose?").lower()
        if option == "1" or option == "one":
            newQuiz = Quiz()
            newQuiz.root.mainloop()
            user.update_student_score(newQuiz.score)
            user.save_student_data({"score" : user.score})
        elif option == "2" or option == "two":
            print("Your score is: {}".format(user.score))
        else: 
            break
    else:
        admin_menu()
        option = input("What number do you choose?").lower()
        if option == "1" or option == "one":
            user.add_question()
        elif option == "2" or option == "two":
            user.add_new_administrator()
        elif option == "3" or option == "three":
            user.remove_user()
        elif option == "4" or option == "four":
            get_the_user()
        elif option == "5" or option == "five":
            from users.sort.sortingandranking import *
        else:
            print("Thank you!")
            break


main_menu()
print("\n")
print("Thanks for checking in and working on your career readiness!")
print("=" * 100)
