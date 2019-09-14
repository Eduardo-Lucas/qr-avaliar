"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('eventos/', include('apps.eventos.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('perguntas/', include('apps.perguntas.urls')),
    path('respostas_padroes/', include('apps.respostas_padroes.urls')),
    path('opcoes/', include('apps.opcoes.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
