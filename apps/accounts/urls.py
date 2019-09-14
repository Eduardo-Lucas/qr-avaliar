from django.urls import path

from apps.accounts.views import SignUp, PerfilCreateView

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('create/', PerfilCreateView.as_view(), name='perfil_create'),
]
