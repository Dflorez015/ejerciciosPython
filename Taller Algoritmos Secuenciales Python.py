# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 23:43:22 2020

@author: duvan
"""
# Calcule el valor de Yindicando paso a paso como llegó al resultado
# 1.
y = ((5 + 2 - 5)**2 * 5 + 8/2 - 30) / 2 * 5 - 3
print(y)
paso_uno = (5+2-5)**2
# Se soluciona el parentesis (2)**2, lo cual nos deja como 4 el primer paso
paso_dos = paso_uno*5 + 8/2 - 30
# Se multiplica el paso uno * 5, el resultado se suma con 8/2
# Y luego se resta con -30 dando como resultado -6
paso_final = paso_dos/2 * 5 - 3
# Paso dos se divide entre 2, luego ese resultado se multiplica por 5
# Y al final ese producto se resta con 3.

# 2.
z = 5
n = 3
m = z - n
y = (((z + 2 - n)**2 * m + 8/2 - 30)/2 * 5 - 3)**5 + 15*3 - 9/3
print(y)

paso_uno = (z + 2 - n)**2 * m + 8/2 - 30
# Al igual que en el punto 1 se realiza primero lo que está dentro del
# parentesis, lo cual nos da 4, que al elevarse al cuadrado nos da 16
# y al multiplicarse el resultado con m nos da 32, sumado con 8/2 da 36, que
# restado con 30 resulta en 6
paso_dos = (paso_uno/2 * 5 - 3)**5
# El resultado del primer paso se divide entre 2, lo cual da 3, posterior se
# multiplica por 5, que da como resultado 15, luego este se resta con 3 que da
# 12, y luego se se eleva a la 5 dando como resultado 248832
paso_final = paso_dos + 15*3 - 9/3
# El segundo paso se suma con el producto de 15*3, que da como resultado
# 248877, que al restarlo con 9/3 nos da como resultado 248874

# 3.
z = 5
n = ((8 + 2 - 4)**2 * 5 + 8 + 7/2 - 30*5) / 2 * 5 - 3
# El primer parentesis da como resultado 6, elevado al cuadrado da 36,
# multiplicado por 5 da 180, sumado más 8 da 188, sumado con 7/2 resulta en
# 191.5, restado con el producto de 30*5 da 41.5, que dividido entre 2 y se
# multiplica por 5, que nos da 103.75,y al final se resta con 3 que nos da
# como resultado 100.75
m = z**2 * 3 + n
y = ((((z + 2 - n)**2 * m + 8/2 - 30) / 2 * 5 - 3)**5 + 15 * 3 - 9/3)**2 - 5/4
print(y)

paso_uno = ((z + 2 - n)**2 * m + 8/2 - 30)
# Se resuelve el parentesis dando como resultado -93.75, que al elevarlo al
# cuadrado nos da 8789.0625, que al multiplicarse con m nos da 1544677.734
# y sumado con 8/2 y luego restado con 30 nos da 1544651.734375
paso_dos = ((paso_uno/2 * 5 - 3)**5 + 15*3 - 9/3)**2
# Luego del primer paso se divide entre 2, se multiplica por 5 y se resta con
# 3, dando como resultado 3861626.336, así resolviendo el parentesis.
# Luego se eleva a la 5, se suma con 15*3 y luego se resta con 9/3 y por último
# se eleva al cuadrado.
paso_final = paso_dos - 5/4
# Por último el paso dos se resta con * 5/4


# Realizar los algoritmosque den solución a la problemáticapresentada
# en los siguientes ejercicios:

# 1.Haga un algoritmoque calcule la masa de la siguiente fórmula:
# Masa = (presión * volúmen) / (0.37 * (temperatura + 460))
presion = float(input("Ingrese el valor de la presión: "))
volumen = float(input("Ingrese el valor del volumen: "))
temoeratura = float(input("Ingrese el valor de la temperatura: "))
masa = (presion*volumen)/(0.37*(temoeratura+460))
print(f"La masa calculada tiene un valor de: {masa}")

# 2.Calcular  el  número  de  pulsaciones  que  una  persona debe tener
# por cada 10 segundos de ejercicio, si la fórmula es:
# Num. Pulsaciones = (200 –edad) /10.

edad = int(input("Ingrese su edad: "))
n_pulsaciones = (200-edad)/10
print(f"Usted debería tener {n_pulsaciones} pulsaciones por cada 10 segundos")

# 3.Tres  personas  deciden  invertir  su  dinero  para  fundar  una  empresa.
# Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje que
# cada quien invierte con respecto a la cantidad total invertida.

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

# 4.Un banco da a sus ahorradores un interes de 1.5% sobre el monto ahorrado.
# Teniendo como dato de entrada el saldo inicial del ahorrador determine
# el saldo final.

saldo_inicial = float(input("Ingrese monto ahorrado: "))
interes_ahorro = (saldo_inicial*0.015)
saldo_total = saldo_inicial-interes_ahorro
print(f"Saldo inicial: {saldo_inicial}")
print(f"Intereses del 1.5%: {interes_ahorro}")
print(f"Saldo final: {saldo_total}")

# 5.Una empresa le hace los siguientes descuentos sobre el sueldo base a sus
# trabajadores: 1% por ley de politica pública, 4% por seguro social,
# 0.5% por seguro forzoso y 5 por caja de ahorro. Realice un algoritmo que
# determine el monto de cada descuento y el monto total a pagar al trabajador.

sueldo_base = float(input("Digite sueldo base de los trabajadores: "))
ley_publica = (sueldo_base)/100
seguro_social = (sueldo_base*0.04)
seguro_forzoso = (sueldo_base*0.005)
caja_ahorro = (sueldo_base*0.05)
descuento_total = ley_publica + seguro_social + seguro_forzoso + caja_ahorro
print(f"Por ley política pública se descuentan {ley_publica} (1%)")
print(f"Por seguro social se descuentan {seguro_social} (4%)")
print(f"Por seguro forzoso se descuentan {seguro_forzoso} (0.5%)")
print(f"Por caja de ahorro se descuentan {caja_ahorro} (5%)")
print(f"Monto total del trabajador: {sueldo_base-descuento_total}")

# 6.El  periódico  el  Informador  cobra  por  un  aviso  clasificado  un
# monto que depende del número de palabras, tamaño en cetímetros y número de
# colores. Cada palabra tiene un costo de $20.000, cada centímetro tiene un
# costo de $15.000 y cada color tiene un costo de $25.000.
# Realice un algoritmo que determine el monto a pagar por un aviso clasificado

frase = input("Ingrese la frase que desea colocar: ")
tamanio = float(input("Digite el tamaño (en centimetros) del aviso: "))
n_colores = int(input("Digite el número de colores que quiere usar: "))
aviso = [frase, tamanio, n_colores]
costo_palabra = len(aviso[0].split()) * 20000
costo_cm = aviso[1] * 15000
costo_colores = aviso[2] * 25000
costo_total = costo_palabra + costo_cm + costo_colores
print(f"Coste por palabras: {costo_palabra}, coste por tamaño: {costo_cm}")
print(f"Coste por colores: {costo_colores}")
print(f"El coste por el aviso clasificado es de : {costo_total}")

# 7.Una empresa paga a sus empleados un bono por antigüedad que consiste en
# $100.000 por el primer año laboral y $120.000 por cada año siguiente.
# Realice un algoritmo que determine el monto del bono a pagar a un trabajador
# que tiene varios años en la empresa.

anios_trabajando = int(
    input("Ingrese los años que ha estado trabajando en la empresa: "))
bono = (20000*(anios_trabajando-1)) + 100000
print(f"El bono por antigüedad que debe recibir el trabajador es de: {bono}")

# 8.Una Universidad le paga a sus profesores $20.000 la hora y le hace un
# descuento del 5% por concepto de caja de ahorro. Determine  el monto del
# descuento y el monto total a pagar al profesor.

horas_trabajo = int(input("Digite sus horas de trabajo: "))
paga_profesores = horas_trabajo * 20000
descuento_caja_ahorro = (paga_profesores*0.05)
monto_total_profesor = paga_profesores - descuento_caja_ahorro
print(f"El descuento por caja de ahorro es de: ${descuento_caja_ahorro}")
print(f"El pago al profesor es de: ${monto_total_profesor}")

# 9.Un centro de comunicaciones alquilan tarjetas para realizar llamadas y
# cobran el monto consumido de la tarjeta mas un recargo del 20%. Teniendo
# como dato de entrada el monto inicial y el monto final de la tarjeta,
# determine el costo de la llamada.

monto_inicial = int(input("Digite el monto inicial de la tarjeta: "))
monto_final = int(input("Digite el monto sobrante de la tarjeta: "))
monto_consumido = monto_inicial - monto_final
recargo = (monto_consumido*0.20)
costo_llamada = monto_consumido + recargo
print(f"Monto inicial: ${monto_inicial}, monto final: ${monto_final}")
print(f"Recargo del 20%: ${recargo}")
print(f"El costo de la llamada es de: ${costo_llamada}")

# 10.En una fototienda cobran por el revelado de un rollo $1.500 por cada foto.
# Realice  un algoritmo que  determine  el  monto  a  pagar  por  un revelado
# completo  sabiendo  que  adiconalmente  le  cobran  el  IVA (16%).

n_fotos = int(input("Ingrese el número de fotos que hay en el rollo: "))
valor_rollo = n_fotos * 1500
iva_rollo = (valor_rollo*0.16)
total_rollo = valor_rollo + iva_rollo
print(f"Sin iva: ${valor_rollo}, con iva: ${iva_rollo}")
print(f"El valor a pagar por el revelado es de: ${total_rollo}")

# 11.En un hospital existen tres áreas: Ginecología, Pediatría y Traumatología.
# El presupuestoanual del hospital se reparte conforme a la siguiente tabla:

presupuestoanual = int(input("Digite el monto presupuestal anual: "))
ginecol_pre = (presupuestoanual*0.4)
pedia_pre = (presupuestoanual*0.3)
traumato_pre = (presupuestoanual*0.3)

print(f"El presupuesto de Ginecología es de: ${ginecol_pre}")
print(f"El presupuesto de Pediatría es de: ${pedia_pre}")
print(f"El presupuesto de Traumatología es de : ${traumato_pre}")

# 12.Una video tienda alquila DVD a $1.500 el día. Tiene una promoción que
# consiste  en  dejar  gratis  el  alquiler  de  una  película.  Realice  un
# algoritmoque  teniendo  como  dato  de  entrada  el  total  de  películas
# alquiladas, y el número de días de alquiler, determine el monto a pagar.

n_peliculas = int(input("Ingrese el número de peliculas alquiladas: "))
n_dias_alquiler = int(input("Ingrese el número de días de alquiler: "))
dias_pago = (n_dias_alquiler-1) * 1500
print(f"El monto a pagar es de: ${dias_pago}")

# 13.Una Agencia de viajes cobra por un Tour a Cartagena $25.000
# diarios por persona. Realice  un algoritmoque  determine  el  monto
# a pagar por una familia que desee realizar dicho Tour sabiendo que también
# cobran el 12% de IVA.

n_familia = int(input("Digite el número de integrantes: "))
pago_fam = n_familia * 25000
iva_fam = (pago_fam*0.12)
total_fam = pago_fam + iva_fam

print(f"Pago sin IVA: ${pago_fam}, IVA: ${iva_fam}")
print(f"El total a pagar por el tour a Cartagena: ${total_fam}")

# 14.Un  Hotel  5  Estrellas  de  Santa  Marta  tiene  una  promoción  para
# sus clientes.  Cobra  por  una  habitación  $100.000  el  primer  día  y
# por  el resto $200.000 por día. Realice un algoritmoque determine el valor
# total a pagar por la habitación si la estadía fue de varios días.

n_dias_hotel = int(input("Digite el número de días en estadía: "))
pago_estadia = (n_dias_hotel*200000)-100000

print(f"El valor a pagar por la estadía es de: ${pago_estadia}")

# 15.El banco del Pueblo da microcréditos a empresarios para ser cancelados en
# un lapso de 2 años (24 meses). Al monto del préstamo se le cobra un interés
# del 24%. El empresario debe pagar la  mitad  del  préstamo  en  4  cuotas
# especiales y la otra mitad en 20 cuotas ordinarias. Realice un algoritmo que
# teniendo como dato de entrada el monto del préstamo, determine el monto total
# a pagar por el  préstamo, el monto de las cuotas especiales y el monto de las
# cuotas ordinarias.

prestamo = int(input("Digite el monto del prestamo: "))
intereses = prestamo*0.24
total_prest = prestamo + intereses
cuota_especial = total_prest/8
cuota_ordinaria = total_prest/40

print(f"Monto total a pagar: ${total_prest}")
print(f"Monto de cada cuota especial: ${cuota_especial}")
print(f"Monto de cada cuota ordinaria: ${cuota_ordinaria}")
