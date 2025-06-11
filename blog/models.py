# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import markdown2


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True,help_text="Deixe em branco para gerar automaticamente a partir do título.")
    content_markdown = models.TextField(verbose_name="Conteúdo (Markdown)", blank=True)
    content_html = models.TextField(verbose_name="Conteúdo (HTML)", editable=False, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    cover_image = models.ImageField(upload_to='blog_covers/', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.content_markdown:
            self.content_html = markdown2.markdown(self.content_markdown,
                                                   extras=['fenced-code-blocks', 'code-friendly'])
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)