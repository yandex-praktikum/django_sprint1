from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def rules(request):
    return render(request, 'rules.html')
