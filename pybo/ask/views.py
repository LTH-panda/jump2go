from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')
    content = {'question_list': question_list}
    return render(request,'ask/index.html', content)

def questDetail(request, quest_id):
    # question = Question.objects.get(id = quest_id)
    question = get_object
    content = {'question':question}
    return render(request, 'ask/question_detail.html', content)