from django.shortcuts import render
from projects.models import Project

def friend_requests_overview(request):
    return render(request, "pages/friend_requests_overview.html", {})