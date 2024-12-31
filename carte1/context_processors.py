from .carte1 import Carte1
#creation context processor pour travaill dans all cart

def carte1(request):
    return {'carte1':Carte1(request)}
