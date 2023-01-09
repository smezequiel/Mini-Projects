# A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista.
#  Finalizar al ingresar el número 0, el cual no debe guardarse.
# B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia.
#  Mostrar un mensaje si no es posible eliminar.
# C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
# D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado.
#  Imprimir esta nueva lista, iterando por ella.
# E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos,
# cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella.
#  Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)].

def menu():
    print("Menu")
    print("Opcion A: los numeros que ingrese se guardaran en una lista")
    print("Opcion B: para quitar un numero de la lista")
    print("Opcion C: la sumatoria de todos los numeros")
    print("Opcion D: nueva lista con numeros menores a un nuevo numero ingresado")
    print("Opcion E: tupla de cantidad de veces repetido un numero")
    print("Ingrese otra letra para salir: ")
    return input()

# ACLARACION: (ver video explicativo)
# PARA PROBAR CADA PARTE, HACERLO POR SEPARADO, ES DECIR, def A con sus valores por un lado y asi. NO TODAS LAS FUNCIONES JUNTAS


def A(lista_numeros):
    numero = int(input("Ingrese una serie de numeros, para finalizar 0: "))
    while numero != 0:
        lista_numeros.append(numero)
        numero = int(input("Ingrese un numero, para finalizar 0: "))

    return lista_numeros


def B(lista_numeros):
    eliminar = int(input("Ingrese el numero a eliminar: "))
    if eliminar in lista_numeros:
        lista_numeros.remove(eliminar)
    else:
        print("No se puede eliminar")

    return lista_numeros


def C(lista_numeros):
    suma = 0
    for num in lista_numeros:
        suma += num
    print("La suma total de los numeros de la lista es: ", suma)


def D(lista_numeros):
    nuevo_numero = int(input("Ingrese un nuevo numero: "))
    nueva_lista = list()
    for num in lista_numeros:
        if num < nuevo_numero:
            nueva_lista.append(num)

    for num in nueva_lista:
        # Si a este print le dejo (num) solo me va a devolver uno debajo del otro
        print(num, end=" ")


def E(lista_numeros):
    nueva_list2 = list()
    for num in lista_numeros:
        tupla = (num, lista_numeros.count(num))
        if tupla not in nueva_list2:          # Hago esto para que no me vuelva a repetir un numero, probar sin para ver
            nueva_list2.append((tupla))

    print(nueva_list2)


#!! Lo que fuimos haciendo aca es debajo de cada funcion agregarle distintas listas como para usarlas de ejemplo !! #
# Pero en teoria todas deberian funcionar juntas, por lo que a continuacion las vamos a unir cada una por separado. #
# PROGRAMA:

numeros = list()
while True:
    opcion = menu()
    if opcion.lower() == 'a':
        numeros = A(numeros)
    elif opcion.lower() == 'b':
        numeros = B(numeros)
    elif opcion.lower() == 'c':
        C(numeros)
    elif opcion.lower() == 'd':
        D(numeros)
    elif opcion.lower() == 'e':
        E(numeros)
    else:
        break

    print(f"La lista tiene estos valores: {numeros}")
