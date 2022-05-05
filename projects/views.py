from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def projects(request):
    msg = 'Hello, you are on projects page'
    return render(request, 'projects.html',{'msg':msg})

def project(request, pk):
    return render(request, 'single-project.html')