from django.test import TestCase

from django.urls import reverse
from mini_url.models import Raccourci

import random
import string

def generer(nb_caracteres):
    caracteres = string.ascii_letters + string.digits
    aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]
    code = ''.join(aleatoire)
    return code
    
def creer_url():
    mini = Raccourci(URLField="http://foo.bar",code=generer(6), pseudo="Maxime")
    mini.save()
    return mini

class MiniURLTests(TestCase):
    def test_liste(self):
        """ Vérifie si une URL sauvegardée est bien affichée """

        mini = creer_url()
        reponse = self.client.get(reverse('accueil'))

        self.assertEqual(reponse.status_code, 200)
        self.assertContains(reponse, mini.URLField)
        self.assertQuerysetEqual(reponse.context['raccourcis'], [repr(mini)])
        
    def test_nouveau_redirection(self):
        """ Vérifie la redirection d'un ajout d'URL """
        data = {
            'URLField': 'http://www.djangoproject.com',
            'pseudo': 'Jean Dupont',
        }

        reponse = self.client.post(reverse('creer_raccourci'), data)
        self.assertEqual(reponse.status_code, 302)
        self.assertRedirects(reponse, reverse('accueil'))
        

    def test_nouveau_ajout(self):
        """
        Vérifie si après la redirection l'URL ajoutée est bien dans la liste
        """
        data = {
            'URLField': 'http://www.crepes-bretonnes.com',
            'pseudo': 'Amateur de crêpes',
        }

        reponse = self.client.post(reverse('creer_raccourci'), data, follow=True)
        self.assertEqual(reponse.status_code, 200)
        self.assertContains(reponse, data['URLField'])
    
