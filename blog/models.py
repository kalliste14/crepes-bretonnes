from django.db import models
from django.utils import timezone

class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom
    
class Article(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)    
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de parution")

    is_visible = models.BooleanField(verbose_name="Article publié ?", default=False)
    
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
  
    class Meta:
        verbose_name = "article"
        ordering = ['date']
        permissions = (
            ("commenter_article", "Commenter un article"),
            ("marquer_article", "Marquer un article comme lu"),
        )        
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.titre
    
    def nb_commentaires_lies(self):
        """
        Renvoie le nombre de commentaires liés à l'article
        """
        return Commentaire.objects.filter(article=self.id, is_visible=True).count()
    

    def get_commentaires_lies(self):
        """
        Renvoie le nombre de commentaires liés à l'article
        """
        return Commentaire.objects.filter(article=self.id, is_visible=True).order_by('-date')



class Commentaire(models.Model):
    pseudo = models.CharField(max_length=42)
    email = models.EmailField()  
    contenu = models.TextField(null=False)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date")
    is_visible = models.BooleanField(verbose_name="Commentaire visible ?", default=True)    

    article = models.ForeignKey('Article', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "commentaire"
        ordering = ['date']

    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.contenu


from django.contrib.auth.models import User

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # La liaison OneToOne vers le modèle User
    site_web = models.URLField(blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    signature = models.TextField(blank=True)
    inscrit_newsletter = models.BooleanField(default=False)

    def __str__(self):
        return "Profil de {0}".format(self.user.username)
    
