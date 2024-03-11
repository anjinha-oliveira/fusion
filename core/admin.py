from django.contrib import admin

from .models import Cargo, Servico, Funcionario, Funcionalidades, Feedbacks


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ("cargo", "ativo", "modificado")


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ("servico", "icone", "ativo", "modificado")


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "cargo", "ativo", "modificado")


@admin.register(Funcionalidades)
class FuncionalidadesAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao", "icone")


@admin.register(Feedbacks)
class FeedbacksAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "profissao",
        "feedbacks",
        "estrelas",
    )
