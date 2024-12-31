
from django.shortcuts import render, get_object_or_404
from .carte1 import Carte1
from store.models import Produit
from django.http import JsonResponse

def cart_sum(request):
    cart = Carte1(request)
    cart_produits = cart.get_prods()
    quantities = cart.get_quants()
    quantity_range = range(1, 6)  # Ajout de la plage pour les quantités
    return render(request, "cart_sum.html", {
        "cart_produits": cart_produits,
        "quantities": quantities,
        "quantity_range": quantity_range  # Ajouté au contexte
    })

def cart_ajouter(request):
    cart = Carte1(request)  # Créez une instance de Carte1 pour accéder au panier

    if request.POST.get('action') == 'post':
        produit_id = request.POST.get('produit_id')
        produit_qty = request.POST.get('produit_qty')

        if produit_id and produit_qty:  # Vérifiez que les deux valeurs existent
            try:
                produit_id = int(produit_id)
                produit_qty = int(produit_qty)
                produit = get_object_or_404(Produit, id=produit_id)

                # Ajoutez le produit au panier
                cart.add(produit=produit, quantity=produit_qty)

                # Récupérez la quantité totale dans le panier
                cart_quantity = cart.__len__()

                # Retournez la quantité dans la réponse JSON
                return JsonResponse({'qty': cart_quantity}, status=200)

            except ValueError:
                return JsonResponse({'error': 'Quantité ou ID produit invalide'}, status=400)

        else:
            return JsonResponse({'error': 'Produit ID ou quantité manquante'}, status=400)

    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)    

# Fonction de suppression du produit dans le panier
def cart_supprimer(request, produit_id):
    if request.method == 'POST':
        # Vérifier si le produit existe dans le panier
        cart = Carte1(request)

        try:
            # Supprimer le produit du panier
            cart.delete(produit_id)

            # Réponse indiquant la suppression réussie
            return JsonResponse({'success': True, 'message': 'Produit supprimé du panier'}, status=200)

        except KeyError:
            return JsonResponse({'error': 'Produit non trouvé dans le panier'}, status=404)

    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


# View for updating the cart

def cart_modifier(request):
    if request.method == 'POST':
        # Récupérer les données envoyées par la requête
        data = json.loads(request.body)
        produit_id = data.get('produit_id')  # ID du produit
        produit_qty = data.get('produit_qty')  # Quantité du produit

        # Vérifier si les données sont valides
        if not produit_id or not produit_qty:
            return JsonResponse({'error': 'ID produit ou quantité manquante'}, status=400)

        try:
            produit_id = int(produit_id)
            produit_qty = int(produit_qty)
            produit = get_object_or_404(Produit, id=produit_id)

            # Récupérer le panier
            cart = Carte1(request)

            # Mettre à jour la quantité du produit dans le panier
            cart.update(produit=produit_id, quantity=produit_qty)

            # Récupérer la quantité totale du panier
            cart_quantity = cart.__len__()

            return JsonResponse({'success': True, 'qty': cart_quantity}, status=200)

        except ValueError:
            return JsonResponse({'error': 'Quantité ou ID produit invalide'}, status=400)
    
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)