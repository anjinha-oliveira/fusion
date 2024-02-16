from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

from .models import Servico, Funcionario, Funcionalidades
from .forms import ContatoForm

#Exemplo de Class Based Views

class indexView(TemplateView, FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super(indexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['funcionalidades'] = Funcionalidades.objects.order_by('?').all()

        return context



