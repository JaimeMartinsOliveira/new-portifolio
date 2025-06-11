from django.shortcuts import render
from .models import Experience, Skill, Formacao, SobreMim, Projeto, Apresentacao


def home(request):
    apresentacao = Apresentacao.objects.first()  # <-- novo
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    formacoes = Formacao.objects.all()
    sobre = SobreMim.objects.first()
    projetos = Projeto.objects.all()

    return render(request, 'index.html', {
        'apresentacao': apresentacao,  # <-- novo
        'experiences': experiences,
        'skills': skills,
        'formacoes': formacoes,
        'sobre': sobre,
        'projetos': projetos,
    })
