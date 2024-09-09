import random

class Arreglo:
    def __init__(self):
        self.a = []
        self.ma = 0

    def generaNumeros(self):
        self.a = [random.randint(1, 100) for _ in range(10)]
        self.ma = max(self.a)  # Calcula el número máximo en la lista
        print("Números generados correctamente.")

    def desplegarNumeros(self):
        if not self.a:
            print("Primero debes generar los números.")
        else:
            print("Números en el arreglo:", self.a)

    def desplegarNumerosInversos(self):
        if not self.a:
            print("Primero debes generar los números.")
        else:
            print("Números en orden inverso:", self.a[::-1])

    def calcularMayor(self):
        if not self.a:
            print("Primero debes generar los números.")
        else:
            print("El número mayor en el arreglo es:", self.ma)

def mostrarMenu():
    print("\nMenú de opciones:")
    print("1. Generar números")
    print("2. Desplegar números generados")
    print("3. Desplegar números en orden inverso")
    print("4. Calcular y mostrar el número mayor")
    print("5. Salir")

def main():
    arreglo = Arreglo()
    while True:
        mostrarMenu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            arreglo.generaNumeros()
        elif opcion == "2":
            arreglo.desplegarNumeros()
        elif opcion == "3":
            arreglo.desplegarNumerosInversos()
        elif opcion == "4":
            arreglo.calcularMayor()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
