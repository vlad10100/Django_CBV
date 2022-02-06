from django.urls import path 

from .views import BookDetailView, BookList

app_name = 'detail_view'

urlpatterns = [
    path('book/<slug:slug>/', BookDetailView.as_view(), name='book_detail'),
    path('books/', BookList.as_view(), name='book_list'),
]