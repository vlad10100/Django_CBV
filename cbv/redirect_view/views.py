from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.db.models import F


from django.views.generic import RedirectView, TemplateView

from template_view.models import Post 

class PostPreLoadTaskView(RedirectView):
    pattern_name = 'redirect_view:redirect_page'

    def get_redirect_url(self, *args, **kwargs):
        post = Post.objects.filter(pk=kwargs['pk'])
        post.update(count=F('count')+1)
        return super().get_redirect_url(*args, **kwargs)




class RedirectToThisPost(TemplateView):
    template_name = 'redirect_view/redirect_to_this_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(kwargs)
        context["posts"] = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        return context 

