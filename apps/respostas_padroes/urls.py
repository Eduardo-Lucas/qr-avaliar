from django.urls import path

from apps.respostas_padroes.views import *

urlpatterns = [
    path('list', RespostaPadraoListView.as_view(),  name='resposta_padrao_list'),
    path('create', manage_resposta_padrao,  name='resposta_padrao_create'),
    path('detail/<int:pk>', RespostaPadraoDetailView.as_view(),  name='resposta_padrao_detail'),
    path('update/<int:pk>', RespostaPadraoUpdateView.as_view(),  name='resposta_padrao_update'),
    path('delete/<int:pk>', RespostaPadraoDeleteView.as_view(),  name='resposta_padrao_delete'),
]
