from django.urls import path

from apps.perguntas.views import *

urlpatterns = [
    path('list', PerguntaListView.as_view(),  name='pergunta_list'),
    path('create', PerguntaCreateView.as_view(),  name='pergunta_create'),
    path('detail/<int:pk>', PerguntaDetailView.as_view(),  name='pergunta_detail'),
    path('update/<int:pk>', PerguntaUpdateView.as_view(),  name='pergunta_update'),
    path('delete/<int:pk>', PerguntaDeleteView.as_view(),  name='pergunta_delete'),
    
]
