# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect, Http404, get_object_or_404, HttpResponseRedirect

from mini_url.models import Raccourci
from mini_url.forms import MiniURLForm

from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage

def accueil(request, page=1):
    """
    Une vue affichant toutes les redirections créées et leurs informations, triées par ordre descendant, de la redirection avec le plus d'accès vers celle en ayant le moins ;
    """
    raccourcis = Raccourci.objects.order_by('-nb_acces')
    paginator = Paginator(raccourcis , 2)  # 5 liens par page

    try:
        # La définition de nos URL autorise comme argument « page » uniquement 
        # des entiers, nous n'avons pas à nous soucier de PageNotAnInteger
        raccourcis = paginator.page(page)
    except EmptyPage:
        # Nous vérifions toutefois que nous ne dépassons pas la limite de page
        # Par convention, nous renvoyons la dernière page dans ce cas
        raccourcis = paginator.page(paginator.num_pages)
    
    return render(request, 'mini_url/accueil.html', locals())
    
    
def renvoiurl(request, code):
    """
    Une vue qui prend comme paramètre dans l'URL le code et redirige l'utilisateur vers l'URL longue
    """
    """raccourci = Raccourci.objects.get(code=code)
    except Raccourci.DoesNotExist:
        raise Http404("L'URL raccourcie n'existe pas")
    """
    raccourci = get_object_or_404(Raccourci, code=code)
    raccourci.nb_acces += 1
    raccourci.save()
    
    return redirect(raccourci.URLField)


class URLCreate(CreateView):
    model = Raccourci
    template_name = 'mini_url/creer_raccourci.html'
    form_class = MiniURLForm
    success_url = reverse_lazy(accueil)
    

class URLUpdate(UpdateView):
    model = Raccourci
    template_name = 'mini_url/creer_raccourci.html'
    form_class = MiniURLForm
    success_url = reverse_lazy(accueil)    

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return get_object_or_404(Raccourci, code=code)   
    
    def form_valid(self, form):
        self.object = form.save()
        # Envoi d'un message à l'utilisateur
        messages.success(self.request, "Votre profil a été mis à jour avec succès.")
        return HttpResponseRedirect(self.get_success_url())    
    
class URLDelete(DeleteView):
    model = Raccourci
    context_object_name = "mini_url"
    template_name = 'mini_url/supprimer.html'
    success_url = reverse_lazy(accueil)

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return get_object_or_404(Raccourci, code=code)    
