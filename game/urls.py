from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("partida", views.round, name="round")
]