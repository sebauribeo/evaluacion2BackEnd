from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book, name='book'),
    path('author/', views.author, name='author'),
    path('genre/', views.genre, name='genre'),
    path('publisher/', views.publisher, name='publisher'),
    path('editAuthor/', views.editAuthor, name='editAuthor'),
    path('editBook/', views.editBook, name='editBook'),
    path('editGenre/', views.editGenre, name='editGenre'),
    path('publisher/editPublish/', views.editPublish, name='editPublish'),
]