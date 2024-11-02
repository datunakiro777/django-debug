from django.shortcuts import render

# Create your views here.
def django_toolbar(request):
    return render(request, 'index.html')