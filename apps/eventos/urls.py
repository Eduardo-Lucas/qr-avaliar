from django.urls import path

from apps.eventos.views import *

urlpatterns = [
    path('list', EventoListView.as_view(),  name='evento_list'),
    path('create', EventoCreateView.as_view(),  name='evento_create'),
    path('detail/<int:pk>', EventoDetailView.as_view(),  name='evento_detail'),
    path('update/<int:pk>', EventoUpdateView.as_view(),  name='evento_update'),
    path('delete/<int:pk>', EventoDeleteView.as_view(),  name='evento_delete'),
    
]
