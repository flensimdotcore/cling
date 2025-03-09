import yaml
import random
import os

script_prefix = os.path.dirname(os.path.abspath(__file__))
banks_prefix = f'{script_prefix}/../res/banks/'
categories_prefix = f'{script_prefix}/../res/categories/'

class Trainer:
    def __init__(self, banks, difficulties, language, subbanks, categories):
        self.subbanks = subbanks
        self.categories = categories
        self.difficulties = difficulties
        self.language = language
        self.banks = self.load_banks(banks)
        self.questions = self.load_questions()
        self.correct_answers = 0
        self.total_questions = 0

    def load_banks(self, user_banks):
        banks = []
        print(self.categories)
        if self.categories not in ['none']:
            for category in self.categories:
                try:
                    with open(f'{categories_prefix}{category}.yaml', 'r', encoding='utf-8') as file:
                        data = yaml.safe_load(file)
                        banks.extend([bank['name'] for bank in data.get('banks', [])])
                except FileNotFoundError:
                    print(f"Category {category} not found")
                except yaml.YAMLError as e:
                    print(f"Error {e} in {category}.yaml file")
        else:
            banks = user_banks

        return banks

    def load_questions(self):
        questions = []
        for bank in self.banks:
            try:
                with open(f"{banks_prefix}{bank}.yaml", "r", encoding="utf-8") as file:
                    data = yaml.load(file, Loader=yaml.SafeLoader)
                    questions.extend(data['questions'])
            except FileNotFoundError:
                print(f"Bank {bank} not found")
            except yaml.YAMLError as e:
                print(f"Error {e} in {bank}.yaml file")

        filtered_questions = [
            q for q in questions if q.get("subbank") in self.subbanks and q.get("difficulty") in self.difficulties
        ]

        return filtered_questions

    def ask_question(self):
        question = random.choice(self.questions)

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
