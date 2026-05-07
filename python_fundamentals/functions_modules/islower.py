#!/usr/bin/python3

def islower(c):
    """
    Fonction qui vérifie si un caractère est en minuscule.
    Utilise la logique ASCII avec ord().
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
