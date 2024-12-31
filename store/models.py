#libreray pour l'image Pillow
from django.db import models
from datetime import datetime

# Product Category
class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'
# Client Model
class Client(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    mots_de_passe = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nom} {self.prenom}'

# Product Model
class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
#add sale
    is_sale = models.BooleanField(default=False)
    sale_prix = models.DecimalField(default=0,decimal_places=2, max_digits=6)
    def __str__(self):
        return self.nom

# Order Model
class Ordre(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    quantities = models.IntegerField(default=1)
    addresse = models.CharField(max_length=100, default='', blank=True)
    telephone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.produit.nom
