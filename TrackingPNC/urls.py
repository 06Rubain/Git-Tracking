from django.contrib import admin
from django.urls import path, include
from . import views  # Import des vues de TrackingPNC
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Routes pour django-allauth
    path('', views.home, name='home'),  # Route pour la page d'accueil
    path('login/', views.login_view, name='login'),  # Route pour le Login
]




urlpatterns = [
    path('ajouter/', views.ajout_suspect, name='ajouter_suspect'),  # Utilise le bon nom de la fonction
]

