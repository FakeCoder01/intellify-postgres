import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import datetime

def just_the_temp(request):
    return render(request, 'just_the_temp.html')


def contact_form(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST.get('msg')
        add_on = datetime.datetime.now()

        try:
            with open('contact_from.txt', 'a') as f:
                f.write(f"NAME : {name} - EMAIL :  {email} - ADD ON : {add_on} \nSUBJECT: {subject} \nMESSAGE :  {msg} \n\n\n")
            return HttpResponse('<span class="text-success">Your message has been sent. Thank you!</span>')
        except:
            return HttpResponse('<span class="text-danger">Something went wrong</span>')
    else:
        return HttpResponse('<span class="text-danger">Something went wrong</span>')       