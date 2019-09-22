from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DetailView

from apps.accounts.models import Perfil


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class PerfilCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Perfil
    fields = ['nome', 'whatsapp', 'email']
    success_message = 'O Perfil %(nome)s foi criado com sucesso.'
    template_name = 'accounts/perfil_form.html'
    success_url = reverse_lazy('login')


class PerfilUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Perfil
    fields = ['nome', 'whatsapp', 'email']
    template_name = 'accounts/perfil_form.html'
    success_message = 'O Perfil %(nome)s foi alterado com sucesso.'
    success_url = reverse_lazy('home')

    
class PerfilDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Perfil
    fields = ['nome', 'whatsapp', 'email']
    success_message = 'O Perfil %(nome)s foi alterado com sucesso.'
    success_url = reverse_lazy('home')
