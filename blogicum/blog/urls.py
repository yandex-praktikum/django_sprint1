from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('<slug:category_slug>/', views.category_posts, name='category_posts'),
    path('', views.index, name='index'),
]