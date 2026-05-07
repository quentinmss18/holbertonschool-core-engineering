#!/usr/bin/env python3

def uppercase(str):
    """
    Parcourt la chaîne et convertit chaque minuscule en majuscule
    en manipulant les valeurs ASCII avec ord() et chr().
    """
    result = ""
    for char in str:
        # On vérifie si le caractère est une minuscule
        if ord(char) >= 97 and ord(char) <= 122:
            # On soustrait 32 pour obtenir la majuscule, 
            # puis on transforme le nombre en caractère avec chr()
            result += chr(ord(char) - 32)
        else:
            # Si ce n'est pas une minuscule, on garde le caractère tel quel
            result += char
    
    # On imprime le résultat final suivi d'une nouvelle ligne
    print("{}".format(result))
