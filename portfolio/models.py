import markdown2
from django.db import models

class Tecnologia(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Experience(models.Model):
    titulo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100, blank=True)
    periodo = models.CharField(max_length=100, blank=True)
    descricao_md = models.TextField(verbose_name="Descrição (Markdown)", blank=True)
    descricao_html = models.TextField(verbose_name="Descrição (HTML)", editable=False, blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)
    imagem = models.ImageField(upload_to='experiencias/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.empresa} - {self.titulo}"

    def save(self, *args, **kwargs):
        self.descricao_html = markdown2.markdown(self.descricao_md, extras=["smarty-pants"])
        super().save(*args, **kwargs)

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('backend', 'Backend Development'),
        ('frontend', 'Frontend Development'),
        ('database_tools', 'Database & Tools'),
        ('ai_other', 'AI & Other Skills'),
    ]

    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='skills/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='backend', verbose_name="Categoria")

    def __str__(self):
        return f"{self.nome} ({self.get_category_display()})"

class Formacao(models.Model):
    imagem = models.ImageField(upload_to='experiencias/', blank=True, null=True)
    curso = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    ano_conclusao = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.curso} - {self.instituicao}"


class SobreMim(models.Model):
    conteudo_md = models.TextField(verbose_name="Conteúdo (Markdown)")
    conteudo_html = models.TextField(verbose_name="Conteúdo (HTML)", editable=False, blank=True)

    def __str__(self):
        return "Conteúdo da seção 'Sobre Mim'"

    def save(self, *args, **kwargs):
        self.conteudo_html = markdown2.markdown(self.conteudo_md, extras=["smarty-pants"])
        super().save(*args, **kwargs)



class Apresentacao(models.Model):
    nome = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='apresentacao/', blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    curriculo = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome

class VisitorCount(models.Model):

    count = models.PositiveIntegerField(default=0, verbose_name="Contagem")

    def __str__(self):
        return f"Contagem de Visitantes: {self.count}"

    class Meta:
        verbose_name = "Contagem de Visitante"
        verbose_name_plural = "Contagens de Visitantes"