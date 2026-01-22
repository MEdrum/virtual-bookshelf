from django.shortcuts import render, get_object_or_404
from .models import Shelf, Book
import uuid
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import ShelfForm


def bookshelves_overview(request):
    """Renders the view bookshelves page

    Args:
        request (HttpRequest): An object containing the request details

    Returns:
        HttpResponse: Return an HttpResponse whose content is filled with the result of calling django.template.loader.render_to_string() with the passed arguments.
    """
    shelves = Shelf.objects.prefetch_related('book_set').all()
    return render(request, "pages/bookshelves_overview.html", {"shelves": shelves})

def view_book(request, shelfid, isbn):
    """Renders the view book page

    Args:
        request (HttpRequest): An object containing the request details
        shelfid (String): Unique identifier (UUID) for the bookshelf
        isbn (String): Unique identifier (UUID OR ISBN) for the book

    Returns:
        HttpResponse: Return an HttpResponse whose content is filled with the result of calling django.template.loader.render_to_string() with the passed arguments.
    """
    shelf = get_object_or_404(Shelf, shelfID=shelfid)
    print("shelf", type(shelf))
    try:
        book = get_object_or_404(Book, isbn=isbn, shelfID=shelf)
    except Exception as err:
        book = get_object_or_404(Book, bookID=isbn, shelfID=shelf)
    return render(request, "pages/view_book.html", {"shelf": shelf, "book": book})

def process_book_form(request, shelfid, bookid=None):
    """Creates or edits a book depending on the optional atribute bookid

    Args:
        request (HttpRequest): An object containing the request details
        shelfid (String): Unique identifier (UUID) for the bookshelf
        bookid (String, optional): Unique identifier (UUID) for the book. Defaults to None.

    Returns:
        HttpResponse: Return an HttpResponse whose content is filled with the result of calling django.template.loader.render_to_string() with the passed arguments.
    """
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
    """Renders the view (singular) shelf page

    Args:
        request (HttpRequest): An object containing the request details
        shelfid (String): Unique identifier (UUID) for the bookshelf

    Returns:
        HttpResponse: Return an HttpResponse whose content is filled with the result of calling django.template.loader.render_to_string() with the passed arguments.
    """
    shelf = get_object_or_404(Shelf, shelfID=shelfid)
    print("shelf", type(shelf))
    return render(request, "pages/bookshelf_view_shelf.html", {"bookshelf": shelf})

@login_required
def add_bookshelf(request):
    if request.method == "POST":
        name = request.POST.get("name")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")

        Shelf.objects.create(
            shelfID=uuid.uuid4(),
            name=name,
            latitude=latitude,
            longitude=longitude,
            ownerID=request.user
        )

        return redirect("bookshelves")

    return render(request, "pages/create_shelf.html")


