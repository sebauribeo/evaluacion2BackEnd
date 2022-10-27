from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book, name='book'),
    path('author/', views.author, name='author'),
    path('genre/', views.genre, name='genre'),
    path('publisher/', views.publisher, name='publisher'),
    path('book/editBook/<int:pk>', views.editBook, name='editBook'),
    path('book/<int:pk>/detail/', views.detailBook, name='detailBook'),
    path('book/deleteBook/<int:pk>', views.deleteBook, name='deleteBook'),
]