from django.shortcuts import render
from projects.models import Project

def home(request):
    return render(request, "pages/home.html", {})