from django.shortcuts import redirect, render
from libraryApp.forms import AuthorForm, BookForm, GenreForm, PublisherForm

from libraryApp.models import Book, Publisher


def home(request):
    books = Book.objects.all()
    return render(request, 'library/home.html', {'allBooks': books})

def book(request):

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'library/book.html', {'form': form})

def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'library/author.html', {'form': form})

def genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.save(commit=False)
            genre = genre.id
            genre.save()
            return redirect('home')
    else:
        form = GenreForm()
    return render(request, 'library/genre.html', {'form': form})

def publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            publisher = form.save(commit=False)
            publisher.save()
            return redirect('home')
    else:
        form = PublisherForm()
    return render(request, 'library/publisher.html', {'form': form})

def editAuthor(request):
    return render(request, 'library/editAuthor')

def editBook(request):
    return render(request, 'library/editBook')

def editGenre(request):
    return render(request, 'library/editGenre')

def editPublish(request):
    return render(request, 'library/editPublish')
