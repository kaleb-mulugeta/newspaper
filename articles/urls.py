from django.urls import path
from .views import ( ArticleListView, ArticleUpdateView, ArticleDetailView, ArticleDeleteView, ArticelCreateView)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='article_delete'),
    path('edit/<int:pk>', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('new', ArticelCreateView.as_view(), name='article_new'),
]
