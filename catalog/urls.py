from django.conf.urls import url
# Books
from .views import BookList, BookCreate, BookDetail, BookDelete, BookUpdate
# Languages
from .views import LanguageList, LanguageCreate, LanguageDetail, LanguageDelete, LanguageUpdate
# Genres
from .views import GenreList, GenreCreate, GenreDetail, GenreDelete, GenreUpdate
# Authors
from .views import AuthorList, AuthorCreate, AuthorDetail, AuthorDelete, AuthorUpdate
# Reservations
from .views import ReservationList, ReservationCreate, ReservationDetail, ReservationDelete, ReservationUpdate

urlpatterns = [

    # Books
    url(r'^$', BookList.as_view(), name='books_list'),
    url(r'^books/new/$', BookCreate.as_view(), name='books_create'),
    url(r'^books/detail/(?P<pk>\d+)/$', BookDetail.as_view(), name='books_detail'),
    url(r'^books/update/(?P<pk>\d+)/$', BookUpdate.as_view(), name='books_update'),
    url(r'^books/delete/(?P<pk>\d+)/$', BookDelete.as_view(), name='books_delete'),

    # Languages
    url(r'^languages$', LanguageList.as_view(), name='languages_list'),
    url(r'^languages/new/$', LanguageCreate.as_view(), name='languages_create'),
    url(r'^languages/detail/(?P<pk>\d+)/$', LanguageDetail.as_view(), name='languages_detail'),
    url(r'^languages/update/(?P<pk>\d+)/$', LanguageUpdate.as_view(), name='languages_update'),
    url(r'^languages/delete/(?P<pk>\d+)/$', LanguageDelete.as_view(), name='languages_delete'),

    # Genres
    url(r'^genres$', GenreList.as_view(), name='genres_list'),
    url(r'^genres/new/$', GenreCreate.as_view(), name='genres_create'),
    url(r'^genres/detail/(?P<pk>\d+)/$', GenreDetail.as_view(), name='genres_detail'),
    url(r'^genres/update/(?P<pk>\d+)/$', GenreUpdate.as_view(), name='genres_update'),
    url(r'^genres/delete/(?P<pk>\d+)/$', GenreDelete.as_view(), name='genres_delete'),

    # Authors
    url(r'^authors$', AuthorList.as_view(), name='authors_list'),
    url(r'^authors/new/$', AuthorCreate.as_view(), name='authors_create'),
    url(r'^authors/detail/(?P<pk>\d+)/$', AuthorDetail.as_view(), name='authors_detail'),
    url(r'^authors/update/(?P<pk>\d+)/$', AuthorUpdate.as_view(), name='authors_update'),
    url(r'^authors/delete/(?P<pk>\d+)/$', AuthorDelete.as_view(), name='authors_delete'),

    # Reservations
    url(r'^reservations$', ReservationList.as_view(), name='reservations_list'),
    url(r'^reservations/new/$', ReservationCreate.as_view(), name='reservations_create'),
    url(r'^reservations/detail/(?P<uuid>[0-9a-f-]+)/$', ReservationDetail.as_view(), name='reservations_detail'),
    url(r'^reservations/update/(?P<uuid>[0-9a-f-]+)/$', ReservationUpdate.as_view(), name='reservations_update'),
    url(r'^reservations/delete/(?P<uuid>[0-9a-f-]+)/$', ReservationDelete.as_view(), name='reservations_delete'),
]