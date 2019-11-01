from django.urls import path
from django.conf.urls import url
# Books
from .views import BookList, BookCreate, BookDetail, BookDelete, BookUpdate
# Languages
from .views import LanguageList
# Genres
from .views import GenreList
# Authors
from .views import AuthorList, AuthorCreate, AuthorDetail, AuthorDelete, AuthorUpdate
# Reservations
from .views import ReservationList

urlpatterns = [

    # Books
    url(r'^$', BookList.as_view(), name='books_list'),
    url(r'^books/new/$', BookCreate.as_view(), name='books_create'),
    url(r'^books/detail/(?P<pk>\d+)/$', BookDetail.as_view(), name='books_detail'),
    url(r'^books/update/(?P<pk>\d+)/$', BookUpdate.as_view(), name='books_update'),
    url(r'^books/delete/(?P<pk>\d+)/$', BookDelete.as_view(), name='books_delete'),

    # Languages
    url(r'^languages', LanguageList.as_view(), name='languages_list'),

    # Genres
    url(r'^genres', GenreList.as_view(), name='genres_list'),

    # Authors
    url(r'^authors$', AuthorList.as_view(), name='authors_list'),
    url(r'^authors/new/$', AuthorCreate.as_view(), name='authors_create'),
    url(r'^authors/detail/(?P<pk>\d+)/$', AuthorDetail.as_view(), name='authors_detail'),
    url(r'^authors/update/(?P<pk>\d+)/$', AuthorUpdate.as_view(), name='authors_update'),
    url(r'^authors/delete/(?P<pk>\d+)/$', AuthorDelete.as_view(), name='authors_delete'),

    # Reservations
    url(r'^reservations', ReservationList.as_view(), name='reservations_list'),
]