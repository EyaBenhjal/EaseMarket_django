from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Adresse e-mail'
    }))
    nom = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Nom'
    }))
    prenom = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Prénom'
    }))

    class Meta:
        model = User
        fields = ('username', 'nom', 'prenom', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nom d\'utilisateur'
        self.fields['username'].label = ''
        self.fields['username'].help_text = (
            '<span class="form-text text-muted">'
            '<small>Requis. 150 caractères ou moins. Lettres, chiffres et @/./+/-/_ uniquement.</small>'
            '</span>'
        )

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Mot de passe'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = (
            '<ul class="form-text text-muted small">'
            '<li>Votre mot de passe ne doit pas ressembler à vos autres informations personnelles.</li>'
            '<li>Votre mot de passe doit contenir au moins 8 caractères.</li>'
            '<li>Votre mot de passe ne doit pas être un mot de passe couramment utilisé.</li>'
            '<li>Votre mot de passe ne doit pas être entièrement numérique.</li>'
            '</ul>'
        )

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmer le mot de passe'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = (
            '<span class="form-text text-muted">'
            '<small>Entrez le même mot de passe que précédemment, pour vérification.</small>'
            '</span>'
        )
