from Question import Question


class MultipleChoiceQuestion(Question):
    def __init__(self, id, question_type, question_text, options, correct_option, is_active=True):
        super().__init__(id, question_type, question_text, options, is_active)
        self.correct_option = correct_option
        self.options = options
#question_type, question_text, options, correct_option)
        
    def get_correct_option(self):
        return self.correct_option

    def update_statistics(self, is_correct):
        super().update_statistics(is_correct)
        # Доп действия для MultipleChoiceQuestion

 
 
    def as_dict(self):
        # TODO apdate id
        return  {'id': 1,#присваиваем порядковый номер в общем списке в файле, начиная с первого, 
                    'question_type': self.get_question_type(), 
                    'question_text': self.get_question_text(),
                    'options': self.options,
                    'correct_option': self.correct_option,
                    'is_active': self.get_is_active()
                    }
    