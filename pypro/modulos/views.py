from django.shortcuts import render
from pypro.modulos import facade


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.listar_aulas_de_modulo_ordenadas(modulo)
    return render(request, "modulos/detalhe.html", context={"modulo": modulo, "aulas": aulas})


def aula(resp, slug):
    pass
