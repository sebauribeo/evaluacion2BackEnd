from django.shortcuts import get_object_or_404, redirect, render
from libraryApp.forms import AuthorForm, BookForm, GenreForm, PublisherForm
from libraryApp.models import Author, Book, Genre, Publisher


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
    return render(request, 'library/edit.html', {'form': form})


def detailBook(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/bookDetail.html', {'book': book})

def deleteBook(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request, {'book': book})

def author(request):
    allAuthor = Author.objects.all()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect('home')
    else:
        form = AuthorForm()

    context = {
        'form': form,
        'allAuthor': allAuthor
    }
    return render(request, 'library/author.html', context)


def editAuthor(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect('author')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'library/edit.html', {'form': form})


def deleteAuthor(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author')
    return render(request, {'author': author})




def genre(request):
    allGenre = Genre.objects.all()
    if request.method == 'POST':
        form = GenreForm(request.POST)
        print('LOG', form)
        if form.is_valid():
            genre = form.save(commit=False)
            genre.save()
            return redirect('home')
    else:
        form = GenreForm()

    context = {
        'form': form,
        'allGenre': allGenre
    }
    return render(request, 'library/genre.html', context)


def editGenre(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            genre = form.save(commit=False)
            genre.save()
            return redirect('genre')
    else:
        form = GenreForm(instance=genre)
    return render(request, 'library/edit.html', {'form': form})


def deleteGenre(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        genre.delete()
        return redirect('genre')
    return render(request, {'genre': genre})





def publisher(request):
    allPublish = Publisher.objects.all()
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            publisher = form.save(commit=False)
            publisher.save()
            return redirect('home')
    else:
        form = PublisherForm()

    context = {
        'form': form,
        'allPublish': allPublish
    }
    return render(request, 'library/publisher.html', context)

def editPublisher(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            publisher = form.save(commit=False)
            publisher.save()
            return redirect('publisher')
    else:
        form = PublisherForm(instance=publisher)
    return render(request, 'library/edit.html', {'form': form})


def deletePublisher(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.delete()
        return redirect('publisher')
    return render(request, {'publisher': publisher})
