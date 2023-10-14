import tkinter as tk

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.current_question = 0
        self.score = 0

        # Define questions and answers (you can customize this)
        self.questions = [
            {
                'question': "What is the capital of France?",
                'options': ["London", "Madrid", "Paris", "Berlin"],
                'correct_answer': "Paris"
            },
            {
                'question': "Which planet is known as the Red Planet?",
                'options': ["Venus", "Mars", "Jupiter", "Saturn"],
                'correct_answer': "Mars"
            },
            {
                'question': "What is 2 + 2?",
                'options': ["3", "4", "5", "6"],
                'correct_answer': "4"
            },
        ]

        self.label = tk.Label(root, text="")
        self.label.pack(pady=10)
        self.show_question()

    def show_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.label.config(text=question_data['question'])
            
            self.buttons = []
            for option in question_data['options']:
                button = tk.Button(self.root, text=option, command=lambda option=option: self.check_answer(option, question_data['correct_answer']))
                self.buttons.append(button)

            for button in self.buttons:
                button.pack(fill="both", padx=10, pady=5)

        else:
            self.show_result()

    def check_answer(self, selected_option, correct_answer):
        if selected_option == correct_answer:
            self.score += 1
        self.current_question += 1
        for button in self.buttons:
            button.pack_forget()
        self.show_question()

    def show_result(self):
        self.label.config(text=f"You scored {self.score} out of {len(self.questions)}!")
        self.current_question = 0
        self.score = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
