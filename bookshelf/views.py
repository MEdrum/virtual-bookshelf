from django.shortcuts import render
from projects.models import Project

def bookshelves_overview(request):
    return render(request, "pages/bookshelves_overview.html", {})