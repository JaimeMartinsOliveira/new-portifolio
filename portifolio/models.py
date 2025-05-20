from django.db import models
from django.utils.text import slugify

class BlogPost(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='blog_imagens/', blank=True, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
    
class Experience(models.Model):
    titulo = models.CharField(max_length=100) 
    empresa = models.CharField(max_length=100, blank=True) 
    periodo = models.CharField(max_length=100, blank=True)  
    descricao = models.TextField()
    tecnologias = models.CharField(max_length=300) 
    imagem = models.ImageField(upload_to='experiencias/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo

    def __str__(self):
        return f"{self.cargo} - {self.empresa}"

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
    sobre = models.TextField()

    def __str__(self):
        return self.sobre[:50]