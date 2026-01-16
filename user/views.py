from django.shortcuts import render, get_object_or_404
from bookshelf.models import Book, Shelf

def view_user(request, username):
    bookshelves = Shelf.objects.filter(ownerID__username=username).prefetch_related('book_set')
    print("bookshelves", bookshelves)
    return render(request, "pages/bookshelves_overview.html", {"shelves": bookshelves})