def contar_palabras(texto):
  palabras = texto.split()
  numero_palabras = len(palabras)
  return numero_palabras

texto = input("Escribe la frase:")
numero_palabras = contar_palabras(texto)

print(f"El número de palabras en la cadena es: {numero_palabras}")