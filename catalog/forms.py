from django import forms
from .models import Book, Language, Genre, Author, BookInstance


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'summary', 'imprint', 'isbn', 'genre', 'language']


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']