from django.forms import inlineformset_factory
from django.shortcuts import render, redirect

from apps.avaliacoes.models import Avaliacao
from apps.eventos.models import Evento


def create_avaliacao(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    AvaliacaoFormset = inlineformset_factory(Evento, Avaliacao, fields=('pergunta', 'tipo', 'ordem'),
                                             can_delete=True, extra=3)
    
    if request.method == 'POST':
        formset = AvaliacaoFormset(request.POST, instance=evento)
        if formset.is_valid():
            formset.save()
            
            redirect('avaliacoes/avaliacao_form.html', evento_id=evento.id)
        
    formset = AvaliacaoFormset(instance=evento)
    
    return render(request, 'avaliacoes/avaliacao_form.html', {'evento': evento,
                                                              'formset':  formset})
