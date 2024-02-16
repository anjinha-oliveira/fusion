from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages

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
    
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(indexView, self).form_valid(form, *args, **kwargs)


