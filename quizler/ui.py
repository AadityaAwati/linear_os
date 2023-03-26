from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
class QuizInterface:
      def __init__(self, quiz_brain: QuizBrain):
          self.score = 0
          self.quiz = quiz_brain
          self.window = Tk()
          self.window.title("Quizler")
          self.window.config(background=THEME_COLOR, pady=20, padx=20)

          self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
          self.score_label.grid(row=0, column=3)

          self.canvas = Canvas(width=350, height=300, bg="white")
          self.question_text = self.canvas.create_text(150,
                                                       125,
                                                       width=280,
                                                       text="Question Text",
                                                       font=("Arial", 20, "italic"),
                                                       fill=THEME_COLOR)
          self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

          right_image = PhotoImage(file="images/true.png")
          right_buttton = Button(image=right_image, command=self.true_pressed)
          right_buttton.grid(row=2, column=0)

          wrong_image = PhotoImage(file="images/false.png")
          wrong_buttton = Button(image=wrong_image, command=self.false_pressed)
          wrong_buttton.grid(row=2, column=1)

          self.get_next_question()

          self.window.mainloop()

      def get_next_question(self):
          if not self.quiz.still_has_questions():
              self.canvas.itemconfig(self.question_text, text="You've reached the end.")
              return "the end"
          q_text = self.quiz.next_question()
          self.canvas.itemconfig(self.question_text, text=q_text)

      def true_pressed(self):
          self.give_feedback(self.quiz.check_answer("True"))
          self.score_label.config(text=f"Score: {self.score}")

      def false_pressed(self):
          self.give_feedback(self.quiz.check_answer("False"))
          self.score_label.config(text=f"Score: {self.score}")

      def give_feedback(self, answer):
          def change_bg_to_white():
              self.canvas.config(bg="white")
          if answer:
              self.score += 1
              self.canvas.config(bg="green")
              self.window.after(1000, change_bg_to_white)
          else:
              self.canvas.config(bg="red")
              self.window.after(1000, change_bg_to_white)

          self.window.after(1000, self.get_next_question)
