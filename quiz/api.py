
from django.http import JsonResponse
from .models import *
import  json
from django.db.models import Sum
# Create your views here.




def get_desc_graph(request, quiz_id):
    if quiz.objects.filter(quiz_id=quiz_id).exists():

        the_quiz = quiz.objects.get(quiz_id=quiz_id)
        data = []
        qno = 1

        # code here

        return JsonResponse(json.dumps({
            'status' : True,
            'quiz_id' : quiz_id,
            'quiz_name' : the_quiz.title,
            'data' : data
        }), safe=False)   
    return JsonResponse(json.dumps({
        'status' : False,
        'msg' : 'Quiz not found'
    }), safe=False)


def get_level_graph(request, quiz_id):
    if quiz.objects.filter(quiz_id=quiz_id).exists():

        the_quiz = quiz.objects.get(quiz_id=quiz_id)
        data = []
        # code here
        
        for x in Category.objects.all():
            res = quiz_response.objects.filter(quiz=the_quiz, level=x)
            data.append(
                {
                    'catagory' : x.category_name,
                    'performence' : res.aggregate(Sum('evaluate'))['evaluate__sum'],
                    'attempted' : res.count(),
                }
            )

        return JsonResponse(json.dumps({
            'status' : True,
            'quiz_id' : quiz_id,
            'quiz_name' : the_quiz.title,
            'data' : data
        }), safe=False)   
    return JsonResponse(json.dumps({
        'status' : False,
        'msg' : 'Quiz not found'
    }), safe=False)

def latest_quiz_graph(request, quiz_id):
    if quiz.objects.filter(quiz_id=quiz_id).exists():

        the_quiz = quiz.objects.get(quiz_id=quiz_id)
        data = []
        qno = 1
        for x in the_quiz.question_list.all():
            res = quiz_response.objects.filter(quiz=the_quiz, question=x) #.aggregate(Sum('evaluate'))['evaluate__sum']
            data.append(
                {
                    'question_no' : 'Q' + str(qno),
                    'performence' : res.aggregate(Sum('evaluate'))['evaluate__sum'],
                    'attempted' : res.count(),
                }
            )
            qno = qno + 1

        return JsonResponse(json.dumps({
            'status' : True,
            'quiz_id' : quiz_id,
            'quiz_name' : the_quiz.title,
            'data' : data
        }), safe=False)   
    return JsonResponse(json.dumps({
        'status' : False,
        'msg' : 'Quiz not found'
    }), safe=False)      

    