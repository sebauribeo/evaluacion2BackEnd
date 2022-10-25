from django.db import models

# Create your models here.


class Genre(models.Model):
    try:
        name = models.CharField(max_length=100, unique = True)

    except Exception as e:
        print('Modelo no creado: ', e)

class Author(models.Model):
    try:
        name = models.CharField(max_length=100, unique = True)
        date_of_birth = models.DateField()

    except Exception as e:
        print('Modelo no creado: ', e)

class Publisher(models.Model):
    try:
        name = models.CharField(max_length=100, unique = True)

    except Exception as e:
        print('Modelo no creado: ', e)


class Book(models.Model):
    try:
        name = models.CharField(max_length=100)
        author = models.ForeignKey(Author, on_delete=models.CASCADE, null = True)
        genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null = True)
        publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null = True)
    except Exception as e:
        print('Modelo no creado: ', e)