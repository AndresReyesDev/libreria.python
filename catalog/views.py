from django.shortcuts import render, redirect
from .models import Book, Genre, Language, Author, BookInstance
from .forms import BookForm


# List views.
def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books.html', {'books': books})


def languages_list(request):
    languages = Language.objects.all()
    return render(request, 'languages/languages.html', {'languages': languages})


def genres_list(request):
    genres = Genre.objects.all()
    return render(request, 'genres/genres.html', {'genres': genres})


def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors/authors.html', {'authors': authors})


def reservations_list(request):
    reservations = BookInstance.objects.all()
    return render(request, 'reservations/reservations.html', {'reservations': reservations})


# Create views
def books_create(request):
    if request.POST:
        return render(request, 'books/books_view.html', {'authors': authors, 'languages': languages, 'genres': genres})
    else:
        authors = Author.objects.all()
        languages = Language.objects.all()
        genres = Genre.objects.all()
        return render(request, 'books/books_form.html', {'authors': authors, 'languages': languages, 'genres': genres})
