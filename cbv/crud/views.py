from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DeleteView

from detail_view.models import Book

from .forms import BookForm

class AddBook(CreateView):
    template_name = 'crud/add_book.html'
    form_class = BookForm 
    success_url = reverse_lazy('detail_view:book_list')

class UpdateBook(UpdateView):
    template_name = 'crud/update_book.html'
    queryset = Book.objects.all()
    form_class = BookForm 
    success_url = reverse_lazy('detail_view:book_list')

class DeleteView(DeleteView): # without confirmation
    model = Book
    context_object_name = 'book'
    success_url = reverse_lazy('detail_view:book_list')

