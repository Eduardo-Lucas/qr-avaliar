from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from apps.eventos.models import Evento


class EventoListView(ListView):
    model = Evento


class EventoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Evento
    fields = ['nome', 'data_inicio', 'data_termino', 'descricao', 'publico_privado',
              'local', 'cep', 'endereco', 'numero', 'bairro', 'cidade', 'uf', 'absorver_taxa_servico']
    success_message = 'O Evento %(nome)s foi criada com sucesso!'
    
    # def form_valid(self, form):
    #     obj = form.save()
    #     funcionario = self.request.user.funcionario
    #     funcionario.evento = obj
    #     funcionario.save()


class EventoDetailView(LoginRequiredMixin, DetailView):
    model = Evento


class EventoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Evento
    fields = ['nome', 'data_inicio', 'data_termino', 'descricao', 'publico_privado',
              'local', 'cep', 'endereco', 'numero', 'bairro', 'cidade', 'uf', 'absorver_taxa_servico']
    success_message = 'O Evento %(nome)s foi atualizada com sucesso!'


class EventoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Evento    
    success_url = reverse_lazy('evento_list')
