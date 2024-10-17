from django.urls import path
from . import views

urlpatterns= [
    path("analisis", views.analisis, name="analisis"),
    path("index", views.index, name="index")

]