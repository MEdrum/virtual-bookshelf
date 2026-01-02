from django.urls import path
from friend_request import views

urlpatterns = [
    path("", views.friend_requests_overview, name="friend_requests"),
]