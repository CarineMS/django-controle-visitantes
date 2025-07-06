from django.shortcuts import render
from visitantes.models import Visitante

from django.utils import timezone

def index(request):

    todos_visitantes = Visitante.objects.all()

    visitantes_aguardando = todos_visitantes.filter(
        status="AGUARDANDO"
    )

    visitantes_em_visita = todos_visitantes.filter(
        status="EM_VISITA"
    )

    visitantes_finalizado = todos_visitantes.filter(
        status="FINALIZADO"
    )

    current_date = timezone.now()
    current_month = current_date.month

    visitantes_mes = todos_visitantes.filter(
        horario_chegada__month=current_month
    )


    context = {
        "nome_pagina" : "Início do dashboard",
        "todos_visitantes" : todos_visitantes,
        "visitantes_aguardando": visitantes_aguardando.count(),
        "visitantes_em_visita": visitantes_em_visita.count(),
        "visitantes_finalizado": visitantes_finalizado.count(),
        "visitantes_mes": visitantes_mes.count(),
    }

    return render(request, "index.html", context)