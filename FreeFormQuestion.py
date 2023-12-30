from Question import Question



class FreeFormQuestion(Question):
    def __init__(self, question_type, question_text, expected_answer, is_active=True):
        super().__init__('free_form',  question_type, question_text, is_active)
        self.expected_answer = expected_answer

    def update_statistics(self, is_correct):
        super().update_statistics(is_correct)


    def as_dict(self):
        # TODO apdate id
        return  {'id': 1,#присваиваем порядковый номер в общем списке в файле, начиная с первого, 
                 'question_type': self.get_question_type(), 
                 'question_text': self.get_question_text(),
                 'expected_answer': self.expected_answer,
                 'is_active': self.get_is_active()
                 }\n
     
    
        
    
