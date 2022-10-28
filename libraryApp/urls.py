from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book, name='book'),
    path('book/editBook/<int:pk>', views.editBook, name='editBook'),
    path('book/<int:pk>/detail/', views.detailBook, name='detailBook'),
    path('book/deleteBook/<int:pk>', views.deleteBook, name='deleteBook'),
    path('author/', views.author, name='author'),
    path('author/editAuthor/<int:pk>', views.editAuthor, name='editAuthor'),
    path('author/deleteAuthor/<int:pk>', views.deleteAuthor, name='deleteAuthor'),
    path('genre/', views.genre, name='genre'),
    path('genre/editGenre/<int:pk>', views.editGenre, name='editGenre'),
    path('genre/deleteGenre/<int:pk>', views.deleteGenre, name='deleteGenre'),
    path('publisher/', views.publisher, name='publisher'),
    path('publisher/editPublisher/<int:pk>', views.editPublisher, name='editPublisher'),
    path('publisher/deletePublisher/<int:pk>', views.deletePublisher, name='deletePublisher'),
]