from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """Formulaire d'enregistrement utilisateur."""
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password1', 'password2']

class CustomUserChangeForm(UserChangeForm):
    """Formulaire de modification utilisateur."""
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role']
