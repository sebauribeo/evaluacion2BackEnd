# Generated by Django 4.1.2 on 2022-10-27 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0006_book_author_book_genre_book_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='author', to='libraryApp.author'),
        ),
    ]
