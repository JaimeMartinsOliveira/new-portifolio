from django.contrib import admin
from .models import Experience, Skill, Formacao, SobreMim, Tecnologia, Projeto, Apresentacao, VisitorCount

admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Formacao)
admin.site.register(SobreMim)
admin.site.register(Tecnologia)
admin.site.register(Projeto)
admin.site.register(Apresentacao)

@admin.register(VisitorCount)
class VisitorCountAdmin(admin.ModelAdmin):
    list_display = ('id', 'count')