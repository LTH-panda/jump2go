from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import *
from .forms import *

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')
    content = {'question_list': question_list}
    return render(request,'ask/index.html', content)

def questDetail(request, quest_id):
    # question = Question.objects.get(id = quest_id)
    question = get_object_or_404(Question, pk=quest_id) # 페이지 존재하지않으면 404 오류 발생
    content = {'question': question}
    return render(request, 'ask/question_detail.html', content)

def questCreate(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('ask:index')
    else:
        form = QuestionForm()
    content = {'form': form}
    return render(request, 'ask/question_create.html', content)

def answerCreate(request, quest_id):
    question_id = quest_id
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('ask:questDetail', question_id=question_id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    # content = request.POST['answer_content']
    # answer = Answer(question=question, content=content)
    # answer.save()
    return render(request, 'ask/question_detail.html', context)