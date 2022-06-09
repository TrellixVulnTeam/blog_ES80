#  DetailView, mostra o detalhe da view
#  ListView, mostra uma lista com as views
from django.views.generic import DetailView, ListView

from .models import Post


class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
