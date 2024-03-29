from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import Book, Genre, Language, Author, BookInstance
from django.urls import reverse_lazy
from .forms import BookForm, AuthorForm, GenreForm, LanguageForm, ReservationForm
# Auth
from django.contrib.auth.forms import UserCreationForm
from django.views import generic


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


class LanguageDetail(DetailView):
    model = Language
    template_name = 'languages/languages_detail.html'


class LanguageCreate(CreateView):
    model = Language
    form_class = LanguageForm
    template_name = 'languages/languages_form.html'
    success_url = reverse_lazy('catalog:languages_list')


class LanguageDelete(DeleteView):
    model = Language
    template_name = 'languages/languages_delete.html'
    success_url = reverse_lazy('catalog:languages_list')


class LanguageUpdate(UpdateView):
    model = Language
    form_class = LanguageForm
    template_name = 'languages/languages_form.html'
    success_url = reverse_lazy('catalog:languages_list')


# Genres
class GenreList(ListView):
    queryset = Genre.objects.order_by('id')
    template_name = 'genres/genres_list.html'


class GenreDetail(DetailView):
    model = Genre
    template_name = 'genres/genres_detail.html'


class GenreCreate(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'genres/genres_form.html'
    success_url = reverse_lazy('catalog:genres_list')


class GenreDelete(DeleteView):
    model = Genre
    template_name = 'genres/genres_delete.html'
    success_url = reverse_lazy('catalog:genres_list')


class GenreUpdate(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'genres/genres_form.html'
    success_url = reverse_lazy('catalog:genres_list')


# Authors
class AuthorList(ListView):
    queryset = Author.objects.order_by('id')
    template_name = 'authors/authors_list.html'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'authors/authors_detail.html'


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors/authors_form.html'
    success_url = reverse_lazy('catalog:authors_list')


class AuthorDelete(DeleteView):
    model = Author
    template_name = 'authors/authors_delete.html'
    success_url = reverse_lazy('catalog:authors_list')


class AuthorUpdate(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors/authors_form.html'
    success_url = reverse_lazy('catalog:authors_list')


# Reservations
class ReservationList(ListView):
    queryset = BookInstance.objects.order_by('id')
    template_name = 'reservations/reservations_list.html'


class ReservationDetail(DetailView):
    model = BookInstance
    pk_url_kwarg = 'id'
    template_name = 'reservations/reservations_detail.html'


class ReservationCreate(CreateView):
    model = BookInstance
    form_class = ReservationForm
    template_name = 'reservations/reservations_form.html'
    success_url = reverse_lazy('catalog:reservations_list')


class ReservationDelete(DeleteView):
    model = BookInstance
    template_name = 'reservations/reservations_delete.html'
    success_url = reverse_lazy('catalog:reservations_list')


class ReservationUpdate(UpdateView):
    model = BookInstance
    form_class = ReservationForm
    template_name = 'reservations/reservations_form.html'
    success_url = reverse_lazy('catalog:reservations_list')


# Auth
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def redirect_view(request):
    response = redirect('/')
    return response
