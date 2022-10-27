# Generated by Django 4.1.2 on 2022-10-27 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0005_remove_book_author_remove_book_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='libraryApp.author'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='libraryApp.genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ManyToManyField(to='libraryApp.publisher'),
        ),
    ]