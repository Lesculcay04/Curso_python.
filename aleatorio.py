import random

def adivinar_numero():
  numero_aleatorio = random.randint(1, 10)

  intentos = 0

  while True:
    adivinanza = int(input("Adivina el número (entre 1 y 10): "))
    intentos += 1

    if adivinanza == numero_aleatorio:
      print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
      break
    elif adivinanza < numero_aleatorio:
      print("Demasiado bajo. Intenta de nuevo.")
    else:
      print("Demasiado alto. Intenta de nuevo.")

# Iniciar el juego
adivinar_numero()
