from bootstrap_datepicker_plus import DateTimePickerInput
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from apps.eventos.models import Evento


class EventoListView(ListView):
    model = Evento


class EventoCreateView(generic.edit.CreateView):
    model = Evento
    fields = ['nome', 'data_inicio', 'data_termino', 'descricao', 'publico_privado', 'local', 'cep', 'endereco',
              'numero', 'bairro', 'cidade', 'uf', 'absorver_taxa_servico']
    success_message = 'O Evento %(nome)s foi criado com sucesso!'

    def form_valid(self, form):
        evento = form.save(commit=False)
        evento.empresa = self.request.user.funcionario.empresa
        evento.save()
        return super(EventoCreateView, self).form_valid(form)
        
    def get_form(self):
        form = super().get_form()
        form.fields['data_inicio'].widget = DateTimePickerInput(options={
                                                           'format': '%d/%m/%Y %H:%M',
                                                           'showClose': True,
                                                           'showClear': True,
                                                           'showTodayButton': True,
                                                       })
        return form


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
