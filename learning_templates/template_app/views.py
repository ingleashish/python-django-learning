from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'template_app/index.html')

def other(request):
    return render(request, 'template_app/other.html')

def base(request):
    return render(request, 'template_app/base.html')

def relative_url(request):
    return render(request, 'template_app/relative_url.html')
