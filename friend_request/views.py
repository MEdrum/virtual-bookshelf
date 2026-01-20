from django.shortcuts import render

def friend_requests_overview(request):
    return render(request, "pages/friend_requests_overview.html", {})