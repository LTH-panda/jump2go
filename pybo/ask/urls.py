from django.urls import path
from . import views

app_name = 'ask'     # namespace

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:quest_id>', views.questDetail, name='questDetail'),
    path('questionCreate', views.questCreate, name='questCreate'),
    path('answerCreate/<int:quest_id>', views.answerCreate, name='answerCreate'),
]