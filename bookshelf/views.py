from django.shortcuts import render, get_object_or_404
from .models import Shelf, Book

def bookshelves_overview(request):
    shelves = Shelf.objects.prefetch_related('book_set').all()
    return render(request, "pages/bookshelves_overview.html", {"shelves": shelves})

def view_book(request, shelfid, isbn):
    shelf = get_object_or_404(Shelf, shelfID=shelfid)
    print("shelf", type(shelf))
    try:
        book = get_object_or_404(Book, isbn=isbn, shelfID=shelf)
    except Exception as err:
        book = get_object_or_404(Book, bookID=isbn, shelfID=shelf)
    #shelves = Shelf.objects.prefetch_related(shelfid).all()
    #shelves = Shelf.objects.prefetch_related('book_set').all()
    return render(request, "pages/view_book.html", {"shelf": shelf, "book": book})

def view_shelf(request, shelfid):
    shelf = get_object_or_404(Shelf, shelfID=shelfid)
    print("shelf", type(shelf))
    #shelves = Shelf.objects.prefetch_related(shelfid).all()
    #shelves = Shelf.objects.prefetch_related('book_set').all()
    return render(request, "pages/bookshelf_view_shelf.html", {"bookshelf": shelf})