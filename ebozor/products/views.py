from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Product

class ArticleListView(ListView):
    model = Product
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Product
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ('productname','description')
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    template_name = 'article_new.html'
    fields = ('productname','description')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser

class HomePageView(TemplateView):
    template_name = 'home.html'