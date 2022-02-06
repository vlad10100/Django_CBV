from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import TemplateView 

from .models import Post 


class PostTemplateView(TemplateView):
    template_name = 'cbv/page_one.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        context["data"] = "Just to add something"
        return context
    