from django.shortcuts import render

from django.views.generic import TemplateView

#Exemplo de Class Based Views

class indexView(TemplateView):
    template_name = 'index.html'
