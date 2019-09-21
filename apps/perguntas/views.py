from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.forms import modelformset_factory

from apps.perguntas.forms import PerguntaForm
from apps.perguntas.models import Pergunta


class PerguntaListView(ListView):
    model = Pergunta


# class PerguntaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#     model = Pergunta
#     fields = ['texto_da_pergunta', ]
#     success_message = 'A pergunta %(texto_da_pergunta)s foi criada com sucesso!'
def manage_pergunta(request):
    PerguntaFormSet = modelformset_factory(Pergunta, fields=('texto_da_pergunta',),
                                           can_delete=False, extra=5, )
    if request.method == 'POST':
        formset = PerguntaFormSet(request.POST, )
        if formset.is_valid():
            formset.save()
            redirect('perguntas/pergunta_form.html', {'formset': formset})
    else:
        formset = PerguntaFormSet()
    
    return render(request, 'perguntas/pergunta_form.html', {'formset': formset})


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
