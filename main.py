from users.user_class import User
from users.student_class import Student
from users.administrator_class import Administrator
from questions.database import get_all_questions
from login.login_module import *
from users.search import *

# I was testing this one. You can 
new_user = login("d.murairi@alustudent.com", "iamdirac")
if new_user == -1:
    print("user not found")
elif new_user == 0:
    print("wrong password")
#else:
    # print(new_user.__dict__)
    # new_user.save_student_data({"score" : 0})
    # new_user.find_questions_by_level(1)

    
