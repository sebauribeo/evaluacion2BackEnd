from django.shortcuts import get_object_or_404, redirect, render
from libraryApp.forms import AuthorForm, BookForm, GenreForm, PublisherForm

from libraryApp.models import Book


def home(request):
    books = Book.objects.all()
    return render(request, 'library/home.html', {'allBooks': books})

def book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('detailBook', pk = book.pk)
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


def editBook(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/editBook.html', {'form': form})


def detailBook(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/bookDetail.html', {'book': book})

def deleteBook(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request, 'Products/deleteProduct.html', {'book': book})
