from django.shortcuts import render
from . forms import CapteursForm
from . import models
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    cList = list(models.Capteurs.objects.all())
    return render(request, 'webcollecte/index.html', {"Liste": cList})

def ajout(request):
    if request.method == "POST":
        form = CapteursForm(request)
        if form.is_valid():
            capteur = form.save()
            return render(request,"webcollecte/affiche.html",{"Capteur" : capteur})
        else:
            return render(request,"webcollecte/ajout.html",{"form": form})
    else:
        form = CapteursForm()
        return render(request,"webcollecte/ajout.html",{"form" : form})

def traitement(request):
    cform = CapteursForm(request.POST)
    if cform.is_valid():
        capteur=cform.save()
        return HttpResponseRedirect("/webcollecte/")
    else:
        return render(request, 'webcollecte/ajout.html', {'form':cform})

def affiche(request, id):
    capteur=models.Capteurs.objects.get(pk=id)
    return render(request, "webcollecte/affiche.html", {"Capteur":capteur})

def update(request, id):
    capteur=models.Capteurs.objects.get(pk=id)
    cform = CapteursForm(capteur.dico())
    return render(request, 'webcollecte/update.html', {"form":cform, "id":id})

def delete(request, id):
    capteur = models.Capteurs.objects.get(pk=id)
    capteur.delete()
    return HttpResponseRedirect("/webcollecte/")

def traitementupdate(request, id):
    cform=CapteursForm(request.POST)
    if cform.is_valid():
        capteur = cform.save(commit=False)
        capteur.id=id;
        capteur.save()
        return HttpResponseRedirect('/webcollecte/')
    else:
        return render(request, "webcollecte/update.html", {"form":cform, "id":id})