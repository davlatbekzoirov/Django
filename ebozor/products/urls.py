from django.urls import path

from .views import *

urlpatterns = [
    path('products/', HomePageView.as_view(), name='home'),
    path('products/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('products/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('products/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('products/new/', ArticleCreateView.as_view(), name='article_new'),
    path('', ArticleListView.as_view(), name='article_list'),
]