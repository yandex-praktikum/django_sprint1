from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]