import os
MAX_COLLABORATORS = 15

def read_file(filename):

    try:
        with open(filename, "r") as file:
            collaborators = [line.strip() for line in file]
            return collaborators[:MAX_COLLABORATORS]
    except:
        print(f"Error: El archivo '{filename}' no se a encontrado.")
        return []


def save_file(filename, colaboradores):
  
    with open(filename, "w") as file:
        for colaborador in colaboradores:
            file.write(f"{colaborador}\n")


def main():
    colaboradores = read_file("colaboradores.txt")
    while True:
        print("\nMenú de Colaboradores:")
        print("1. Mostrar colaboradores")
        print("2. Agregar colaborador")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            try:
                numero_colaboradores = int(input("¿Cuántos colaboradores desea ver?: "))
                if not (0 < numero_colaboradores <= 15):
                 numero_colaboradores = 15
            except ValueError:
                numero_colaboradores = 5

            if not colaboradores:
                print("La lista de colaboradores está vacía.")
            else:
                print("Colaboradores:")
                for i, colaborador in enumerate(colaboradores[:numero_colaboradores]):
                    print(f"{i + 1}. {colaborador}")

        elif opcion == "2":
            nombre_colaborador = input("Ingrese el nombre del colaborador: ")
            if len(colaboradores) >= MAX_COLLABORATORS:
                print(f"Error: Se ha alcanzado el límite máximo de {MAX_COLLABORATORS} colaboradores.")
                continue

            else:
                colaboradores.append(nombre_colaborador.strip().upper())
                print(f"Se ha agregado al colaborador '{nombre_colaborador.upper()}'.")

                save_file("colaboradores.txt", colaboradores)

if __name__ == "__main__":
    main()
