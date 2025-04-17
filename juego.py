import random

def comparar(opcion1, opcion2):
    if opcion1 == opcion2:
        return 0  
    elif (opcion1 == "piedra" and opcion2 == "tijera") or \
         (opcion1 == "papel" and opcion2 == "piedra") or \
         (opcion1 == "tijera" and opcion2 == "papel"):
        return 1 
    else:
        return -1  

