from django.db import models

# Create your models here.
class Capteurs(models.Model):
    nomcapteur = models.CharField(max_length=100)
    emplacement = models.CharField(max_length=50, default='Emplacement à définir')

    def __str__(self):
        chaine = f" Capteur : '{self.nomcapteur}', emplacement : {self.emplacement}"
        return chaine

    def dico(self):
        return {"nomgroupe": self.nomcapteur, "emplacement": self.emplacement}

class Datas(models.Model):
    capteur = models.ForeignKey('Capteurs', on_delete=models.CASCADE, default=None)