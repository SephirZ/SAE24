from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models



class CapteursForm(ModelForm):
    class Meta:
        model = models.Capteurs
        fields=('nomcapteur', 'emplacement')
        labels = {
            'nomcapteur' : _("Nom du capteur"),
            'emplacement' : _('Emplacement du capteur'),
        }