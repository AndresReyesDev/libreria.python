from django.urls import path
from .views import books_list, languages_list, genres_list, authors_list, reservations_list
from .views import books_create
from . import views

urlpatterns = [
    # List Models
    path('', books_list, name='books_list'),
    path('languages', languages_list, name='languages_list'),
    path('genres', genres_list, name='genres_list'),
    path('authors', authors_list, name='authors_list'),
    path('reservations', reservations_list, name='reservations_list'),

    # Create Model
    path('books/new', books_create, name='books_create'),
]