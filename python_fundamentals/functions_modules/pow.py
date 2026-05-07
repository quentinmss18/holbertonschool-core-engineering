#!/usr/bin/env python3

def pow(a, b):
    """
    Calcule a puissance b manuellement à l'aide d'une boucle.
    """
    # Cas particulier : tout nombre à la puissance 0 vaut 1
    if b == 0:
        return 1
    
    # Si l'exposant est négatif
    if b < 0:
        # On peut gérer les négatifs ainsi, ou retourner 0 selon l'exercice
        # Pour rester simple et conforme au standard :
        return 1 / pow(a, -b)

    result = 1
    # On multiplie 'result' par 'a', 'b' fois
    for i in range(b):
        result *= a
        
    return result
