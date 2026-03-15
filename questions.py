import random

dictionary = {
    "informatica": [
        "python",
        "programa",
        "variable",
        "funcion",
        "bucle",
        "cadena",
        "entero",
        "lista",
    ],
    "hardware": ["teclado", "mouse", "procesador"],
}

print("¡Bienvenido al Ahorcado!")
print()

choice = input(
    f"Seleccione una de las siguientes categorias: {', '.join(dictionary.keys())}. "
)
print()

word = random.choice(dictionary[choice])
guessed = []

attempts = 6

score = 0


while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        score += 6
        print(f"¡Ganaste! Tu puntaje es {score}.")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")

    if not letter.isalpha() or len(letter) != 1:
        print("Entrada no válida.")
        continue
    elif letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        score -= 1
        print("Esa letra no está en la palabra.")

    print()

else:
    score = 0
    print(f"¡Perdiste! La palabra era: {word}. Tu puntaje es {score}.")
