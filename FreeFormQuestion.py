from question import Question



class FreeFormQuestion(Question):
    def __init__(self, question_text, expected_answer, expected_answer, is_active=True):
        super().__init__('free_form', question_text, is_active)
        self.expected_answer = expected_answer

    def update_statistics(self, is_correct):
        super().update_statistics(is_correct)
