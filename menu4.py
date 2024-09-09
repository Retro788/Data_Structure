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

    def calcularMayorRecursivo(self, lista=None, indice=0):
        if lista is None:
            lista = self.a
        
        # Caso base: Si la lista tiene solo un elemento, ese es el mayor
        if len(lista) == 1:
            return lista[0]
        
        # Encuentra el mayor entre el primer elemento y el máximo del resto
        mayor_resto = self.calcularMayorRecursivo(lista[1:], indice + 1)
        return lista[0] if lista[0] > mayor_resto else mayor_resto

    def buscarNumeroRecursivo(self, x, indice=0):
        # Caso base: si hemos llegado al final de la lista, devolvemos -1
        if indice >= len(self.a):
            return -1
        
        # Si encontramos el número, devolvemos su índice
        if self.a[indice] == x:
            return indice
        
        # De lo contrario, seguimos buscando en el resto de la lista
        return self.buscarNumeroRecursivo(x, indice + 1)

    def sumarElementosRecursivo(self, indice=0):
        # Caso base: Si el índice alcanza la longitud de la lista, regresamos 0
        if indice == len(self.a):
            return 0
        # Llamada recursiva: suma el elemento actual con la suma del resto
        return self.a[indice] + self.sumarElementosRecursivo(indice + 1)


class Numero:
    def factorial(self, x):
        # Caso base: 0! = 1 y 1! = 1
        if x == 0 or x == 1:
            return 1
        # Llamada recursiva
        else:
            return x * self.factorial(x - 1)


def mostrarMenu():
    print("\nMenú de opciones:")
    print("1. Generar números")
    print("2. Desplegar números generados")
    print("3. Desplegar números en orden inverso")
    print("4. Calcular y mostrar el número mayor (recursivo)")
    print("5. Buscar un número en el arreglo (recursivo)")
    print("6. Calcular factorial de un número (clase Numero)")
    print("7. Calcular la suma de los elementos del arreglo (recursivo)")
    print("8. Salir")

def main():
    arreglo = Arreglo()
    numero = Numero()
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
            if not arreglo.a:
                print("Primero debes generar los números.")
            else:
                mayor = arreglo.calcularMayorRecursivo()
                print("El número mayor en el arreglo es:", mayor)
        elif opcion == "5":
            if not arreglo.a:
                print("Primero debes generar los números.")
            else:
                try:
                    x = int(input("Ingresa el número a buscar: "))
                    indice = arreglo.buscarNumeroRecursivo(x)
                    if indice == -1:
                        print(f"El número {x} no se encuentra en el arreglo.")
                    else:
                        print(f"El número {x} se encuentra en la posición {indice}.")
                except ValueError:
                    print("Por favor, ingresa un número válido.")
        elif opcion == "6":
            try:
                n = int(input("Ingresa el número para calcular su factorial: "))
                if n < 0:
                    print("El factorial no está definido para números negativos.")
                else:
                    factorial = numero.factorial(n)
                    print(f"El factorial de {n} es: {factorial}")
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == "7":
            if not arreglo.a:
                print("Primero debes generar los números.")
            else:
                suma = arreglo.sumarElementosRecursivo()
                print(f"La suma de los elementos del arreglo es: {suma}")
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
