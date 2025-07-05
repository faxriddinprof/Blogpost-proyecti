from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class Basepageview(ListView):
    model = Post
    template_name = "home.html"


class Blogdetailview(DetailView):
    model = Post
    template_name = "detail_view.html"


class Blogcreateview(CreateView):
    model = Post
    template_name = "detail_new.html"
    fields = ["title", "author", "text"]


class Detailyangilash(UpdateView):
    model = Post
    template_name = "detail_yangilash.html"
    fields = ["title", "text"]


class Postdelete(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
