from django.db import models

from stdimage.models import StdImageField


class Base(models.Model):
    criados = models.DateField("Criação", auto_now_add=True)
    modificado = models.DateField("Atualização", auto_now=True)
    ativo = models.BooleanField("Ativo?", default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ("lni-cog", "Engrenagem"),
        ("lni-stats-up", "Gráfico"),
        ("lni-users", "Usuários"),
        ("lni-layers", "Design"),
        ("lni-mobile", "Mobile"),
        ("lni-rocket", "Foguete"),
    )
    servico = models.CharField("Serviço", max_length=100)
    descricao = models.TextField("Descrição", max_length=200)
    icone = models.CharField("Icone", max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField("Cargo", max_length=100)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField("Nome", max_length=100)
    cargo = models.ForeignKey(
        "core.Cargo", verbose_name="Cargo", on_delete=models.CASCADE
    )
    bio = models.TextField("Bio", max_length=200)
    imagem = StdImageField(
        "Imagem",
        upload_to="equipe",
        variations={"thumb": {"width": 480, "height": 480, "crop": True}},
    )
    facebook = models.CharField("Facebook", max_length=100, default="#")
    twitter = models.CharField("Twitter", max_length=100, default="#")
    instagram = models.CharField("Instagram", max_length=100, default="#")

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    def __str__(self):
        return self.nome


class Funcionalidades(Base):
    ICONE_CHOICES = (
        ("lni-rocket", "Foguete"),
        ("lni-laptop-phone", "Eletrónicos"),
        ("lni-cog", "Engrenagem"),
        ("lni-leaf", "Folha"),
        ("lni-layers", "Camadas"),
    )
    nome = models.CharField("Nome", max_length=100)
    descricao = models.TextField("Descrição", max_length=200)
    icone = models.CharField("Icone", max_length=16, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = "Funcionalidade"
        verbose_name_plural = "Funcionalidades"

    def __str__(self):
        return self.nome


class Feedbacks(Base):
    ICONE_CHOICES = (
        (0, "Nenhuma estrela"),
        (1, "Uma estrela"),
        (2, "Duas estrelas"),
        (3, "Três estrelas"),
        (4, "Quatro estrelas"),
        (5, "Cinco estrelas"),
    )

    nome = models.CharField("Nome", max_length=100)
    profissao = models.CharField("Profissão", max_length=200)
    feedbacks = models.TextField("Feedbacks", max_length=400)
    estrelas = models.IntegerField(
        "Quantidade de Estrelas", choices=ICONE_CHOICES, default=1
    )

    imagem = StdImageField(
        "Imagem",
        upload_to="staticfiles_build/img/testimonial",
        variations={"thumb": {"width": 180, "height": 180, "crop": True}},
    )

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"

    def __str__(self):
        return self.nome

    def estrelas_preenchidas(self):
        return range(self.estrelas)

    def estrelas_vazias(self):
        return range(5 - self.estrelas)
