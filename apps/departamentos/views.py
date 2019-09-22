from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  UpdateView,
                                  DeleteView,
                                  CreateView)

from apps.departamentos.models import Departamento


class DepartamentoList(LoginRequiredMixin, ListView):
    """Lista os Departamentos da empresa logada"""
    model = Departamento
    
    def get_queryset(self):
        """Pega a empresa logada a partir do Usuário logado """
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentoEdit(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Departamento
    fields = ['nome']
    success_message = "O Departamento %(nome)s foi alterado com sucesso."


class DepartamentoDelete(LoginRequiredMixin, DeleteView):
    model = Departamento
    success_url = reverse_lazy('departamento_list')


class DepartamentoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Departamento
    fields = ['nome']
    success_message = "O Departamento %(nome)s foi criado com sucesso."
    success_url = reverse_lazy('departamento_list')
    
    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreate, self).form_valid(form)
