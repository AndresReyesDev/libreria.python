from django import forms
from .models import Book, Language, Genre, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'summary',
            'imprint',
            'isbn',
            'genre',
            'language'
        ]

        labels = {
            'title': 'Título',
            'author': 'Autor',
            'summary': 'Descripción',
            'imprint': 'Imprenta',
            'isbn': 'ISBN',
            'genre': 'Género',
            'language': 'Idioma'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control'}),
            'imprint': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'language': forms.Select(attrs={'class': 'form-control'})
        }


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