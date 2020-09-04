# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 02:09:03 2020

@author: duvan
"""
# 1.


def color_func(num):
    if(num == 1 or num == 2):
        print("La calcomanía es de color: amarillo")
    elif(num == 3 or num == 4):
        print("La calcomanía es de color: rosa")
    elif(num == 5 or num == 6):
        print("La calcomanía es de color: rojo")
    elif(num == 7 or num == 8):
        print("La calcomanía es de color: verde")
    else:
        print("La calcomanía es de color: azul")


n = int(input("Digite el número de carros: "))
w = 0
while w < n:
    placa = input('Ingrese la placa: ')
    for p in placa[len(placa)-1]:
        color_func(int(p))
    w = w + 1


# 2. Escogí las jirafas (15 muestras)
jirafas = [1, 5, 3, 2, 1, 6, 0, 5, 1, 3, 4, 2, 6, 1, 3]
categorias = [0, 0, 0]
for i in jirafas:
    if(i >= 0 and i <= 1):
        categorias[0] = categorias[0] + 1
    if(i > 1 and i < 3):
        categorias[1] = categorias[1] + 1
    if(i >= 3):
        categorias[2] = categorias[2] + 1
print("En la categoría '0 a 1 año' hay: ",
      categorias[0]*100/len(jirafas), "%")
print("En la categoría 'de mas de 1 año y menos de 3' hay: ",
      categorias[1]*100/len(jirafas), "%")
print("En la categoría 'de 3 o mas años' hay: ",
      categorias[2]*100/len(jirafas), "%")


# 3.
n = int(input("Digite el número de trabajadores: "))
w = 0
while w < n:
    tiempo_trabajo = int(
        input(f"Ingrese las horas de laburo del trabajador {w+1}:"))
    if(tiempo_trabajo <= 40):
        print(f"Al trabajador se le debe de pagar: ${tiempo_trabajo*20}")
    else:
        extras = tiempo_trabajo - 40
        print(f"Al trabajador se le debe de pagar: ${800+(extras*25)}")
    w = w + 1


# 4.
hombres = [65, 89, 35, 54, 65, 32, 49, 28, 36, 47, 21, 24]
mujeres = [67, 23, 54, 39, 24, 26, 57, 68, 84, 76, 37, 64]
alumnos = [14, 15, 13, 15, 18, 14, 12, 16, 15, 14, 17, 16]
promedios = [0, 0, 0]
for i in hombres:
    promedios[0] = promedios[0] + i
for i in mujeres:
    promedios[1] = promedios[1] + i
for i in alumnos:
    promedios[2] = promedios[2] + i
print("El promedio de la edad de los hombres es de:",
      promedios[0]/len(hombres))
print("El promedio de la edad de las mujeres de:",
      promedios[1]/len(mujeres))
print("El promedio de la edad de los alumnos es de:",
      promedios[2]/len(alumnos))


# 5.
n = int(input("Ingrese la cantidad de números que desee ingresar: "))
w = 0
numeros = []
while w < n:
    num = int(input("Digite un número: "))
    numeros.append(num)
    w = w + 1
numeros.sort()
print(f"El menor valor del cojunto es: {numeros[0]}")


# 6.
w = 0
while w < 5:
    ultimo_peso = int(
        input("Digite el peso de la última vez que se reunieron: "))
    pesos = []
    promedio = 0
    c = 0
    while c < 10:
        peso = int(input(f"Digite el peso dado en la báscula {c+1}: "))
        pesos.append(peso)
        c = c + 1
    for i in pesos:
        promedio = promedio + i
    promedio = promedio / 10
    print(f"El integrante número {w+1} pesa en promedio: {promedio}kg")
    estado = promedio - ultimo_peso
    if(estado < 0):
        print(
            f"De modo tal que ha bajado: {estado}kg",
            f" desde la última vez: {ultimo_peso}")
    else:
        print(f"De modo tal que ha subido: {estado}kg",
              f" desde la última vez: {ultimo_peso}")
    w = w + 1


# 7.
w = 1
total = 0
while w == 1:
    precio = int(input("Ingrese el valor del artículo: "))
    total = total + precio
    w = int(
        input("¿Desea seguir agregando articulos al carrito?: (Si=1, No=0): "))
print(f"El total a pagar por la compra es de: {total} pesos.")


# 8.
w = 1
descuentos = [0, 0, 0, 0, 0]
while w == 1:
    edad = int(input("Ingrese la edad de la persona: "))
    if(edad >= 5 and edad <= 14):
        descuentos[0] = descuentos[0] + 1
    elif(edad >= 15 and edad <= 19):
        descuentos[1] = descuentos[1] + 1
    elif(edad >= 20 and edad <= 45):
        descuentos[2] = descuentos[2] + 1
    elif(edad >= 46 and edad <= 65):
        descuentos[3] = descuentos[3] + 1
    elif(edad >= 66):
        descuentos[4] = descuentos[4] + 1
    else:
        print("No tiene la edad suficiente para entrar al teatro.")
    w = int(input("¿Desea seguir atendiendo clientes?: (Si=1, No=0): "))
print("En la categoria de niños '5-14 años' hubo:",
      f" {descuentos[0]} descuentos.")
print("En la categoria de niños '15-19 años' hubo:",
      f" {descuentos[1]} descuentos.")
print("En la categoria de niños '20-45 años' hubo:",
      f" {descuentos[2]} descuentos.")
print("En la categoria de niños '46-65 años' hubo:",
      f" {descuentos[3]} descuentos.")
print("En la categoria de niños 66 años en adelante hubo:",
      f" {descuentos[4]} descuentos.")


# 9. Coloqué solo dos trabajadores para no hacerlo extenso
w = 0
ventas = []
comision = []
while w < 2:
    vendido = int(input("Ingrese la cantidad que vendió anualmente: "))
    if(vendido <= 20000000):
        ventas.append(vendido)
        comision.append(vendido*0.1)
    elif(vendido > 20000000 and vendido < 40000000):
        ventas.append(vendido)
        comision.append(vendido*0.15)
    elif(vendido >= 40000000 and vendido < 80000000):
        ventas.append(vendido)
        comision.append(vendido*0.2)
    elif(vendido >= 80000000 and vendido < 160000000):
        ventas.append(vendido)
        comision.append(vendido*0.25)
    else:
        ventas.append(vendido)
        comision.append(vendido*0.3)
    w = w + 1
for i, ic in zip(ventas, comision):
    print(f"El vendedor vendió: {i}, y su comisión es de: {ic}")


# 10.
votos = 0
voto_candidato = [0, 0, 0]
bandera = True
while votos != 50000:
    while voto_candidato[0] > 50000 or bandera:
        voto_candidato[0] = int(
            input("Ingrese la cantidad de votos del candidato 1: "))
        if(voto_candidato[0] >= 0):
            bandera = False
    bandera = True
    while voto_candidato[1] > 50000 or bandera:
        voto_candidato[1] = int(
            input("Ingrese la cantidad de votos del candidato 2: "))
        if(voto_candidato[1] >= 0):
            bandera = False
    bandera = True
    while voto_candidato[2] > 50000 or bandera:
        voto_candidato[2] = int(
            input("Ingrese la cantidad de votos del candidato 3: "))
        if(voto_candidato[2] >= 0):
            bandera = False
    votos = voto_candidato[0] + voto_candidato[1] + voto_candidato[2]
    if(votos != 50000):
        print("Por favor ingrese bien la cantidad",
              " de votos de cada participante, ya que ",
              f"el total de votos es {votos}, y no 50000")
        votos = 0
        bandera = True
voto_candidato.sort(reverse=True)
empate = [0]
for i in voto_candidato:
    if(voto_candidato.count(i) != 1):
        empate.append(i)
if(len(empate) > 1):
    if(voto_candidato[0] == empate[1]):
        print(f"Hubo un empate de {voto_candidato[0]}",
              f"votos por parte de los dos primeros",
              f"y un perdedor con {voto_candidato[2]}")
    elif(len(empate) == 3):
        print(f"Hubo un ganador con {voto_candidato[0]} votos y",
              f"un empate con {empate[1]} votos")
    elif(len(empate) == 4):
        print(f"Hubo un empate con {empate[1]} votos")
else:
    print(f"El candidato con {voto_candidato[0]} ganó",
          f"Y los otros perdieron con {voto_candidato[1]}",
          f"y {voto_candidato[2]}")










