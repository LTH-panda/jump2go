from django.urls import path
from . import views

urlpatterns = [
    path('<int:quest_id>', views.questDetail, name = 'questDetail'),
    path('', views.index, name = 'index'),
]