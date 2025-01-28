from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Charge un fichier HTML nommé index.html

import os

def login_view(request):
    print(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates/users/login.html'))
    return render(request, 'users/login.html')





def add_suspect(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        name = request.POST['name']
        description = request.POST['description']
        date_arrestation = request.POST['date_arrestation']
        lieu = request.POST['lieu']
        service = request.POST['service']
        photo = request.FILES.get('photo', None)


def ajout_suspect(request):  # C'est probablement comme ça que tu l'as nommée
    return render(request, 'ajouter_suspect.html')  # Charge un template pour ajouter un suspect

