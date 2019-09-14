from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from apps.perguntas.models import Pergunta


class PerguntaListView(ListView):
    model = Pergunta


class PerguntaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Pergunta
    fields = ['texto_da_pergunta', ]
    success_message = 'A pergunta %(texto_da_pergunta)s foi criada com sucesso!'


class PerguntaDetailView(LoginRequiredMixin, DetailView):
    model = Pergunta


class PerguntaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Pergunta
    fields = ['texto_da_pergunta', ]
    success_message = 'A pergunta %(texto_da_pergunta)s foi atualizada com sucesso!'
    

class PerguntaDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Pergunta
    success_message = 'A pergunta foi apagada com sucesso!'
    success_url = reverse_lazy('pergunta_list')
