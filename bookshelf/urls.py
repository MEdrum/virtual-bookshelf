from django.urls import path
from bookshelf import views

urlpatterns = [
    path("", views.bookshelves_overview, name="bookshelves"),
]