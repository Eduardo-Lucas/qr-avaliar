from django.urls import path
from apps.funcionarios.views import (
    FuncionarioList,
    FuncionarioEdit,
    FuncionarioDelete,
    FuncionarioCreate)

urlpatterns = [
    path('list', FuncionarioList.as_view(), name='funcionario_list'),
    path('create', FuncionarioCreate.as_view(), name='funcionario_create'),
    path('edit/<int:pk>', FuncionarioEdit.as_view(), name='funcionario_edit'),
    path('delete/<int:pk>', FuncionarioDelete.as_view(), name='funcionario_delete'),

]
