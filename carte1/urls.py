from django.urls import path
from . import views 

urlpatterns = [
    path('',views.cart_sum, name='cart_sum'),
    path('ajoute/',views.cart_ajouter, name='cart_ajouter'),
    path('delete/',views.cart_supprimer, name='cart_supprimer'),
    path('update/',views.cart_modifier, name='cart_modifier'),

]