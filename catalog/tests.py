from django.test import TestCase, Client
from .models import Author, Book, Genre, Language


def create_author(first_name, last_name):
    return Author.objects.create(first_name=first_name, last_name=last_name)


class BookModelTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_create_book(self):
        instance = Book.objects.create(title='Título', summary='Resumen', imprint='Imprenta', isbn='0011223344')
        self.assertEqual(instance.__str__(), 'Título')


class AuthorModelTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list_view(self):
        response = self.client.get('/authors')
        self.assertEqual(response.status_code, 200)

    def test_create_author(self):
        instance = Author.objects.create(first_name='Nombre', last_name='Apellido')
        self.assertEqual(instance.__str__(), 'Nombre Apellido')


class GenreModelTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list_view(self):
        response = self.client.get('/genres')
        self.assertEqual(response.status_code, 200)

    def test_create_genre(self):
        instance = Genre.objects.create(name='Género')
        self.assertEqual(instance.__str__(), 'Género')


class LanguageModelTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list_view(self):
        response = self.client.get('/languages')
        self.assertEqual(response.status_code, 200)

    def test_create_language(self):
        instance = Language.objects.create(name='Idioma')
        self.assertEqual(instance.__str__(), 'Idioma')
