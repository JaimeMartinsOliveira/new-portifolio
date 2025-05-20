from django.contrib import admin
from .models import BlogPost, Experience, Skill, Formacao, SobreMim, Tecnologia, Projeto

admin.site.register(BlogPost)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Formacao)
admin.site.register(SobreMim)
admin.site.register(Tecnologia)
admin.site.register(Projeto)