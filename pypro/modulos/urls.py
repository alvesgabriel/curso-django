from django.urls import path
from pypro.modulos import views

app_name = "modulos"
urlpatterns = [
    path("", views.indice, name="indice"),
    path("<slug:slug>/", views.detalhe, name="detalhe"),
    path("aula/<slug:slug>/", views.aula, name="aula"),
]
