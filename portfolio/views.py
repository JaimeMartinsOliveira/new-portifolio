# portfolio/views.py

from django.shortcuts import render
from .models import Experience, Skill, Formacao, SobreMim, Projeto, Apresentacao
from collections import OrderedDict


def home(request):
    # --- Busca todos os dados necessários ---
    apresentacao = Apresentacao.objects.first()
    experiences = Experience.objects.all()
    formacoes = Formacao.objects.all()
    sobre_mim = SobreMim.objects.first() # Renomeado para 'sobre_mim' para consistência
    projetos = Projeto.objects.all()

    # --- Agrupa as Skills por Categoria ---
    skills_by_category = OrderedDict()
    category_order = ['backend', 'frontend', 'database_tools', 'ai_other']
    category_names = dict(Skill.CATEGORY_CHOICES)

    for cat_key in category_order:
        skills_in_cat = Skill.objects.filter(category=cat_key)
        if skills_in_cat.exists():
            category_display_name = category_names.get(cat_key)
            skills_by_category[category_display_name] = skills_in_cat

    # --- Monta o contexto FINAL para enviar ao template ---
    context = {
        'apresentacao': apresentacao,
        'experiences': experiences,
        'formacoes': formacoes,
        'sobre_mim': sobre_mim, # Enviando a variável com o nome correto
        'projetos': projetos,
        'skills_by_category': skills_by_category, # A variável que faltava!
    }

    # --- Renderiza o template com o contexto completo ---
    return render(request, 'index.html', context)