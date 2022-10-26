from django import forms

from libraryApp.models import Author, Book, Genre, Publisher


# .objects.values_list('name', flat=True).order_by('id')
class BookForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(
    attrs={
        'class': 'form-control mt-2',
        'type': 'text',
        'placeholder': 'Ingresa el nombre del producto'
        }
    ))
    autor = forms.ModelChoiceField(queryset = Author.objects.all(), empty_label='Selecciona un autor') 
    genero = forms.ModelChoiceField(queryset = Genre.objects.all(), empty_label='Selecciona un genero')
    publicador = forms.ModelChoiceField(queryset = Publisher.objects.all(), empty_label='Selecciona una publicacion ')

    class Meta:
        model = Book
        fields = ('nombre', 'autor', 'genero', 'publicador')


class AuthorForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(
    attrs={
        'class': 'form-control mt-2',
        'type': 'text',
        'placeholder': 'Ingresa el nombre del producto'
        }
    ))
    fecha_cumpleaños = forms.DateField(widget=forms.DateInput(
    attrs={
        'class': 'form-control mt-2',
        'type': 'text',
        'placeholder': 'Ingresa el nombre del producto'
        }
    ))
    class Meta:
        model = Author
        fields = ('nombre', 'fecha_cumpleaños')

class GenreForm(forms.ModelForm):

    nombre = forms.CharField(widget=forms.TextInput(
    attrs={
        'class': 'form-control mt-2',
        'type': 'text',
        'placeholder': 'Ingresa el nombre del producto'
        }
    ))

    class Meta:
        model = Genre
        fields = ('nombre',)

class PublisherForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(
    attrs={
        'class': 'form-control mt-2',
        'type': 'text',
        'placeholder': 'Ingresa el nombre del producto'
        }
    ))

    class Meta:
        model = Publisher
        fields = ('nombre',)