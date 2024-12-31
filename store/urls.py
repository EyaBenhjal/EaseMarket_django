from django.urls import path
from . import views 

urlpatterns = [
    path('',views.acceuil, name='acceuil'),
    path('about/',views.about, name='about'),
    path('connecter/',views.connecter_user, name='connecter'),#name hua action f html
    path('deconnecter/',views.deconnecter_user, name='deconnecter'),
    path('inscrire/',views.inscrire_user, name='inscrire'),
    path('produit/<int:pk>',views.produit, name='produit'),
    path('categorie/<str:foo>',views.categorie, name='categories'),

]