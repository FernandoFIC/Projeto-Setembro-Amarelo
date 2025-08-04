from django.shortcuts import render, redirect
from blog.form import ContatoForm

# Create your views here.
def index(request):
  

 return render (request, 'blog/template.html')

def contato(request):
 if request.method == 'POST':
    form = ContatoForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('contato')
    
 if request.method == 'GET':
    form = ContatoForm()
    return render (request, 'blog/contato.html', {'form': form})

def template(request):
 return render (request, 'blog/template.html')
