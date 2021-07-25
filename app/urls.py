from django.urls import path

from .views import HomePageView, AboutPageView, BlogDetailView, BlogCreateView, BlogUpdateView, FormPageView, BlogDeleteView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('form/', FormPageView.as_view(), name='form'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', HomePageView.as_view(), name='home'),
]