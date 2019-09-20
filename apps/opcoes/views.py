from django.forms import inlineformset_factory
from django.shortcuts import render, redirect

from apps.opcoes.models import Opcao
from apps.perguntas.models import Pergunta


def create_opcao(request, pergunta_id):
    pergunta = Pergunta.objects.get(id=pergunta_id)
    OpcaoFormset = inlineformset_factory(Pergunta, Opcao, fields=('opcao', ),
                                         can_delete=True, extra=5)

    if request.method == 'POST':
        formset = OpcaoFormset(request.POST, instance=pergunta)
        if formset.is_valid():
            formset.save()
            
            redirect('opcoes/opcao_form.html', pergunta_id=pergunta.id)
        
    # formset = OpcaoFormset(queryset=Opcao.objects.filter(pergunta_id=pergunta.id))
    formset = OpcaoFormset(instance=pergunta)
    
    return render(request, 'opcoes/opcao_form.html', {'pergunta': pergunta,
                                                      'formset':  formset})
