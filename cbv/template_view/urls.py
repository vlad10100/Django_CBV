from django.urls import path 

from .views import PostTemplateView

app_name = 'template_view'
urlpatterns = [
    path('', PostTemplateView.as_view(), name='template_view'),
]
