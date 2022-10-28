from django.http import HttpResponse
def helloWorld(request):
	return HttpResponse("<b><h2><center>Hello World</center></h2></b>")

	
	
	
from django.shortcuts import render 

def tal(request): 
    return render(request,'page.html')
	
	
def bonjour(request):
    return render(request,'nom_prenom.html')


def welcome(request):
    prenom_nom = request.GET['prenom_nom'] #pour recupérer le nom et prénom
    print(prenom_nom) #C'est où qu'on peut voir notre print ?
    return render(request,'affiche.html', {'fullname':prenom_nom}) # Le disctionnaire qui nous permet d'envoyer les information à l'utilisateur
    
def compteur(request):
    return render(request,'compteur.html')

def affiche(request):
    compteur_mots = request.GET['texte']
    liste_mots = compteur_mots.split()
    print(compteur_mots)
    return render(request,'affiche.html', {'compteur_mots': compteur_mots, 'liste_mots': len(liste_mots)})




	
	
# python manage.py runserver
	
	
