from django.urls import path

from apps.empresas.views import *

urlpatterns = [
    path('list', EmpresaListView.as_view(),  name='empresa_list'),
    path('create', EmpresaCreateView.as_view(),  name='empresa_create'),
    path('detail/<int:pk>', EmpresaDetailView.as_view(),  name='empresa_detail'),
    path('update/<int:pk>', EmpresaUpdateView.as_view(),  name='empresa_update'),
    path('delete/<int:pk>', EmpresaDeleteView.as_view(),  name='empresa_delete'),
    
]
