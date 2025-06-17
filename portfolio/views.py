# portfolio/views.py

from django.shortcuts import render
from .models import Experience, Skill, Formacao, SobreMim, Projeto, Apresentacao, VisitorCount
from collections import OrderedDict
from captcha.utils import process_first_visit

def home(request):
    # --- Busca todos os dados necessários ---
    apresentacao = Apresentacao.objects.first()
    experiences = Experience.objects.all()
    formacoes = Formacao.objects.all()
    sobre_mim = SobreMim.objects.first() # Renomeado para 'sobre_mim' para consistência
    projetos = Projeto.objects.all()
    visitor_count_obj, created = VisitorCount.objects.get_or_create(pk=1)

    # --- Agrupa as Skills por Categoria ---
    skills_by_category = OrderedDict()
    category_order = ['backend', 'frontend', 'database_tools', 'ai_other']
    category_names = dict(Skill.CATEGORY_CHOICES)

    if not request.session.get('has_visited', False):
        visitor_count_obj.count += 1
        visitor_count_obj.save()

        process_first_visit(request)
        request.session['has_visited'] = True

    for cat_key in category_order:
        skills_in_cat = Skill.objects.filter(category=cat_key)
        if skills_in_cat.exists():
            category_display_name = category_names.get(cat_key)
            skills_by_category[category_display_name] = skills_in_cat

    context = {
        'apresentacao': apresentacao,
        'experiences': experiences,
        'formacoes': formacoes,
        'sobre_mim': sobre_mim,
        'projetos': projetos,
        'skills_by_category': skills_by_category,
        'total_visitors': visitor_count_obj.count,
    }

    return render(request, 'index.html', context)