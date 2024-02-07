from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def about(request: HttpResponse) -> HttpRequest:
    """Страница с описание проекта."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request: HttpResponse) -> HttpRequest:
    """Страница с правилами проекта."""
    template = 'pages/rules.html'
    return render(request, template)
