from tkinter import E
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from school.models import *
from teacher.models import *
from student.models import *
import random, requests, json
from django.contrib.auth.decorators import login_required

from .forms import QuestionsForm, AnswerForm
# Create your views here.

@login_required(login_url='/school/school-login')
def add_quiz(request):
    # check if the school/teacher is logged in or not
    if request.user.groups.filter(name='school').exists() or request.user.groups.filter(name='Teachers').exists():
        if request.user.groups.filter(name='school').exists():
            school = request.user.schooluserprofile
            schoolNavHeader = True
            classrooms = Classroom.objects.filter(school_id=school)
        else:
            school = request.user.teacherprofile.school
            teacher = request.user.teacherprofile
            schoolNavHeader = False
            classrooms = teacher.classroom.all()

        try:
            if request.method == 'POST':
                print('tt')
                classroom = request.POST['classroom']
                subject = request.POST['subject']
                teacher = request.POST['teacher']
                quiz_schedule = request.POST['quiz_schedule']
                title = request.POST['title']
                time_limit = request.POST['time_limit']

                hasError = False
                if not Classroom.objects.filter(id=int(classroom)).exists():
                    hasError = True
                if not subjects.objects.filter(id=int(subject)).exists():
                    hasError = True
                if not teacher_profile.objects.filter(id=int(teacher)).exists():
                    hasError = True
                if int(teacher)<1 :
                    hasError = True           

                if hasError != False:
                    return redirect('/quiz/add?msg=form-invalid') 
                else:
                    new_quiz = quiz.objects.create(
                        classroom = Classroom.objects.get(id=int(classroom)),
                        subject = subjects.objects.get(id=int(subject)),
                        teacher = teacher_profile.objects.get(id=int(teacher)),
                        quiz_schedule = quiz_schedule,
                        title = title,
                        time_limit = time_limit,
                    )
                    new_quiz.save()
                    quiz_id = new_quiz.quiz_id
                    return redirect(f"/quiz/search-ques/?quiz_id={quiz_id}&msg=Quiz-added")
            context = {
                'classrooms' : classrooms,
                'teachers' : teacher_profile.objects.filter(school=school),
                'schoolNavHeader' : schoolNavHeader,
                'subjects' : subjects.objects.all() if schoolNavHeader else teacher.subject
            }       
            return render(request, 'quiz/add-quiz.html', context)
        except:#
            return redirect('/quiz/add')     
    return redirect('/')    

def valid_quiz_uid(quiz_id):
    if quiz.objects.filter(quiz_id=quiz_id).exists():
        return True
    else:
        return False    

# normal search ques page
@login_required(login_url='/school/school-login')
def search_ques(request):
    if request.user.groups.filter(name='school').exists() or request.user.groups.filter(name='Teachers').exists():
        if request.user.groups.filter(name='school').exists():
            school = request.user.schooluserprofile
            schoolNavHeader = True
        else:
            school = request.user.teacherprofile.school
            schoolNavHeader = False

        if not 'quiz_id' in request.GET:
            return redirect('/quiz/add/?msg=no-uid')   

        if not valid_quiz_uid(str(request.GET['quiz_id'])):
            return redirect('/quiz/add/?msg=uid-not-found')       

        quiz_id = str(request.GET['quiz_id'])

        new_quiz = quiz.objects.get(quiz_id=quiz_id)

        context = {
            'quiz' : new_quiz,
            'quiz_id' : quiz_id,
            'schoolNavHeader' : schoolNavHeader,
            'questions' : Question.objects.all(),
        }       
        return render(request, 'quiz/search-ques.html', context)
    return redirect('/')   
    


def select_question_api(request):
    try:
        question_objs = list(Question.objects.all())
        if 'qs' in request.GET:
            question_objs = list(Question.objects.filter(question__icontains = request.GET['qs']))
        data = []
        random.shuffle(question_objs)
        for question_obj in question_objs:
            data.append({
                "category" : question_obj.level.category_name,
                "question" : question_obj.question,
                "marks" : question_obj.marks,
                "answers" : question_obj.get_answers(),
                'question_id' : question_obj.uid,
            })
        
        payload = {'status' : True, 'data' : data}
        
        return JsonResponse(payload)
    
    except Exception as e:
        print(e)
    return HttpResponse("Something went wrong.")

@login_required(login_url='/')
def quiz_list(request):

    if request.user.groups.filter(name='school').exists():
        school = School.objects.get(user=request.user)
        schoolNavHeader =  True
        isStudent = False
        quizs  = quiz.objects.filter(classroom__school_id= school)  
    elif request.user.groups.filter(name='Teachers').exists():
        school = request.user.teacherprofile.school
        schoolNavHeader = isStudent = False
        quizs  = quiz.objects.filter(classroom__school_id= school)  
    else:
        schoolNavHeader = False
        isStudent = True
        quizs  = quiz.objects.filter(classroom= request.user.studentprofile.classroom)  

    

    context = {
        'quizs' : quizs,
        'schoolNavHeader' : schoolNavHeader,
        'isStudent' : isStudent
    }       
    return render(request, 'quiz/quiz-list.html', context)  



def select_quiz_profile_api(request):
    if request.user.groups.filter(name='school').exists() or request.user.groups.filter(name='Teachers').exists():
        if request.user.groups.filter(name='school').exists():
            school = request.user.schooluserprofile
            schoolNavHeader = True
        else:
            school = request.user.teacherprofile.school
            schoolNavHeader = False

        if not 'quiz_id' in request.GET:
            return redirect('/quiz/add/?msg=no-uid')   

        if not valid_quiz_uid(str(request.GET['quiz_id'])):
            return redirect('/quiz/add/?msg=uid-not-found')       


        quiz_id = str(request.GET['quiz_id'])
        pro_quiz = quiz.objects.get(quiz_id=quiz_id)

        context = {
            'quiz' : pro_quiz,
            'quiz_id' : quiz_id,
            'schoolNavHeader' : schoolNavHeader,
        }       
        return render(request, 'quiz/quiz-profile.html', context)   


             
        return redirect('/quiz/list?msg=add-success') ###
    return redirect('/')   


@login_required(login_url='/school/school-login')
def add_quiz_question_api(request):
    try:
        question_objs = list(Question.objects.all())
        if 'quiz_uid' in request.GET and 'question_uid' in request.GET:
            if not valid_quiz_uid(str(request.GET['quiz_uid'])):
                return redirect('/quiz/add/')
            if not Question.objects.filter(uid=str(request.GET['question_uid'])):
                return redirect('/quiz/add/')      
        else:
            return redirect('/quiz/add/')   

        add_quiz =  quiz.objects.get(quiz_id=str(request.GET['quiz_uid']))    
        new_question = Question.objects.get(uid=str(request.GET['question_uid']))

        add_quiz.question_list.add(new_question)
        add_quiz.save()

        payload = {'status' : True, 'data' : 'Added'}
        return JsonResponse(payload)
    
    except Exception as e:
        print(e)
    return HttpResponse("Something went wrong.")

@login_required(login_url='/school/school-login')
def del_quiz_question_api(request):
    try:

        if 'quiz_uid' in request.GET and 'question_uid' in request.GET:
            if not valid_quiz_uid(str(request.GET['quiz_uid'])):
                return redirect('/quiz/add/')
            if not Question.objects.filter(uid=str(request.GET['question_uid'])):
                return redirect('/quiz/add/')      
        else:
            return redirect('/quiz/add/')   

        del_quiz =  quiz.objects.get(quiz_id=str(request.GET['quiz_uid']))    
        del_question = Question.objects.get(uid=str(request.GET['question_uid']))

        del_quiz.question_list.remove(del_question)

        payload = {'status' : True, 'data' : 'Deleted'}
        return JsonResponse(payload)
    
    except Exception as e:
        print(e)
    return HttpResponse("Something went wrong.")


@login_required(login_url='/school/school-login')
def get_quiz_questions_api(request):
    try:
        if 'quiz_uid' in request.GET:
            if not valid_quiz_uid(str(request.GET['quiz_uid'])):
                return redirect('/quiz/add/')  
        else:
            return redirect('/quiz/add/')   

        the_quiz =  quiz.objects.get(quiz_id=str(request.GET['quiz_uid']))

        qi_li = the_quiz.question_list.all()

        data = []
        for question_obj in qi_li:
            data.append({
                "question" : question_obj.question,
                'question_id' : question_obj.uid,
            })
        payload = {'status' : True, 'data' : data}
        return JsonResponse(payload)
    
    except:
        return HttpResponse("Something went wrong.")

def add_ques(request):
    quesForm = QuestionsForm()
    ansForm = AnswerForm()
    if request.user.groups.filter(name='school').exists():
        schoolNavHeader =  True
    else:
        schoolNavHeader = False
    if request.method == "POST":
        quesForm = QuestionsForm(request.POST)
        ansForm = AnswerForm(request.POST)
        if quesForm.is_valid() and ansForm.is_valid():
            quesForm.save()
            ansForm.save()
    context = {'quesForm': quesForm, 'schoolNavHeader':schoolNavHeader, 'ansForm': ansForm}
    return render(request, 'quiz/add_ques.html', context)


def ques_list(request):
    if request.user.groups.filter(name='school').exists():
        schoolNavHeader =  True
    else:
        schoolNavHeader = isStudent = False
    context = {
        'questions' : Question.objects.all(),
        'schoolNavHeader':schoolNavHeader
    }
    return render(request, 'quiz/ques_list.html', context)


@login_required(login_url='/student/login')
def attempt_quiz(request, quiz_id):
    if quiz.objects.filter(quiz_id=quiz_id).exists():
        if request.user.studentprofile.classroom == quiz.objects.get(quiz_id=quiz_id).classroom :
            the_quiz = quiz.objects.get(quiz_id=quiz_id)
            context = {
                'quiz' : the_quiz,
                'no_of_questions' : the_quiz.count_total(),
            }
            return render(request, 'quiz/attempt_quiz.html', context)
        return redirect('/quiz/list/')
    return redirect('/quiz/list/')


@login_required(login_url='/student/login')
def attempt_quiz_questions_api(request):
    try:
        if 'quiz_uid' in request.GET:
            if not valid_quiz_uid(str(request.GET['quiz_uid'])):
                return redirect('/student')  
        else:
            return redirect('/student')   

        the_quiz =  quiz.objects.get(quiz_id=str(request.GET['quiz_uid']))

        # qi_li = random.shuffle(list(the_quiz.question_list.all()))
        qi_li = the_quiz.question_list.all()

        data = []
        for question_obj in qi_li:
            data.append({
                "question" : question_obj.question,
                'question_id' : question_obj.uid,
                'answers' : question_obj.quiz_answer()
            })
        payload = {
            'status' : True, 
            'quiz_id' : str(request.GET['quiz_uid']),
            'data' : data
        }
        return JsonResponse(payload)
    
    except Exception as err:
        print(err)
        return HttpResponse("Something went wrong q.")   

@login_required(login_url='/student/login')
def attempt_quiz_answer(request):
    if request.method == 'POST':
        try: #
            quiz_id = request.POST['quiz_id']
            question_id = request.POST['question_id']
            answer_id = request.POST['answer_id']

            if quiz_id == request.GET['quiz_id'] and quiz.objects.filter(quiz_id=quiz_id, classroom=request.user.studentprofile.classroom).exists() and Answer.objects.filter(uid=answer_id).exists() and Question.objects.filter(uid=question_id).exists():
                atm_quiz = quiz.objects.get(quiz_id=quiz_id, classroom=request.user.studentprofile.classroom)
                atm_answer = Answer.objects.get(uid=answer_id)
                atm_question = Question.objects.get(uid=question_id)

                eval_true = 0

                if atm_quiz.question_list.filter(uid=question_id).exists() and atm_answer.question == atm_question:
                    if quiz_response.objects.filter(quiz=atm_quiz, student=request.user.studentprofile, question=atm_question).exists():
                        quiz_response.objects.get(quiz=atm_quiz, student=request.user.studentprofile, question=atm_question).delete()
                    if atm_answer == Answer.objects.get(is_correct=True, question=atm_question):
                        eval_true = 1
                    add_attempt_quiz_response = quiz_response.objects.create(
                        quiz = atm_quiz,
                        student = request.user.studentprofile,
                        question = atm_question,
                        student_answer = atm_answer,
                        evaluate = eval_true,
                        correct_key = Answer.objects.get(is_correct=True, question=atm_question),
                        quiz_name = atm_quiz.title,
                        subject = atm_quiz.subject,
                        topic = atm_question.topic,
                        teacher_name = atm_quiz.teacher,
                        answer_text = atm_answer.answer,
                        correct_answer_text = Answer.objects.get(question=atm_question, is_correct=True),
                        question_text = atm_question.question,
                        question_tags = atm_question.tags,
                    )
                    return JsonResponse(json.dumps({
                        "status_code" : 200,
                        "answer_added" : True,
                        "msg" : "success"
                    }), safe=False)   
        except Exception as err:
            print(err)
            pass    
    return JsonResponse(json.dumps({
        "status_code" : 422,
        "msg" : "failed"
    }), safe=False)        


@login_required(login_url='/')
def evaluate_quiz_master(request):
    if request.method == 'POST':
        try: #
            quiz_id = request.POST['quiz_id']
            total_marks = 0
            if quiz_id == request.GET['quiz_id'] and quiz.objects.filter(quiz_id=quiz_id, classroom=request.user.studentprofile.classroom).exists():
                atm_quiz = quiz.objects.get(quiz_id=quiz_id, classroom=request.user.studentprofile.classroom)

                get_all_responses = quiz_response.objects.filter(quiz=atm_quiz, student=request.user.studentprofile)

                for res in get_all_responses:
                    if res.correct_key == res.student_answer:
                        total_marks = total_marks + int(res.question.marks)
                quiz_master_evalute = quiz_master.objects.create(
                        quiz_uid = atm_quiz.quiz_id,
                        quiz_data = atm_quiz,
                        quiz_type = atm_quiz.quiz_type,
                        quiz_num = 3,
                        quiz_name = atm_quiz.title,
                        school_id = atm_quiz.classroom.school_id,
                        school_name = atm_quiz.classroom.school_id.name,
                        subject = atm_quiz.subject,
                        quiz_class = atm_quiz.classroom.standard,
                        quiz_topic = atm_quiz,
                        student_name = request.user.studentprofile.full_name,
                        teacher = atm_quiz.teacher,
                        teacher_name =atm_quiz.teacher.full_name ,
                        student = request.user.studentprofile,
                        marks = total_marks,
                        attempted_question = get_all_responses.count(),
                )

                return JsonResponse(json.dumps({
                    'student_id' : request.user.studentprofile.id,
                    'user_id' : request.user.id,
                    'student_name' : request.user.studentprofile.full_name,
                    'quiz_title' : atm_quiz.title,
                    'marks' : total_marks
                }), safe=False)
        except Exception as err:
            print(err)    
    return JsonResponse(json.dumps({
        "status_code" : 422,
        "msg" : "failed"
    }), safe=False)        


# MASTER QUIZ AFTER SUBMITTING
def getCSV(request):
    with open('quiz_master.csv', 'a') as f:
        master = quiz_master.objects.all()
        f.write(f"Quiz_ID, Quiz_Data, Quiz_Type, Quiz_Num, Quiz_Name, School_ID , School_Name, Subject, Quiz_Class, Quiz_Topic, {x.student_name}, {x.teacher}, {x.teacher_name}, {x.student}, {x.student_name}, {x.marks}, {x.attempted_question}, {x.submited_on} \n")
        for x in master:
            f.write(f"{x.quiz_uid},{x.quiz_data}, {x.quiz_type}, {x.quiz_num}, {x.quiz_name}, {x.school_id} , {x.school_name}, {x.subject}, {x.quiz_class}, {x.quiz_topic}, {x.student_name}, {x.teacher}, {x.teacher_name}, {x.student}, {x.student_name}, {x.marks}, {x.attempted_question}, {x.submited_on} \n")
    return HttpResponse("Hey you :))")


def getResponseCSV(request):
    with open('quiz_response.csv', 'a') as file:
        res = quiz_response.objects.all()
        i = 1
        for m in res:
            file.write(f"{m.quiz.quiz_id}, {m.quiz.title}, {m.student}, {i}, {m.question}, {m.student_answer},{m.evaluate},{m.correct_key},{m.quiz_name},{m.subject},{m.topic},{m.teacher_name}, {m.answer_text},{m.correct_answer_text}, {m.question_text}, {m.question_tags}  \n")    
            i = i+1

    return HttpResponse("<h1>hello :))</h1>")        



    