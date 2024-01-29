from django.shortcuts import render

from django.views.generic import TemplateView

#Exemplo de Class Based Views

class indexView(TemplateView):
    tamplate_name = 'index.html'
