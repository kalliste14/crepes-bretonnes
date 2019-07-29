# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, render_to_response
from django.views.generic import ListView, DetailView
from blog.models import Article, Categorie
from blog.forms import CommentaireForm, ConnexionForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

class LireArticle(DetailView):
    context_object_name = "article"
    model = Article
    template_name = "blog/lire.html"
    

class ArticleCategorieListView(ListView):
    model = Article
    template_name = "blog/accueil.html"
    context_object_name = "articles"
    paginate_by = 4
    
    def get_queryset(self):
        return Article.objects.filter(categorie__id=self.kwargs['id'])

class ArticleListView(ListView):
    model = Article
    template_name = "blog/accueil.html"
    context_object_name = "articles"
    paginate_by = 2
    
    queryset = Article.objects.filter(is_visible=True).order_by('-date')

    def get_context_data(self, **kwargs):
        # Nous récupérons le contexte depuis la super-classe
        context = super(ArticleListView, self).get_context_data(**kwargs)
        # Nous ajoutons la liste des catégories, sans filtre particulier
        context['categories'] = Categorie.objects.all()
        return context

def connexion(request):
    error = False
        
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur

                next_url = request.POST.get('next')
                if next_url !='':
                    return redirect(next_url)


            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'blog/connexion.html', locals())


def deconnexion(request):
    logout(request)
    #return redirect(reverse_lazy(connexion))
    return redirect(reverse_lazy('connexion'))

def dire_bonjour(request):

    from django.contrib import messages
    messages.debug(request,"C'est tout")
    messages.info(request, "Bonjour!")
    messages.success(request, "Succès")
    messages.warning(request,"Warning")
    messages.error(request, "Erreur")
    messages.set_level(request, messages.SUCCESS)
    messages.info(request, "Bonjour!")
    
    if request.user.is_authenticated:
        return HttpResponse("Salut, {0} !".format(request.user.username))
    return HttpResponse("Salut, anonyme.")

@login_required()
def suite(request):
    return HttpResponse("Tu es maintenant connecté. Tu peux donc voir le reste.")

from django.utils.translation import ugettext as _
from django.utils.translation import ungettext


def test_i18n(request):
    nb_chats = 2
    couleur = "blanc"
    chaine = _("J'ai un %(animal)s %(col)s.") % {'animal': 'chat', 'col': couleur}
    infos = ungettext(
        "… et selon mes informations, vous avez %(nb)s chat %(col)s !",
        "… et selon mes informations, vous avez %(nb)s chats %(col)ss !",
        nb_chats) % {'nb': nb_chats, 'col': couleur}


    return render(request, 'blog/test_i18n.html', locals())
