from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView)

from apps.funcionarios.models import Funcionario


class FuncionarioList(ListView):
    """Lista os Funcionários da empresa logada"""
    model = Funcionario
    
    def get_queryset(self):
        """Pega a empresa logada a partir do Usuário logado """
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamento']
    success_url = reverse_lazy('funcionario_list')


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamento']
    success_url = reverse_lazy('funcionario_list')
    
    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionario_list')
