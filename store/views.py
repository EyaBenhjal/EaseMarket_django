from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit, Categories
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
# store/views.py
from store.models import Produit  # If the model is in the same app

from django.contrib.auth.forms import UserCreationForm  # Correct import

def categorie(request, foo):
    try:
        categorie = get_object_or_404(Categories, name=foo)
        
        produits = Produit.objects.filter(categories=categorie)  # Assurez-vous que `categories` est le bon champ

        return render(request, 'categorie.html', {'produits': produits, 'categorie': categorie})
    
    except Categories.DoesNotExist:
        messages.error(request, f"La catégorie '{foo}' n'existe pas.")
        return redirect('acceuil')
    
    except Exception as e:
        print(f"Erreur : {e}")
        messages.error(request, f"Une erreur inattendue s'est produite : {e}")
        return redirect('acceuil')



def produit(request, pk):
    produit = Produit.objects.get(id=pk)  
    return render(request, 'produit.html', {'produit': produit})

def acceuil(request):
    produits = Produit.objects.all()
    return render(request, 'acceuil.html', {'produits' : produits})

def about(request):
    return render(request, 'about.html', {})

def connecter_user(request):
    if request.method == "POST":
        nom = request.POST.get('nom', '').strip()  
        mots_de_passe = request.POST.get('mots_de_passe', '').strip()

        if not nom or not mots_de_passe:
            messages.error(request, "Veuillez remplir tous les champs.")
            return redirect('connecter')

        user = authenticate(request, username=nom, password=mots_de_passe)
        if user is not None:
            login(request, user)
            messages.success(request, "Connecté avec succès!")
            return redirect('acceuil')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            return redirect('connecter')
    else:
        # Affichage de la page de connexion
        return render(request, 'connecter.html', {})
def deconnecter_user(request):
    logout(request)
    messages.success(request,("Deconnecter avec succès"))
    return redirect('acceuil')

def inscrire_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Connexion de l'utilisateur
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "Inscription réussie! Bienvenue!")
            return redirect('connecter')
        else:
            messages.success(request, "Erreur d'authentification après l'inscription.")
            return redirect('inscrire')
        
    else:
        return render(request, 'inscrire.html', {'form': form})