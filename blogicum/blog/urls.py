from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/<slug:category_slug>/', views.post_detail, name='post_detail'),  # Два параметра
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
]
