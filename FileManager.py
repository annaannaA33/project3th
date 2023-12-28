from question import Question
import json
import datetime
from MultipleChoiceQuestion import MultipleChoiceQuestion
from FreeFormQuestion import FreeFormQuestion
from typing import Union


class FileManager:
    def __init__(self):

        self.USER_DATA_FILE = 'user_data.json'


# question_text - тут должна быть вся инфа по каждому вопросу 
    #сохраняем все в фаил в формате json
    def save_free_form_question(self, file_path='questions.json', new_question_list):
        data = {'id': id #присваиваем порядковый номер в общем списке в файле, начиная с первого, 
                 'question_type': q.get_question_type(), 
                 'question_text': new_question_list[question_text],
                 'correct_option': new_question_list[correct_option],
                 'options': options[] 
                 'is_active': q.is_active
                 } 

#сохраняем все в фаил в формате json
        
    def save_multiple_choice_question(self, file_path='questions.json'):
        data = [{'id': id # присваиваем порядковый номер в общем списке в файле, начиная с первого, 
                 'question_type': new_question_list[question_type], 
                 'question_text': new_question_list[question_text],
                 'correct_option': new_question_list[correct_option], 
                 'is_active': q.is_active - по умолчанию активен,}] 
    

    def save_questions_to_json(self,new_question_list):
        #проходимся по всему спискувопросов из new_question_list полученного из Learning_tool и для каждого спрашиваем тип вопроса и сохраняем
        for q in new_question_list:
            with open('questions.json', 'w') as file:
                json.dump(new_question_list, file)
    #получаем из списка вопросов сохраненных количество вопросов и порядковые номера, присваиваем айди каждому новому вопросу согласно порядковому номеру
        if question_type == multiple_choice_question_type:
            save_multiple_choice_question(self, file_path='questions.json')
        elif question_type == free_form_question_type:
            save_free_form_question(self, file_path='questions.json')
# если во сохранилось передаем сохранено удачно
        return True
    

'''
question_id = len(self.questions)
        question.id = question_id


    def save_questions(self, file_path='questions.json'):
        data = [{'id': q.id, 'question_type': q.get_question_type(), 'question_text': q.get_question_text(),
                 'answer': q.get_answer(), 'is_active': q.is_active, 'practice_count': q.practice_count,
                 'test_count': q.test_count, 'correct_count': q.correct_count,
                 'total_correct_percentage': q.total_correct_percentage, 'total_questions': q.total_questions}
                for q in self.question_manager.questions]
        with open(file_path, 'w') as file:
            json.dump(data, file)
'''
    def create_question_from_data(self, data: dict) -> Union[FreeFormQuestion, MultipleChoiceQuestion]:
        if data['question_type'] == 'free_form':
            return FreeFormQuestion(data['question_text'], data['answer'], data['is_active'])
        elif data['question_type'] == 'multiple_choice':
            return MultipleChoiceQuestion(data['question_text'], data['answer_options'], data['correct_option'], data['is_active'])
        else:
            raise ValueError(f"Unsupported question type: {data['question_type']}")


    def load_questions(self, file_path='questions.json'):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            questions = [self.create_question_from_data(q) for q in data]
            return questions
        except FileNotFoundError:
            return []

    
    def save_statistics(self, question_id, score, file_path='result.txt'):
        # Method to save test scores to a text file
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(file_path, 'a') as file:
            file.write(f"{timestamp} - Question ID: {question_id}, Score: {score}%\n")

    def load_statistics(self, file_path='results.txt'):
        # Method to load test scores from a text file
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def save_user_data(self, player):
        data = {'name': player.name}
        with open(self.USER_DATA_FILE, 'w') as file:
            json.dump(data, file)

    def load_user_data(self):
        try:
            with open(self.USER_DATA_FILE, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            return {}
        

    def add_question(self, question):
        self.questions.append(question)
        question_id = len(self.questions)
        question.id = question_id
        self.file_manager_instance.save_questions([question.get_data_for_save() for question in self.questions])