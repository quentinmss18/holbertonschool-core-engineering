#!/usr/bin/env python3

def print_last_digit(number):
    """
    Récupère, affiche et retourne le dernier chiffre d'un nombre.
    Le chiffre retourné est toujours positif.
    """
    # On prend la valeur absolue pour gérer les nombres négatifs
    # puis le modulo 10 pour isoler le dernier chiffre
    last_digit = abs(number) % 10
    
    # On affiche le chiffre sans retour à la ligne automatique (optionnel selon le testeur)
    # ou simplement avec print standard si le testeur attend un saut de ligne
    print("{}".format(last_digit), end="")
    
    # On retourne la valeur
    return last_digit
