from django.urls import path
from bookshelf import views

urlpatterns = [
    path("", views.bookshelves_overview, name="bookshelves"),
    path("<str:shelfid>/<str:isbn>/", views.view_book, name="view-book"),
    path('book/new/<str:shelfid>/', views.process_book_form, name='new_book'),
    path('book/edit/<str:shelfid>/<uuid:bookid>/', views.process_book_form, name='edit_book'),
   ]