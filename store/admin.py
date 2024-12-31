from django.contrib import admin
from .models import Categories , Client, Produit, Ordre
admin.site.register(Categories)
admin.site.register(Client)
admin.site.register(Produit)
admin.site.register(Ordre)