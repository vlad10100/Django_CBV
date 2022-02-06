from django.shortcuts import render
from django.db.models import F
from django.utils import timezone


from .models import Book

from django.views.generic import DetailView, ListView




class BookDetailView(DetailView):
    template_name = 'detail_view/book_detail.html'
    model = Book


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = Book.objects.filter(slug = self.kwargs.get('slug'))
        post.update(count=F('count') + 1)

        context['time'] = timezone.now()
        context['book'] = Book.objects.get(slug = self.kwargs.get('slug'))
                #context_object_name = 'book' >>>>> the same

        return context


class BookList(ListView):
    template_name = 'detail_view/book_list.html'
    queryset = Book.objects.all()
    context_object_name = 'books' # Iterable using ListView