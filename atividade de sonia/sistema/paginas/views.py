from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def projetos(request):
    return render(request, 'projetos.html')

def contato(request):
    return render(request, 'contato.html')