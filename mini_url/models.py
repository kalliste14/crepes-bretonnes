from django.db import models
from django.utils import timezone

import random
import string

from django.utils.translation import ugettext_lazy as _

class Raccourci(models.Model):
    URLField = models.URLField(unique=True, verbose_name = _("URL à réduire"))
    code = models.CharField(max_length=6, unique = True) 
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name=_("Date d'enregistrement"))
    pseudo = models.CharField(max_length=20, null=True, verbose_name = _("Pseudo"))
    nb_acces = models.IntegerField(default=0, verbose_name = _("Nombre d'accès à l'URL"))
    
    class Meta:
        verbose_name = _("Mini URL")
        verbose_name_plural = _("Minis URL")
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.code
  
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.generer(6)

        super(Raccourci, self).save(*args, **kwargs)
 
    def generer(self, nb_caracteres):
        caracteres = string.ascii_letters + string.digits
        aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]
    
        self.code = ''.join(aleatoire)
  

from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Raccourci)
def ma_fonction_de_suppression(sender, instance, **kwargs):
    print("Je passe dans ma fonction de suppression.")
    
    
post_delete.connect(ma_fonction_de_suppression, sender=Raccourci)
