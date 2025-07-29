from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
 return render (request, 'blog/template.html')
def contato(request):
 return render (request, 'blog/contato.html')

def template(request):
 return render (request, 'blog/template.html')
 return render (request, 'blog/template.html')
