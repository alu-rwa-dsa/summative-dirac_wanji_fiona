from questions.database.get_all_questions import *
from tkinter import *
from tkinter import messagebox as mb
import json

root = Tk()
root.geometry("850x500")
root.title("Quiz")
# with open('quiz.JSON', "r") as f:
#     obj = json.load(f)
# q = (obj['ques'])
# options = (obj['options'])
# a = (obj['ans'])
q = []
options = []
a = []
hints = []
my_questions = get_all_questions()

for question in my_questions:
    hints.append(question["hint"])
    q.append(question["question"])
    options.append(question["options"])
    a.append(question["answer"])


class Quiz:
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn):
        t = Label(root, text="Career Development Prep", width=50, bg="black", fg="white", font=("times", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(root, text=q[qn], width=60, font=("times", 16, "bold"), anchor="w")
        qn.place(x=70, y=100)
        return qn

    def radiobtns(self):
        val = 0
        b = []
        yp = 150
        while val < 2:
            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 40
        return b

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[val]['text'] = op
            val += 1

    def buttons(self):
        nextbutton = Button(root, text="Next", command=self.nextbtn, width=10, bg="green", fg="white",
                            font=("times", 16, "bold"))
        nextbutton.place(x=200, y=380)
        quitbutton = Button(root, text="Quit", command=root.destroy, width=10, bg="red", fg="white",
                            font=("times", 16, "bold"))
        quitbutton.place(x=380, y=380)

    def checkans(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True

    def nextbtn(self):
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(q):
            self.display_result()
        else:
            self.display_options(self.qn)

    def display_result(self):
        score = int(self.correct / len(q) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(q) - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))


quiz = Quiz()
root.mainloop()
