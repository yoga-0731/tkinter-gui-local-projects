from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {quiz.score}", font=('Arial', 15, 'bold'), fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Hello", fill='black', font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_image = PhotoImage(file='images/true.png')
        self.right = Button(image=right_image, highlightthickness=0, command=self.check_answer_1)
        self.right.grid(row=2, column=0)
        wrong_image = PhotoImage(file='images/false.png')
        self.wrong = Button(image=wrong_image, highlightthickness=0, command=self.check_answer_2)
        self.wrong.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text=f"""You've reached the end of the game!\n
                                                    Your score is {self.quiz.score}/{len(self.quiz.question_list)}""")
            self.right.config(state='disabled')
            self.wrong.config(state='disabled')

    def check_answer_1(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_answer_2(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct):
        if is_correct:
            color = 'green'
            self.quiz.score += 1
        else:
            color = 'red'

        self.canvas.config(bg=color, highlightthickness=0)
        self.window.after(1000, self.get_next_question)
