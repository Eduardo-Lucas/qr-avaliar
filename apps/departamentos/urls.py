from django.urls import path

from apps.departamentos.views import (
    DepartamentoCreate,
    DepartamentoList,
    DepartamentoEdit,
    DepartamentoDelete)

urlpatterns = [
    path('list', DepartamentoList.as_view(), name='departamento_list'),
    path('create', DepartamentoCreate.as_view(), name='departamento_create'),
    path('edit/<int:pk>', DepartamentoEdit.as_view(), name='departamento_edit'),
    path('delete/<int:pk>', DepartamentoDelete.as_view(), name='departamento_delete'),

]
