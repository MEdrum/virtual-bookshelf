from django.urls import path
from bookshelf import views

urlpatterns = [
    path("", views.bookshelves_overview, name="bookshelves"),
    path("<str:shelfid>/<str:isbn>/", views.view_book, name="view-book"),
]