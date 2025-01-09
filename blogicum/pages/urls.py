from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('about.html', views.about, name='about'),
    path('rules.html', views.rules, name='rules'),
]
