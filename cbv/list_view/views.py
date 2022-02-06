from django.shortcuts import render

from detail_view.models import Book 

from django.views.generic import ListView


class GenreListView(ListView):
    template_name = 'list_view/genre_list.html'
    model = Book 
    context_object_name = 'books'
    paginate_by = 2 

    def get_queryset(self, *args, **kwargs):
        return Book.objects.filter(genre__icontains=self.kwargs.get('genre'))

