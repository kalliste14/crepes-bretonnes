from django.urls import path
from django.views.generic import TemplateView, ListView
from . import views
from .models import Article
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('<int:id>',  views.ArticleCategorieListView.as_view(), name="blog_categorie"), 
    path('',  views.ArticleListView.as_view(), name="accueil_blog"), 
    path('article/<int:pk>', views.LireArticle.as_view(), name='lire'),
    path('faq', TemplateView.as_view(template_name='blog/faq.html')),
    #path('connexion', views.connexion, name='connexion'),
    path('connexion', auth_views.LoginView.as_view(template_name='blog/connexion.html'), name='connexion'),
    #path('deconnexion', views.deconnexion, name='deconnexion'),
    path('deconnexion', auth_views.LogoutView.as_view(next_page='connexion'), name='deconnexion'),
    path('bonjour', views.dire_bonjour, name='bonjour'),
    path('suite', views.suite, name='suite'),
    path('test_i18n', views.test_i18n, name='test_i18n'),
]
