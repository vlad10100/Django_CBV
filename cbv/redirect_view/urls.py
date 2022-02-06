from django.urls import path 

from django.views.generic import RedirectView

from .views import RedirectToThisPost, PostPreLoadTaskView

app_name = 'redirect_view'

urlpatterns = [
    path('redirect/', RedirectView.as_view(url='https://www.instagram.com/'), name='instagram'),
    path('page/<int:pk>/', RedirectToThisPost.as_view(), name='redirect_page'),
    path('preload/<int:pk>/', PostPreLoadTaskView.as_view(), name='preload'),
]