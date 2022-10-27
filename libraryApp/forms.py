from django import forms

from libraryApp.models import Author, Book, Genre, Publisher


# .objects.values_list('name', flat=True).order_by('id')
class BookForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-2',
            'type': 'text',
            'placeholder': 'Ingresa el nombre del producto'
        }
    ))
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label='Selecciona el autor', widget=forms.Select(
        attrs={
            'class': 'form-select',
        }
    ))
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), empty_label='Seleciona el genero', widget=forms.Select(
        attrs={
            'class': 'form-select',
        }
    ))
    publisher = forms.ModelChoiceField(queryset=Publisher.objects.all(), empty_label='Selecciona el publicador', widget=forms.Select(
        attrs={
            'class': 'form-select',
        }
    ))

    class Meta:
        model = Book
        fields = ('name', 'author', 'genre', 'publisher')


class AuthorForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-2',
            'type': 'text',
            'placeholder': 'Ingresa el nombre del producto'
        }
    ))
    date_of_birth = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form-control mt-2',
            'type': 'text',
            'placeholder': 'Ingresa el nombre del producto'
        }
    ))

    class Meta:
        model = Author
        fields = ('name', 'date_of_birth')


class GenreForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-2',
            'type': 'text',
            'placeholder': 'Ingresa el nombre del producto'
        }
    ))

    class Meta:
        model = Genre
        fields = ('name',)


class PublisherForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-2',
            'type': 'text',
            'placeholder': 'Ingresa el nombre del producto'
        }
    ))

    class Meta:
        model = Publisher
        fields = ('name',)
