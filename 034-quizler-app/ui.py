THEME_COLOR = "#272e4b"

from tkinter import *
from quiz_brain import QuizBrain
import math


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR, padx=50, pady=50)

        self.canvas = Canvas(width=600, height=420)
        self.question_text = self.canvas.create_text(
            300,
            225,
            text="Love",
            font=('Varela Round', 34, 'normal'),
            fill=THEME_COLOR,
            width=500
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(
            text=f"Score: {0}",
            font=('Arial', 30, 'italic'),
            fg="white",
            bg=THEME_COLOR
        )
        self.score_label.grid(row=0, column=1)

        self.true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.is_true)
        self.true_button.grid(row=2, column=1)

        self.false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.is_false)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text="Congrats. You've reached the end of this quiz."
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def is_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, check_correctness):
        if check_correctness:
            self.canvas.config(bg="#00b29a")
        else:
            self.canvas.config(bg="#fc8a7a")
        self.window.after(1000, self.get_next_question)
