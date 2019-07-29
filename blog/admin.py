from django.contrib import admin
from django.utils.text import Truncator

from blog.models import Categorie, Article, Commentaire

class ArticleAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'categorie', 'auteur', 'date', 'apercu_contenu', 'is_visible')
    list_filter    = ('auteur','categorie', )
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('titre', 'contenu')
    prepopulated_fields = {'slug': ('titre', ), }   
    fieldsets = (
    # Fieldset 1 : meta-info (titre, auteur…)
   ('Général', {
        'classes': ['collapse',],
        'fields': ('titre', 'auteur', 'categorie','slug','is_visible')
    }),
    # Fieldset 2 : contenu de l'article
    ('Contenu de l\'article', {
       'classes': ['collapse',],
       'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
       'fields': ('contenu', )
    }),
)

    def apercu_contenu(self, article):
        """ 
        Retourne les 40 premiers caractères du contenu de l'article, 
        suivi de points de suspension si le texte est plus long. 
        """
        return Truncator(article.contenu).chars(40, truncate='...')

    # En-tête de notre colonne
    apercu_contenu.short_description = 'Aperçu du contenu'


class CommentaireAdmin(admin.ModelAdmin):
    list_display   = ('pseudo', 'article_titre', 'date', 'apercu_contenu', 'is_visible')
    list_filter    = ('article', )
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('contenu',)   
    # fields = ('auteur', 'article_lie', 'date', 'apercu_contenu', 'is_visible')

    def apercu_contenu(self, commentaire):
        """ 
        Retourne les 40 premiers caractères du contenu du commentaire, 
        suivi de points de suspension si le texte est plus long. 
        """
        return Truncator(commentaire.contenu).chars(40, truncate='...')

    # En-tête de la colonne
    apercu_contenu.short_description = 'Description'
    
    def article_titre(self, commentaire):
        """ 
        Retourne les 40 premiers caractères du contenu de l'article, 
        suivi de points de suspension si le texte est plus long. 
        """
        return Truncator(commentaire.article.titre).chars(40, truncate='...')

    article_titre.short_description = 'Article'

admin.site.register(Categorie)
admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Article, ArticleAdmin)

