from django.contrib import admin
from .models import BlogPost, Experience, Skill, Formacao

admin.site.register(BlogPost)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Formacao)