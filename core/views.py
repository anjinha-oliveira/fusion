from typing import Any
from django.shortcuts import render

from django.views.generic import TemplateView
from .models import Servico, Funcionario, Funcionalidades

#Exemplo de Class Based Views

class indexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(indexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        return context



