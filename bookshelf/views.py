from django.shortcuts import render
from .models import Shelf

def bookshelves_overview(request):
    shelves = Shelf.objects.prefetch_related('book_set').all()
    print("shelves", shelves)
    print(shelves)
    print(shelves[0].book_set.all())
    return render(request, "pages/bookshelves_overview.html", {"shelves": shelves})