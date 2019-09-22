from django.urls import path

from apps.accounts.views import SignUp, PerfilCreateView, PerfilUpdateView, PerfilDetailView

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('create/', PerfilCreateView.as_view(), name='perfil_create'),
    path('update/<int:pk>', PerfilUpdateView.as_view(), name='perfil_update'),
    path('detail/<int:pk>', PerfilDetailView.as_view(), name='perfil_detail'),
]
