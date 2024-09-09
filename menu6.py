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

    def desplegarNumerosInversosRecursivo(self, i=0):
        # Caso base: cuando el índice llega al tamaño del arreglo, termina la recursión
        if i == len(self.a):
            return
        # Llamada recursiva primero
        self.desplegarNumerosInversosRecursivo(i + 1)
        # Imprime el número después de la llamada recursiva para mostrar en orden inverso
        print(self.a[i], end=' ')

    def calcularMayorRecursivo(self, i=0, ma=None):
        # Si es la primera llamada, inicializamos 'ma' con el primer elemento del arreglo
        if ma is None:
            ma = self.a[0]
        
        # Caso base: cuando el índice llega al tamaño del arreglo, devuelve el mayor
        if i == len(self.a):
            return ma
        
        # Comparar el elemento actual con 'ma' y actualizar si es mayor
        if self.a[i] > ma:
            ma = self.a[i]
        
        # Llamada recursiva con el siguiente índice
        return self.calcularMayorRecursivo(i + 1, ma)

    def buscarNumeroIterativo(self, x):
        # Búsqueda iterativa usando el operador 'in'
        if x in self.a:
            print(f"El número {x} se generó.")
        else:
            print(f"El número {x} no se generó.")
    
    def buscarNumeroRecursivo(self, x, indice=0):
        # Caso base: si hemos llegado al final de la lista, devolvemos -1
        if indice == len(self.a):
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
    print("3. Desplegar números en orden inverso (recursivo)")
    print("4. Calcular y mostrar el número mayor (recursivo)")
    print("5. Buscar un número en el arreglo (iterativo)")
    print("6. Buscar un número en el arreglo (recursivo)")
    print("7. Calcular factorial de un número (clase Numero)")
    print("8. Calcular la suma de los elementos del arreglo (recursivo)")
    print("9. Salir")

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
            if not arreglo.a:
                print("Primero debes generar los números.")
            else:
                print("Números en orden inverso:")
                arreglo.desplegarNumerosInversosRecursivo()
                print()  # Para una nueva línea después de la salida
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
                    arreglo.buscarNumeroIterativo(x)
                except ValueError:
                    print("Por favor, ingresa un número válido.")
        elif opcion == "6":
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
        elif opcion == "7":
            try:
                n = int(input("Ingresa el número para calcular su factorial: "))
                if n < 0:
                    print("El factorial no está definido para números negativos.")
                else:
                    factorial = numero.factorial(n)
                    print(f"El factorial de {n} es: {factorial}")
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == "8":
            if not arreglo.a:
                print("Primero debes generar los números.")
            else:
                suma = arreglo.sumarElementosRecursivo()
                print(f"La suma de los elementos del arreglo es: {suma}")
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
