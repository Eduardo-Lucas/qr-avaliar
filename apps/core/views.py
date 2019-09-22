from django.shortcuts import render
from django.views.generic import TemplateView

from apps.accounts.models import Perfil


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.request.user
        # if self.request.user:
        #     context['perfil'] = Perfil.objects.get(user_id=self.request.user.id)
        return context


class ComoFuncionaView(TemplateView):
    template_name = "core/como_funciona.html"


class PlanosView(TemplateView):
    template_name = "core/planos.html"
