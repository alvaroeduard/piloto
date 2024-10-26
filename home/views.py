from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def sobre(request):
    return render(request,'sobre.html')

def contato(request):
    return render(request,'contato.html')

