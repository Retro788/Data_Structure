import random

def generar_matriz(matriz, fila=0):
    if fila >= 4:
        return matriz
    matriz.append([random.randint(1, 100) for _ in range(4)])
    return generar_matriz(matriz, fila + 1)

def desplegar_matriz(matriz, fila=0):
    if fila >= len(matriz):
        return
    print(matriz[fila])
    desplegar_matriz(matriz, fila + 1)

def desplegar_fila(matriz, fila, i=0):
    if fila >= len(matriz) or i >= len(matriz[0]):
        print()
        return
    print(matriz[fila][i], end=' ')
    desplegar_fila(matriz, fila, i + 1)

def desplegar_columna(matriz, columna, fila=0):
    if fila >= len(matriz):
        return
    print(matriz[fila][columna])
    desplegar_columna(matriz, columna, fila + 1)

def diagonal_principal(matriz, indice=0):
    if indice >= len(matriz):
        print()
        return
    print(matriz[indice][indice], end=' ')
    diagonal_principal(matriz, indice + 1)

def diagonal_inversa(matriz, indice=0):
    if indice >= len(matriz):
        print()
        return
    print(matriz[indice][len(matriz) - indice - 1], end=' ')
    diagonal_inversa(matriz, indice + 1)

def suma_elementos(matriz, fila=0, col=0, suma=0):
    if fila >= len(matriz):
        return suma
    if col >= len(matriz[0]):
        return suma_elementos(matriz, fila + 1, 0, suma)
    return suma_elementos(matriz, fila, col + 1, suma + matriz[fila][col])

def contar_mayores_50(matriz, fila=0, col=0, count=0):
    if fila >= len(matriz):
        return count
    if col >= len(matriz[0]):
        return contar_mayores_50(matriz, fila + 1, 0, count)
    if matriz[fila][col] > 50:
        count += 1
    return contar_mayores_50(matriz, fila, col + 1, count)

def fila_menor_elemento(matriz, fila=0, col=0, menor=float('inf'), fila_menor=-1):
    if fila >= len(matriz):
        return fila_menor
    if col >= len(matriz[0]):
        return fila_menor_elemento(matriz, fila + 1, 0, menor, fila_menor)
    if matriz[fila][col] < menor:
        menor = matriz[fila][col]
        fila_menor = fila
    return fila_menor_elemento(matriz, fila, col + 1, menor, fila_menor)

def menu():
    matriz = []
    while True:
        print("\nMenú de Operaciones con Matrices:")
        print("1. Generar una matriz aleatoria de 4x4")
        print("2. Desplegar la matriz")
        print("3. Desplegar una fila específica")
        print("4. Desplegar una columna específica")
        print("5. Desplegar la diagonal principal")
        print("6. Desplegar la diagonal inversa")
        print("7. Obtener la suma de todos los elementos")
        print("8. Contar cuántos elementos mayores a 50 hay")
        print("9. Indicar en qué fila se encuentra el dato menor")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            matriz = generar_matriz([])
            print("Matriz generada.")

        elif opcion == '2':
            if matriz:
                desplegar_matriz(matriz)
            else:
                print("Primero genera una matriz.")

        elif opcion == '3':
            if matriz:
                fila = int(input("Ingresa el número de la fila (0-3): "))
                if 0 <= fila < 4:
                    desplegar_fila(matriz, fila)
                else:
                    print("Número de fila inválido.")
            else:
                print("Primero genera una matriz.")

        elif opcion == '4':
            if matriz:
                columna = int(input("Ingresa el número de la columna (0-3): "))
                if 0 <= columna < 4:
                    desplegar_columna(matriz, columna)
                else:
                    print("Número de columna inválido.")
            else:
                print("Primero genera una matriz.")

        elif opcion == '5':
            if matriz:
                diagonal_principal(matriz)
            else:
                print("Primero genera una matriz.")

        elif opcion == '6':
            if matriz:
                diagonal_inversa(matriz)
            else:
                print("Primero genera una matriz.")

        elif opcion == '7':
            if matriz:
                print("La suma de todos los elementos es:", suma_elementos(matriz))
            else:
                print("Primero genera una matriz.")

        elif opcion == '8':
            if matriz:
                print("Cantidad de elementos mayores a 50:", contar_mayores_50(matriz))
            else:
                print("Primero genera una matriz.")

        elif opcion == '9':
            if matriz:
                print("La fila del elemento menor es:", fila_menor_elemento(matriz))
            else:
                print("Primero genera una matriz.")

        elif opcion == '0':
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

menu()
