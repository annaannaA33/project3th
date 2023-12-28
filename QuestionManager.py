from random import shuffle
from FreeFormQuestion import FreeFormQuestion
from MultipleChoiceQuestion import MultipleChoiceQuestion
from PracticeMode import PracticeMode
from FileManager import FileManager
from Learning_tool import main_manu


    def add_question_menu(self):
        question_to_be_added = []

        def create_free_form_question(self, question_type, question_text):
            #cпрашиваем question_text, expected_answer и если все заполнено, тогда все сохраняем в список  question_to_be_added    
            expected_answer = input("Enter the answer: ")

            new_question = FreeFormQuestion(question_type, question_text, expected_answer)
            
            #question_to_be_added.append(new_question(question_type, question_text, expected_answer))
            return new_question
    
        def craete_multiple_choice_question(self):   
            #cпрашиваем сколько ответов, варианты ответов, праильный вариант ответа и если все заполнено, все сохраняем в список  question_to_be_added 
            num_options = int(input("Enter the number of answer options: "))
            options = [input(f"Enter option {i + 1}: ") for i in range(num_options)]
            correct_option = input("Enter the correct option: ")
            new_question = MultipleChoiceQuestion(question_type, question_text, options, correct_option, options)
            return new_question

        new_question = None

        while True:
            question_type = input("Enter the question type (1 for FreeFormQuestion, 2 for MultipleChoiceQuestion): ")
            if question_type == '1' or question_type == '2':
                question_text = input("Enter the question text: ")
                if not question_text or len(question_text) > 5:
                    print("Please, Enter the question")
                else:    
                    if question_type == '1':
                        question_type = free_form_question_type
                        new_question = create_free_form_question(question_type, question_text)
                        # когда вопрос сохранили выходим цикла, но не из функциию. пользователю опять предлагается ввести вопров, пока он не нажмет выход
                    elif question_type == '2':
                        question_type = multiple_choice_question_type
                        new_question = craete_multiple_choice_question(question_type, question_text)    
                        # когда вопрос сохранили выходим цикла, но не из функциию. пользователю опять предлагается ввести вопров, пока он не нажмет выход
                    question_to_be_added.append(new_question)
            elif question_type == "main_manu":
                if len(question_to_be_added) > 0:
                # если был добавлен в question_to_be_added хоть один вопрос, то возвращаем question_to_be_added[]    
                    return question_to_be_added
            else:
                print("Invalid question type.")

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