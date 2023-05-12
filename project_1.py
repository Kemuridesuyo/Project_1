import tkinter as tk
from tkinter import messagebox


class StudentGrades:
    def __init__(self):
        self.scores_list = []

    def get_grade(self, score: int, best: int) -> str:
        if score >= best - 10:
            return 'A'
        elif score >= best - 20:
            return 'B'
        elif score >= best - 30:
            return 'C'
        elif score >= best - 40:
            return 'D'
        else:
            return 'F'

    def process_scores(self, n: int, scores_input: str) -> str:
        try:
            scores_list = [int(score) for score in scores_input.split()]

            if len(scores_list) > n:
                scores_list = scores_list[:n]

            best = max(scores_list)

            result = ""
            for i, score in enumerate(scores_list):
                grade = self.get_grade(score, best)
                result += f"Student {i+1} score is {score} and grade is {grade}\n"

            return result

        except Exception as e:
            return f"Error: {e}"


def submit():
    try:
        n = int(number_entry.get())
        scores_input = scores_entry.get()
        grades = student_grades.process_scores(n, scores_input)
        messagebox.showinfo("Result", grades)
    except ValueError:
        messagebox.showerror("Error", "Please input valid values.")


student_grades = StudentGrades()

app = tk.Tk()
app.title("Student Grades")

number_label = tk.Label(app, text="Total number of students:")
number_label.pack()
number_entry = tk.Entry(app)
number_entry.pack()

scores_label = tk.Label(app, text="Enter scores (separated by space):")
scores_label.pack()
scores_entry = tk.Entry(app)
scores_entry.pack()

submit_button = tk.Button(app, text="Submit", command=submit)
submit_button.pack()

app.mainloop()
