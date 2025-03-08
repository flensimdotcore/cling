import yaml
import random
import os

script_prefix = os.path.dirname(os.path.abspath(__file__))

class Trainer:
    def __init__(self, bank, difficulty, language):
        self.bank = bank
        self.difficulty = difficulty
        self.language = language
        self.questions = self.load_questions()
        self.correct_answers = 0
        self.total_questions = 0

    def load_questions(self):
        with open(f"{script_prefix}/../banks/{self.bank}.yaml", "r", encoding="utf-8") as file:
            return yaml.load(file, Loader=yaml.SafeLoader)

    def ask_question(self):
        question = random.choice(self.questions["general"])
        if self.language in question['language']:
            question_text = question['language'][self.language]
        else:
            question_text = question['language']['en']
        print(f"Question: {question_text}")

        user_input = input("Enter your command: ").strip()
        if user_input in question["answers"]:
            print("Correct!\n")
            self.correct_answers += 1
        else:
            print(f"Wrong! Correct answers: {', '.join(question['answers'])}\n")

        self.total_questions += 1

    def start_session(self, repeat):
        for _ in range(repeat):
            self.ask_question()
        print(f"Your result: {self.correct_answers}/{self.total_questions} correct answers.")
