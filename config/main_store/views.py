from django.shortcuts import render
from .models import Product_mini, Product_max
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView

def main_page(request):
    try:
        logged_in = request.session["email"]
        product_mini = Product_mini.objects.all()
        product_max = Product_max.objects.all()
        return render(request, 'index.html', {'product_min': product_mini, 'product_max': product_max,"ok": logged_in})
    except:
        return render(request, 'index.html')

def help(request):
    return render(request, 'help.html')

def about_us(request):
    return render(request, 'about_us.html')

def cooming_soon(request):
    return render(request, 'cooming_soon.html')

def howitworks(request):
    return render(request, 'howitworks.html')

def pricing(request):
    return render(request, 'pricing.html')

def productpage(request):
    return render(request, 'productpage.html')

# def productpage(request):
#     obj = Product_mini.objects.all()
#     context = {
#         'object': obj
#     }
#     return render(request, 'productpage.html')

def profile(request):
    return render(request, 'profile.html')

def error_404(request, exception):
    return render(request, '404.html')
def error_403(request, exception):
    return render(request, '404.html')

class ArticleListView(ListView):
    model = Product_mini, Product_max
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Product_mini, Product_max
    template_name = 'article_detail.html'
class ArticleUpdateView(UpdateView):
    model = Product_mini, Product_max
    fields = ('image','product_name', 'description','olchov','budget','price', 'material', 'status', 'kafolat',)
    template_name = 'article_edit.html'
    
class ArticleDeleteView(DeleteView):
    model = Product_mini, Product_max
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleCreateView(CreateView):
    model = Product_mini, Product_max
    template_name = 'article_new.html'
    fields = ('title','summary','body','photo',)


