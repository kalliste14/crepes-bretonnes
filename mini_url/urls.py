 
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('<int:page>', views.accueil, name='accueil'),
    path('creer_raccourci', views.URLCreate.as_view(), name='creer_raccourci'),
    #path('modifier_raccourci/<int:pk>', views.URLUpdate.as_view(), name='modifier_raccourci'),
    path('modifier_raccourci/<str:code>', views.URLUpdate.as_view(), name='modifier_raccourci'),
    path('renvoiurl/<str:code>', views.renvoiurl, name='renvoiurl'),
    #path('supprimer_raccourci/<str:code>', views.supprimer_raccourci, name='supprimer_raccourci'),
    path('supprimer_raccourci/<str:code>', views.URLDelete.as_view(), name='supprimer_raccourci'),
]


