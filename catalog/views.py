from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import Book, Genre, Language, Author, BookInstance
from django.urls import reverse_lazy
from .forms import BookForm


# Books
class BookList(ListView):
    queryset = Book.objects.order_by('id')
    template_name = 'books/books_list.html'


class BookDetail(DetailView):
    model = Book
    template_name = 'books/books_detail.html'


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/books_form.html'
    success_url = reverse_lazy('catalog:books_list')


class BookDelete(DeleteView):
    model = Book
    template_name = 'books/books_delete.html'
    success_url = reverse_lazy('catalog:books_list')


class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/books_form.html'
    success_url = reverse_lazy('catalog:books_list')


# Languages
class LanguageList(ListView):
    queryset = Language.objects.order_by('id')
    template_name = 'languages/languages_list.html'


# Genres
class GenreList(ListView):
    queryset = Genre.objects.order_by('id')
    template_name = 'genres/genres_list.html'


# Authors
class AuthorList(ListView):
    queryset = Author.objects.order_by('id')
    template_name = 'authors/authors_list.html'


# Reservations
class ReservationList(ListView):
    queryset = BookInstance.objects.order_by('id')
    template_name = 'reservations/reservations_list.html'
