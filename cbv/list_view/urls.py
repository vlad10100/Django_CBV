from django.urls import path 

from .views import GenreListView

app_name = 'list_view'

urlpatterns = [
    path('<str:genre>/', GenreListView.as_view(), name='genre')

]