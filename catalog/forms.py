from django import forms
from .models import Book, Language, Genre, Author, BookInstance


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

        labels = {'name': 'Idioma'}

        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

        labels = {'name': 'Género'}

        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'first_name',
            'last_name',
            'date_of_birth',
            'date_of_death'
        ]

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'date_of_birth': 'Fecha de Nacimiento',
            'date_of_death': 'Fecha de Muerte',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control', 'type': 'date'}),
            'date_of_death': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control', 'type': 'date'})
        }


class ReservationForm(forms.ModelForm):
    class Meta:
        model = BookInstance

        fields = [
            'book',
            'due_back',
            'status'
        ]

        labels = {
            'book': 'Libro',
            'due_back': 'Fecha de Devolución',
            'status': 'Estado'
        }

        widgets = {
            'book': forms.Select(attrs={'class': 'form-control'}),
            'due_back': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
