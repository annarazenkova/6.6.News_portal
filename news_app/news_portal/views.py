from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_in'] = datetime.utcnow()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news_one.html'
    context_object_name = 'news_one'
    pk_url_kwarg = 'id'



