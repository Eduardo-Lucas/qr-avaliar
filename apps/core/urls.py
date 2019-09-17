from django.urls import path

from apps.core.views import HomeView, ComoFuncionaView, PlanosView

urlpatterns = [
    path('', HomeView.as_view(),  name='home'),
    path('como_funciona', ComoFuncionaView.as_view(),  name='como_funciona'),
    path('planos', PlanosView.as_view(),  name='planos'),
    
]
