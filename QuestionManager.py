from random import shuffle
from FreeFormQuestion import FreeFormQuestion
from MultipleChoiceQuestion import MultipleChoiceQuestion
from PracticeMode import PracticeMode
from FileManager import FileManager
from Learning_tool import main_manu


class QuestionManager:
    def __init__(self):
        self.questions = []

    
    def add_question_menu(self):

        while True:
            question_type = input("Enter the question type (1 for FreeFormQuestion, 2 for MultipleChoiceQuestion): ")
            if question_type == '1' or '2':
                
                question_text = input("Enter the question text: ")

                if not question_text or len(question_text) > 5:
                    print("Invalid question type.")
                
                
                    if question_type == '1':
                        expected_answer = input("Enter the answer: ")
                        self.question = FreeFormQuestion(question_text, expected_answer)

                    elif question_type == '2':
                        question_answer = {}
                        num_options = int(input("Enter the number of answer options: "))
                        options = [input(f"Enter option {i + 1}: ") for i in range(num_options)]
                        correct_option = input("Enter the correct option: ")
                        self.question = MultipleChoiceQuestion(question_text, options, correct_option)
                else:
                    print("Please, Enter the question")

            elif question_type == "main_manu":
                main_manu()
            else:
                print("Invalid question type.")
    
 
                   

    def add_question(self, question):
        self.questions.append(question)
        question_id = len(self.questions)
        question.id = question_id
       # self.file_manager_instance.save_questions(self.questions)

'''

    def view_statistics(self):
        for question in self.questions:
            print(f"ID: {question.id}, Type: {question.get_question_type()}, "
                  f"Text: {question.get_question_text()}, Active: {question.is_active()}, "
                  f"Practice Count: {question.practice_count}, Test Count: {question.test_count}, "
                  f"Correct Percentage: {question.total_correct_percentage}%")

    def toggle_question_menu(self):
        question_id = int(input("Enter the ID of the question to toggle: "))
        disable = input("Enter 'disable' to deactivate or 'enable' to activate the question: ").lower() == 'disable'
        self.disable_enable_question(question_id, disable)

    def disable_enable_question(self, question_id, disable=True):
        for question in self.questions:
            if question.id == question_id:
                question.is_active = not disable
                self.file_manager_instance.save_questions(self.questions)
                break
'''
    
'''
    def test_mode(self, num_questions):
        active_questions = [q for q in self.questions if q.is_active]
        if len(active_questions) < num_questions:
            print("Not enough active questions for the test.")
            return 

        selected_questions = shuffle(active_questions)[:num_questions]

        correct_answers = 0
        for question in selected_questions:
            user_answer = input(f"Test Mode - {question.get_question_text()}: ")
            is_correct = self.check_answer(question, user_answer)
            question.test_count += 1
            question.update_statistics(is_correct)

            if is_correct:
                correct_answers += 1

        score = (correct_answers / num_questions) * 100
        print(f"Test completed. Score: {score}%")
        self.file_manager.save_statistics(selected_questions[0].id, score)

    def check_answer(self, question, user_answer):
        if isinstance(question, MultipleChoiceQuestion):
            try:
                user_answer_index = int(user_answer) - 1
                return user_answer_index == question.get_correct_option()
            except ValueError:
                return False
        else:
            return user_answer.lower() == question.get_answer().lower()

    '''