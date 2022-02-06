from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin

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




# User access Mixin!!
class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return redirect('/detail/books/')


        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)
    




class DeleteView(UserAccessMixin, DeleteView): # without confirmation
    raise_exception = False
    permission_required = 'detail_view.delete_book'       # if there is no permission to delete, user will be redirected

    model = Book
    context_object_name = 'book'
    success_url = reverse_lazy('detail_view:book_list')

    def get_redirect_field_name(self):
        return reverse_lazy('detail_view:book_list')
