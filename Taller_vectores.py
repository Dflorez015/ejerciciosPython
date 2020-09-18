# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:03:56 2020

@author: duvan
"""


def condicion(text):
    seguir = input(f"{text} Escriba True si desea seguir" +
                   ", si no escriba False: ").lower().strip()
    if seguir == "true":
        seguir = True
        return seguir
    elif seguir == "false":
        seguir = False
        return seguir
    else:
        print("Error: Ingrese True o False")
        condicion(text)


def primer_punto(lista):
    sumatoria = n_mayor = n_menor = 0
    productoria = 1
    for i in lista:
        sumatoria = sumatoria + i
        productoria = productoria * i
    lista = sorted(lista)
    n_menor = min(lista)
    n_mayor = max(lista)
    print(f"La sumatoria es de: {sumatoria}.\n" +
          f"La productoria es de: {productoria}.\n" +
          f"El mayor es: {n_mayor}.\n" +
          f"El menor es: {n_menor}.")


def primos(num):
    primo = False
    divs = 0
    for i in range(num):
        i = i + 1
        if num % i == 0:
            divs = divs + 1
    if divs == 2:
        primo = True
    return primo


def produc(num):
    productoria = 1
    for i in num:
        productoria = productoria * i
    return productoria


def punto_seis(lista):
    tamanio = int(len(lista))
    contador = 1
    for i in lista:
        if i != lista[tamanio-contador]:
            return False
        contador = contador + 1
    return True


# 1.
lista = [2, 4, 5, 7, 1]
sigue = True
while sigue:
    n = int(input("Digite un número: "))
    lista.append(n)
    sigue = condicion("¿Desea seguir digitando números?")
primer_punto(lista)

# 2.
pares = []
impares = []
primo = []
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sigue = True
while sigue:
    n = int(input("Digite un número: "))
    lista.append(n)
    sigue = condicion("¿Desea seguir digitando números?")
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
    if primos(i):
        primo.append(i)
print(f"Los números pares son: {pares}. \n" +
      f"Los número impares son: {impares}. \n" +
      f"Los números primos son: {primo}")

# 3.
lista = [2, 3, 5, 6, 7]
lista_2 = [4, 3, 2, 1, 8]
lista_suma = []
lista_resta = []
sigue = True
while sigue:
    n = int(input("Digite un número en la lista 1: "))
    lista.append(n)
    n = int(input("Digite un número en la lista 2: "))
    lista_2.append(n)
    sigue = condicion("¿Desea seguir digitando números?")
lista_suma = list(map(lambda x, z: x+z, lista, lista_2))
lista_resta = list(map(lambda x, z: x-z, lista, lista_2))
print(f"Lista de la suma de los dos vectores: {lista_suma}. \n" +
      f"Lista de la resta de los dos vectores: {lista_resta}.")

# 4.
lista = [1, 1, 1, 3, 4, 5, 5, 5, 6, 6]
lista_repe = {}
sigue = True
while sigue:
    n = int(input("Digite un número: "))
    lista.append(n)
    sigue = condicion("¿Desea seguir digitando números?")
for i in lista:
    lista_repe[i] = lista.count(i)
lista_repe = sorted(lista_repe.items(), key=lambda x: x[1], reverse=True)
for i, j in lista_repe:
    if j == lista_repe[0][1]:
        print(f"El número {i} se repite con un total de {j} veces")

# 5.
lista = [1, 11, 20, 7, 5]
tamanio = len(lista)
sigue = True
while sigue:
    n = int(input("Digite un número: "))
    tamanio = tamanio + 1
    lista.append(n)
    sigue = condicion("¿Desea seguir digitando números?")
    if tamanio % 2 != 0:
        sigue = True
        print("Es necesario que la lista tenga un tamaño par. El tamaño" +
              f" actual de la lista no es par ({tamanio})")
mitad = int(tamanio / 2)
productoria = produc(lista[:mitad])
sumatoria = sum(lista[mitad:])
print(f"La productoria de la primera mitad es: {productoria}.")
print(f"La sumatoria de la segunda mitad es: {sumatoria}.")

# 6.
lista = [3, 5, 7, 8, 7, 5, 3]
if punto_seis(lista):
    print(f"El vector: {lista} es simétrico.")
else:
    print(f"El vector: {lista} no es simétrico.")

# 7.
lista = [2, 3, 5, 6, 7]
lista_2 = [4, 3, 2, 1, 8]
union = set(lista + lista_2)
interc = []
dif_a = []
dif_b = []
for i, j in zip(lista, lista_2):
    if lista_2.count(i) >= 1:
        interc.append(i)
    else:
        dif_a.append(i)
    if lista.count(j) == 0:
        dif_b.append(j)
print(f"La unión de los dos vectores es: {union}")
print(f"La intercepción entre los dos vectores es: {interc}")
print("Los elementos del vector 'lista' que no están en 'lista_2'",
      f" son: {dif_a}")
print("Los elementos del vector 'lista_2' que no están en 'lista'",
      f" son: {dif_b}")
