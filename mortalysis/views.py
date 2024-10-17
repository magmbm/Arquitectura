from django.shortcuts import render
from . import models

# Create your views here.

def analisis(request):
    return render(request, "mortalysis/analisis.html", {})

def index(request):
    return render(request, "mortalysis/index.html", {})