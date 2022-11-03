from datetime import datetime
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from school.models import subjects, Classroom
from student.models import student_profile
from teacher.models import teacher_profile
import uuid
import random

# Create your models here.



class BaseModel(models.Model):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    
    class Meta:
        abstract = True #does not create a model, just uses it as class

class Category(BaseModel):
    category_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.category_name

class Question(BaseModel):
    level = models.ForeignKey(Category, related_name ='level', on_delete= models.CASCADE)
    question = models.CharField(max_length= 500)
    marks = models.IntegerField(default = 1)
    subject = models.ForeignKey(subjects, on_delete=models.CASCADE, blank=True, null=True)
    standard = models.CharField(max_length=50, blank=True, null=True)
    chapter = models.CharField(max_length=200, blank=True, null=True)
    topic = models.CharField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.question

    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question = self))
        random.shuffle(answer_objs)
        data = []

        for answer_obj in answer_objs:
            data.append({
                'answer' : answer_obj.answer,
                'is_correct' : answer_obj.is_correct
            })
        return data

    def quiz_answer(self):
        answer_objs = list(Answer.objects.filter(question = self))
        random.shuffle(answer_objs)
        data = []

        for answer_obj in answer_objs:
            data.append({
                'answer' : answer_obj.answer,
                'answer_id' : answer_obj.uid
            })
        return data    

class Answer(BaseModel):
    question = models.ForeignKey(Question, related_name='question_answer', on_delete= models.CASCADE)
    answer = models.CharField(max_length = 300)
    is_correct = models.BooleanField(default = False)

    def __str__(self):
        return self.answer


 




class quiz(models.Model):
    quiz_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    classroom = models.ForeignKey(Classroom, related_name="quiz_classroom",on_delete=models.CASCADE, blank=True, null=True)
    subject = models.ForeignKey(subjects, on_delete=models.CASCADE, blank=True, null=True)
    question_list = models.ManyToManyField(Question, blank=True, null=True)
    teacher = models.ForeignKey(teacher_profile, on_delete=models.CASCADE, blank=True, null=True)
    quiz_schedule = models.DateTimeField(default=datetime.now())
    time_limit = models.IntegerField(blank=True, null=True) # in minutes
    no_of_questions = models.IntegerField(blank=True, null=True)
    quiz_number = models.IntegerField(blank=True, null=True) # for the particular classroom
    quiz_type = models.CharField(max_length=50, blank=True, null=True)
    allowed_atempts = models.IntegerField(default=1, blank=True, null=True) 
    title = models.CharField(max_length=256)
    student_list = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title       

    def get_questions_of_quiz(self):
        ques_objs = list(self.question_list)
        random.shuffle(ques_objs)
        data = []

        for ques_obj in ques_objs:
            data.append({
                'question_uid' : ques_obj.uid,
                'question_title' : ques_obj.question,
                'question_answers' : ques_obj.get_answers()
            })
        return data    

    def count_total(self):
        self.no_of_questions = self.question_list.count()
        return self.no_of_questions


class quiz_response(models.Model):
    quiz = models.ForeignKey(quiz, related_name="quiz_quizresponse", on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(student_profile, related_name="student_quizresponse", on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey(Question, related_name="question_quizresponse", on_delete=models.CASCADE, null=True, blank=True)
    student_answer = models.ForeignKey(Answer, related_name="answer_quizresponse", on_delete=models.CASCADE, null=True, blank=True)
    evaluate = models.IntegerField(default=0)
    correct_key = models.ForeignKey(Answer, related_name="correct_answer_quizresponse", on_delete=models.CASCADE, null=True, blank=True)



    quiz_name = models.CharField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    topic = models.CharField(max_length=50, null=True, blank=True)
    teacher_name = models.CharField(max_length=50, null=True, blank=True)
    answer_text = models.CharField(max_length=50, null=True, blank=True)
    correct_answer_text = models.CharField(max_length=50, null=True, blank=True)

    question_text = models.CharField(max_length=150, null=True, blank=True)
    question_tags = models.CharField(max_length=150, null=True, blank=True)

    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.student.full_name

class quiz_master(models.Model):
    quiz = models.ForeignKey(quiz, related_name="quiz_quizmaster", on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(student_profile, related_name="student_quizmaster", on_delete=models.CASCADE, null=True, blank=True)
    marks = models.CharField(max_length=5, default='0', null=True, blank=True)
    attempted_question = models.IntegerField(default=0)
    submited_on =  models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.student.full_name