from django.shortcuts import render, get_object_or_404
from .models import Shelf, Book
import uuid

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

def process_book_form(request, shelfid, bookid=None):
    shelf = get_object_or_404(Shelf, shelfID=shelfid)

    is_edit = bookid is not None

    if bookid:
        book = get_object_or_404(Book, bookID=bookid, shelfID=shelf)
    else:
        book = None

    if request.method == 'POST':
        if book is None:
            book = Book(
                bookID=uuid.uuid4(),
                ownerID=request.user,
                shelfID=shelf
            )

        book.title = request.POST['title']
        book.author = request.POST['author']
        book.isbn = request.POST['isbn']
        book.genre = request.POST['genre']
        book.language = request.POST['language']
        #book.year_of_publication = request.POST['pubDate']
        book.visibility = request.POST['visibility']
        book.borrowable = 'borrowable' in request.POST
        book.coverURL = request.POST['coverURL']

        book.save()
        return render(request, "pages/new_book_done.html", {"is_edit": is_edit})

    return render(request, "pages/edit_book.html", {
        "shelf": shelf,
        "book": book,
        "is_edit": book is not None
    })

def view_shelf(request, shelfid):
    shelf = get_object_or_404(Shelf, shelfID=shelfid)
    print("shelf", type(shelf))
    #shelves = Shelf.objects.prefetch_related(shelfid).all()
    #shelves = Shelf.objects.prefetch_related('book_set').all()
    return render(request, "pages/bookshelf_view_shelf.html", {"bookshelf": shelf})
