from django.urls import path

from .views import AddBook, UpdateBook, DeleteView


app_name = 'crud'

urlpatterns = [
    
    path('add/', AddBook.as_view(), name='add_book'),
    path('update/<slug:slug>/', UpdateBook.as_view(), name='update_book'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete_book'),
]
