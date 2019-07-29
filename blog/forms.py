from django import forms
from .models import Commentaire

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        # fields = ('__all__')
        fields = ('pseudo','email','contenu')
        
        
    def clean_contenu(self):
        
        contenu = self.cleaned_data['contenu']
        if "<" in contenu or ">" in contenu:
            raise forms.ValidationError("Votre commentaire semble contenir des balises HTML!")

        return contenu


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
