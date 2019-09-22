from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.request.user
        context['perfil_id'] = self.request.user.id
        print(context)
        return context


class ComoFuncionaView(TemplateView):
    template_name = "core/como_funciona.html"


class PlanosView(TemplateView):
    template_name = "core/planos.html"
