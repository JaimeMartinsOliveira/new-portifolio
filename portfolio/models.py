from django.db import models
from django.utils.text import slugify


class Tecnologia(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Experience(models.Model):
    titulo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100, blank=True)
    periodo = models.CharField(max_length=100, blank=True)
    descricao = models.TextField()
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)
    imagem = models.ImageField(upload_to='experiencias/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.empresa} - {self.titulo}"


class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo


class Skill(models.Model):
    nome = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50, blank=True)
    imagem = models.ImageField(upload_to='experiencias/', blank=True, null=True)

    def __str__(self):
        return self.nome


class Formacao(models.Model):
    imagem = models.ImageField(upload_to='experiencias/', blank=True, null=True)
    curso = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    ano_conclusao = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.curso} - {self.instituicao}"


class SobreMim(models.Model):
    titulo = models.CharField(max_length=200)  # Novo campo para o título
    sobre = models.TextField()  # Texto do "Sobre mim"

    def __str__(self):
        return self.titulo



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
