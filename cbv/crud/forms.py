from django import forms 

from detail_view.models import Book


class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book 
        fields = ['title', 'author', 'genre', 'isbn', 'count']
