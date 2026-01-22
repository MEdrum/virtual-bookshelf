from django.urls import path
from bookshelf import views

urlpatterns = [
    path("", views.bookshelves_overview, name="bookshelves"),
    path("add/", views.add_bookshelf, name="add-bookshelf"),
    path("<str:shelfid>/<str:isbn>/", views.view_book, name="view-book"),
    path('book/new/<str:shelfid>/', views.process_book_form, name='new_book'),
    path('book/edit/<str:shelfid>/<uuid:bookid>/', views.process_book_form, name='edit_book'),
    path("<str:shelfid>/", views.view_shelf, name="view-shelf"),
]
