from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('about-us/', about_us, name='about_us'),
    path('cooming-soon/', cooming_soon, name='cooming_soon'),
    path('help/', help, name='help'),
    path('howitworks/', howitworks, name='howitworks'),
    path('pricing/', pricing, name='pricing'),
    path('productpage/', productpage, name='productpage'),
    path('profile/', profile, name='profile'),
    path('article/', ArticleListView.as_view(), name="article_list"),
    path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name="article_edit"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/new/', ArticleCreateView.as_view(), name='article_new'),
]
