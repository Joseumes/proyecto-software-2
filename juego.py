import random
import sys
def comparar(opcion1, opcion2):
    if opcion1 == opcion2:
        return 0  
    elif (opcion1 == "piedra" and opcion2 == "tijera") or \
         (opcion1 == "lapiz" and opcion2 == "piedra") or \
         (opcion1 == "tijera" and opcion2 == "papel"):
        return 1 
    else:
        return -1  

def main():
    if len(sys.argv) != 4:
        print("Uso: python juego.py <opcion1> <opcion2> <opcion3>")
        sys.exit(1)

    opciones_humano = [sys.argv[1].lower(), sys.argv[2].lower(), sys.argv[3].lower()]

    for opcion in opciones_humano:
        if opcion not in ["piedra", "papel", "tijera"]:
            print(f"Opción inválida: {opcion}. Las opciones válidas son 'piedra', 'papel' o 'tijera'.")
            sys.exit(1)

    opciones_programa = [random.choice(["piedra", "papel", "tijera"]) for _ in range(3)]


    puntaje_humano = 0
    puntaje_programa = 0

    for i in range(3):
        resultado = comparar(opciones_humano[i], opciones_programa[i])
        if resultado == 1:
            puntaje_humano += 1
        elif resultado == -1:
            puntaje_programa += 1

    if puntaje_humano > puntaje_programa:
        ganador = "Humano"
    elif puntaje_humano < puntaje_programa:
        ganador = "Programa"
    else:
        ganador = "Empate"

    print(f"El programa eligió: {' '.join(opciones_programa)}")
    print(f"Punteo: {puntaje_humano} - {puntaje_programa}")
    print(f"Ganador: {ganador}")

if __name__ == "__main__":
    main()