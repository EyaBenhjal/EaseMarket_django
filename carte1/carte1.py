
from store.models import Produit
class Carte1:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')

        # Create a session if not available
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, produit, quantity):
        produit_id = str(produit.id)
        produit_qty = int(quantity)

        # Add or update the product in the cart
        if produit_id in self.cart:
            self.cart[produit_id] += produit_qty
        else:
            self.cart[produit_id] = produit_qty

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        produit_ids = self.cart.keys()
        produits = Produit.objects.filter(id__in=produit_ids)
        return produits

    def get_quants(self):
        return self.cart

    def update(self, produit, quantity):
        produit_id = str(produit)
        produit_qty = int(quantity)

        # Update the product quantity in the cart
        if produit_id in self.cart:
            self.cart[produit_id] = produit_qty
        else:
            self.cart[produit_id] = produit_qty

        self.session.modified = True
        return self.cart  # Return the updated cart
    
    def delete(self, produit_id):
        produit_id = str(produit_id)
        if produit_id in self.cart:
            del self.cart[produit_id]  # Supprimer le produit du panier
            self.session.modified = True
            return True
        return False
