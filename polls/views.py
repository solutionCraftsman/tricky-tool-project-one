from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Choice
# from decouple import config

# Create your views here.


def index(request):
    questions = Question.objects.all()
    # print(questions)
    context = {
        'questions': questions
    }
    return render(request, 'polls/index.html', context)


# def environment(request):
#     return HttpResponse(config())
