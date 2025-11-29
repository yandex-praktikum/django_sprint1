from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'about.html')

def rules(request):
    return render(request, 'rules.html')