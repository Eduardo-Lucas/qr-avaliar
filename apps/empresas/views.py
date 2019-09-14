from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from apps.empresas.models import Empresa


class EmpresaListView(ListView):
    model = Empresa


class EmpresaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Empresa
    fields = ['nome', ]
    success_message = 'A Empresa %(nome)s foi criada com sucesso!'
    
    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        

class EmpresaDetailView(LoginRequiredMixin, DetailView):
    model = Empresa


class EmpresaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Empresa
    fields = ['nome', ]
    success_message = 'A Empresa %(nome)s foi atualizada com sucesso!'


class EmpresaDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Empresa
    success_message = 'A empresa foi apagada com sucesso!'
    success_url = reverse_lazy('empresa_list')
