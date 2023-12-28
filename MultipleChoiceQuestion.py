from question import Question


class MultipleChoiceQuestion(Question):
    def __init__(self, question_text, answer_options, correct_option, is_active=True):
        super().__init__('multiple_choice', question_text, answer_options, is_active)
        self.correct_option = correct_option
#question_type, question_text, options, correct_option)
        
    def get_correct_option(self):
        return self.correct_option

    def update_statistics(self, is_correct):
        super().update_statistics(is_correct)
        # Доп действия для MultipleChoiceQuestion
