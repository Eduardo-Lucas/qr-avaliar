from django.urls import path

from apps.avaliacoes.views import *
app_name = 'avaliacoes'
urlpatterns = [
    # path('list', EmpresaListView.as_view(), name='empresa_list'),
    path('create/<int:evento_id>', create_avaliacao, name='create_avaliacao'),
    # path('detail/<int:pk>', EmpresaDetailView.as_view(), name='empresa_detail'),
    # path('update/<int:pk>', EmpresaUpdateView.as_view(), name='empresa_update'),
    # path('delete/<int:pk>', EmpresaDeleteView.as_view(), name='empresa_delete'),

]
