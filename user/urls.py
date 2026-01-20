from django.urls import path
from user import views

urlpatterns = [
    # path("", views.bookshelves_overview, name="bookshelves"),
    path("<str:username>/", views.view_user, name="view-user"),
]