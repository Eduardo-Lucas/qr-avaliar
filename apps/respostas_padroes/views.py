from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView

from apps.respostas_padroes.models import RespostaPadrao


class RespostaPadraoListView(ListView):
    model = RespostaPadrao


def manage_resposta_padrao(request):
    RespostaPadraoFormSet = modelformset_factory(RespostaPadrao, fields=('texto',),
                                                 can_delete=False, extra=1,)
    if request.method == 'POST':
        formset = RespostaPadraoFormSet(request.POST, )
        if formset.is_valid():
            formset.save()
            redirect('respostas_padroes/respostapadrao_form.html', {'formset': formset})
    else:
        formset = RespostaPadraoFormSet()
        
    return render(request, 'respostas_padroes/respostapadrao_form.html',
                  {'formset': formset})
        
    
class RespostaPadraoDetailView(DetailView):
    model = RespostaPadrao
    

class RespostaPadraoUpdateView(UpdateView):
    model = RespostaPadrao
    fields = ['texto', ]
    

class RespostaPadraoDeleteView(DeleteView):
    model = RespostaPadrao
    success_url = reverse_lazy('resposta_padrao_list')
