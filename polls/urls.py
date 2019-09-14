from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.QuestionList.as_view(), name='question-list'),
    path('question-detail', views.QuestionDetail.as_view(), name='question-detail'),
    path('question-add', views.QuestionCreate.as_view(), name='question-add'),
    path('question-edit', views.QuestionCreate.as_view(), name='question-add'),
]
