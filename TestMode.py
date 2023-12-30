from random import shuffle
from MultipleChoiceQuestion import MultipleChoiceQuestion


class TestMode:


    

    def start_test(self, num_questions, questions_list):
        active_questions = [q for q in questions_list if q.is_active]
        if len(active_questions) < num_questions:
            print("Not enough active questions for the test.")
            return 
        '''
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
        self.question_manager.file_manager.save_statistics(selected_questions[0].id, score)

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