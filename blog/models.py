import markdown2
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")

    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")

    slug = models.SlugField(max_length=200, unique=True,
                            help_text="Uma versão curta e legível do título para URLs.")

    content = models.TextField(verbose_name="Conteúdo (HTML ou Markdown)")

    content_markdown = models.TextField(verbose_name="Conteúdo em Markdown")

    content_html = models.TextField(editable=False)

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts', verbose_name="Autor")
    published_date = models.DateTimeField(default=timezone.now,
                                          verbose_name="Data de Publicação")
    cover_image = models.ImageField(upload_to='blog_covers/',
                                    blank=True, null=True,
                                    verbose_name="Imagem de Capa")

    class Meta:
        ordering = ['-published_date']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:post_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        import markdown2
        self.content_html = markdown2.markdown(self.content_markdown)
        super().save(*args, **kwargs)


