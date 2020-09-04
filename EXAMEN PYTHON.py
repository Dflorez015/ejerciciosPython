# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 03:36:31 2020

@author: duvan
"""
# 1.

donacion = float(input("Digite la monto de la donación: "))
telecom = donacion * 0.1
sistema = donacion * 0.25
administ = donacion * 0.35
contabil = donacion - telecom - sistema - administ
print(f"La porción recibida por parte de telecomunicaciones es: {telecom}")
print(f"La porción recibida por parte de sistemas es: {sistema}")
print(f"La porción recibida por parte de administración es: {contabil}")
print(f"La porción recibida por parte de contabilidad es: {contabil}")

# 2.

primer_inversor = float(
    input("Cantidad invertida por la primera persona: "))
segundo_inversor = float(
    input("Cantidad invertida por la segunda persona: "))
tercer_inversor = float(
    input("Cantidad invertida por la tercera persona: "))
total_inversion = primer_inversor + segundo_inversor + tercer_inversor
porc_primera_p = (primer_inversor/total_inversion)*100
porc_segunda_p = (segundo_inversor/total_inversion)*100
porc_tercera_p = (tercer_inversor/total_inversion)*100
print(f"Total invertido: {total_inversion}$")
print(f"La primera persona invirtió un {porc_primera_p}% del total.")
print(f"La primera persona invirtió un {porc_segunda_p}% del total.")
print(f"La primera persona invirtió un {porc_tercera_p}% del total.")

# 3.

sueldo_base = float(input("Ingrese su sueldo base: "))
ventas_mes = float(input("Ingrese las ventas realizadas en el mes: "))
total = sueldo_base + ventas_mes * 0.15
print(f"El trabajador ganó {ventas_mes*0.15} en comisiones")
print(f"El trabajador debe recibir {total} en total")

# 4.

w = 0
talleres = 0
while w < 3:
    taller = float(input(f"Ingrese la nota del taller {w+1}: "))
    talleres = talleres + taller
    w = w + 1
examen_clase = float(input("Ingrese la nota de su examen en clase: "))
proyecto_final = float(input(("Ingrese la nota de su proyecto final: ")))
porcentajes = [talleres/len(talleres) * 0.5,
               examen_clase * 0.3, proyecto_final * 0.2]
nota = 0
for i in porcentajes:
    nota = nota + i
print(f"La nota final de la materia fundamentos de programación es: {nota}")

# 5.

n_alumnos_redes = int(input("Ingresar el número de alumnos de redes: "))
n_alumnos_cont = int(input("ingrese el número de alumnos en contabilidad: "))
n_alumnos_dise = int(input("Ingrese el número de alumnos en diseño: "))
n_alumnos = n_alumnos_cont + n_alumnos_dise + n_alumnos_redes
print(f"En redes está el {n_alumnos_redes/n_alumnos * 100}%",
      f" de los {n_alumnos} alumnos.")
print(f"En contabilidad está el {n_alumnos_cont/n_alumnos * 100}%",
      f" de los {n_alumnos} alumnos.")
print(f"En diseño está {n_alumnos_dise/n_alumnos * 100}%",
      f" de los {n_alumnos} alumnos.")

# 6.

w = True
gano = 0
perdio = 0
while w:
    nota = float(input("Digite la nota de tu asignatura: "))
    if(nota >= 3.0):
        gano = gano + 1
    else:
        perdio = perdio + 1
    seguir = int(input("¿Desea seguir ingresando notas?: (Si=1, No=0): "))
    if(seguir == 0):
        w = False
print(f"Ganó {gano} asignaturas, y perdió {perdio} asignaturas")

# 7.

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
      f" {descuentos[0]} descuentos del 35%.")
print("En la categoria de adolescentes '15-19 años' hubo:",
      f" {descuentos[1]} descuentos del 25%.")
print("En la categoria de adultos jovenes '20-45 años' hubo:",
      f" {descuentos[2]} descuentos del 10%.")
print("En la categoria de adultos mayores '46-65 años' hubo:",
      f" {descuentos[3]} descuentos del 25%.")
print("En la categoria de mayores de edad '66 años en adelante' hubo:",
      f" {descuentos[4]} descuentos del 35%.")

# 8.

n = int(input("Digite el número de trabajadores: "))
w = 0
while w < n:
    tiempo_trabajo = int(
        input(f"Ingrese las horas de laburo del trabajador {w+1} :"))
    if(tiempo_trabajo <= 40):
        print(f"Al trabajador se le debe de pagar: ${tiempo_trabajo*20}")
    else:
        extras = tiempo_trabajo - 40
        print(f"Al trabajador se le debe de pagar: ${800+(extras*25)}")
    w = w + 1

# 9.

w = 0
ventas = []
comision = []
while w < 100:
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
