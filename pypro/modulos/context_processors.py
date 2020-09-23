from pypro.modulos import facade


def modulos_ordenados(request):
    return {"MODULOS": facade.listar_modulos_ordenados()}
