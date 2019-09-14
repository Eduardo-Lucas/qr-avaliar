from django.contrib.auth.forms import UserCreationForm

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.views.generic import CreateView

from apps.accounts.models import Perfil


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class PerfilCreateView(SuccessMessageMixin, CreateView):
    model = Perfil
    fields = ['nome', 'email']
    success_message = 'O Perfil %(nome)s foi criado com sucesso.'
    template_name = 'perfil_form.html'
    success_url = reverse_lazy('login')
