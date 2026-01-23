from django.shortcuts import render, get_object_or_404
from .models import Shelf, Book, GENRES, LANGUAGES
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
    if book.year_of_publication:
        pass
    else:
        book.year_of_publication = "Unknown"
    return render(
        request,
        "pages/view_book.html",
        {
            "shelf": shelf,
            "book": book,
            "current_genre": book.genre.title(),
            "current_language": book.language.title()
        })

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
        if not book:
            book = Book(
                bookID=uuid.uuid4(),
                ownerID=request.user,
                shelfID=shelf
            )

        book.title = request.POST['title']
        book.author = request.POST['author']
        book.isbn = request.POST['isbn']
        INV_GENRES = {v: k for k, v in GENRES}
        book.genre = INV_GENRES.get(request.POST['genre'], "")
        INV_LANGUAGES = {v: k for k, v in LANGUAGES}
        book.language = INV_LANGUAGES.get(request.POST['language'], "")
        book.year_of_publication = request.POST['pubYear']
        #print("pubdate:", request.POST['pubDate'])
        if request.POST['pubYear']:
            pass
            #dt = datetime.strptime(request.POST['pubDate'], "%Y-%m-%d").replace(tzinfo=timezone.utc)
            #book.year_of_publication = int(dt.timestamp())
        else:
            book.year_of_publication = 0
        book.visibility = request.POST['visibility']
        book.borrowable = 'borrowable' in request.POST
        book.coverURL = request.POST['coverURL']

        book.save()
        return render(request, "pages/new_book_done.html", {"is_edit": is_edit})

    current_genre = ""
    current_language = ""
    if book:
        if book.genre:
            current_genre = book.genre.title()
        if book.language:
            current_language = book.language.title()

    return render(request, "pages/edit_book.html", {
        "shelf": shelf,
        "book": book,
        "genres": dict(GENRES).values(),
        "current_genre": current_genre,
        "languages": dict(LANGUAGES).values(),
        "current_language": current_language,
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


