print("- Se juega con 3 dados y se enfrentan 2 jugadores. El juego se desarrolla en 2 rondas, \ny en cada ronda ambos jugadores pueden sumar puntos según las reglas de esa ronda.")

print("\n--------------------------------------------------------------------------------------------\n")


player1 = input("Nombre del primer jugador: ")
player2 = input("Nombre del segundo jugador: ")

print("\n\t\t\t\t##### RONDA 1 #####\n")

print("Turno de tiro para","|",player1,"|")
input("\nPresione cualquier tecla para tirar los dados: ")
# ------- Asignaremos el valor de cada dado de manera aleatoria con el módulo random
import random

print("\nLanzando dados...")

d1 = random.randrange(1,7)
print ("\t\t▩",d1)
input()
d2 = random.randrange(1,7)
print ("\t\t▩",d2)
input()
d3 = random.randrange(1,7)
print ("\t\t▩",d3)
input()

''' 
########################### RONDA 1 ########################### 
JUGADOR 1 
'''
# Primera condición: si los 3 dados comparten el mismo valor entonces se gana 6 puntos

if d1 == d2 and d2 == d3:
    puntosP1ronda1 = 6
    print("\nObtuviste 6 puntos!!! :o\n")
    input()


# Segunda condición: Si salen dos dados iguales y uno distinto, este ultimo debe tirarse nuevamente y si coincide con el resto gana 6 puntos sino, 3.
# A su vez requiere de otras condiciones necesarias para asignar el nuevo valor del dado distinto.

if d2 == d3 and d1!=d2:                                        # d1 distinto a d2 y d3
    print("\n - Tire nuevamente el dado distinto al resto:\n")
    input()
    d1 = random.randrange(1,6)
    print("\t\t\t▩",d1,"\t\t▩",d2,"\t\t▩",d3)
    input()


    if d1 == d2 and d2 == d3:
        puntosP1ronda1 = 6
        print("\nObtuviste 6 puntos!!! :o\n")
        input()
    else:
        puntosP1ronda1 = 3
        print("\nAcabas de obtener 3 puntos\n")
        input()



if d1 == d3 and d2!=d1:                                         # d2 distinto a d1 y d3
    print("\n - Tire nuevamente el dado distinto al resto:\n")
    d2 = random.randrange(1,6)
    print("\t\t\t▩",d1,"\t\t▩",d2,"\t\t▩",d3)
    input()


    if d1 == d2 and d2 == d3:
        puntosP1ronda1 = 6
        print("\nObtuviste 6 puntos!!! :o\n")
        input()
    else:
        puntosP1ronda1 = 3
        print("\nAcabas de obtener 3 puntos\n")
        input()



if d1 == d2 and d3!=d1:                                         # d3 distinto a d1 y d2
    print("\n - Tire nuevamente el dado distinto al resto:\n")
    d3 = random.randrange(1,6)
    print("\t\t\t▩",d1,"\t\t▩",d2,"\t\t▩",d3)
    input()


    if d1 == d2 and d2 == d3:
        puntosP1ronda1 = 6
        print("\nObtuviste 6 puntos!!! :o\n")
        input()
    else:
        puntosP1ronda1 = 3
        print("\nAcabas de obtener 3 puntos\n")
        input()



# Tercera condición: si los dados son desiguales entre sí no se gana puntos
if d1!=d2 and d2!=d3 and d3!=d1:
    puntosP1ronda1 = 0
    print("\nObtuviste 0 puntos :(")
    input()

''' 
########################### RONDA 1 ########################### 
JUGADOR 2 
'''
print("--------------------------------------------------------------------------------------------")
print("\nTurno de tiro para |",player2,"|",":\n")

print("Lanzando dados...")

input()
d1 = random.randrange(1,7)
print ("\t\t▩",d1)
input()
d2 = random.randrange(1,7)
print ("\t\t▩",d2)
input()
d3 = random.randrange(1,7)
print ("\t\t▩",d3)
input()

# Condicion 1
if d1 == d2 and d2 == d3:
    puntosP2ronda1 = 6
    print("\nObtuviste 6 puntos!!! :o\n")
    input()

# Condición 2
if d2 == d3 and d1!=d2:                                        # d1 distinto a d2 y d3
    print("\n - Tire nuevamente el dado distinto al resto:\n")
    d1 = random.randrange(1,6)
    print("\t\t\t▩",d1,"\t\t▩",d2,"\t\t▩",d3)
    input()


    if d1 == d2 and d2 == d3:
        puntosP2ronda1 = 6
        print("\nObtuviste 6 puntos!!! :o\n")
        input()
    else:
        puntosP2ronda1 = 3
        print("\nAcabas de obtener 3 puntos\n")
        input()



if d1 == d3 and d2!=d1:                                         # d2 distinto a d1 y d3
    print("\n - Tire nuevamente el dado distinto al resto:\n")
    d2 = random.randrange(1,6)
    print("\t\t\t▩",d1,"\t\t▩",d2,"\t\t▩",d3)
    input()


    if d1 == d2 and d2 == d3:
        puntosP2ronda1 = 6
        print("\nObtuviste 6 puntos!!! :o\n")
        input()
    else:
        puntosP2ronda1 = 3
        print("\nAcabas de obtener 3 puntos\n")
        input()



if d1 == d2 and d3!=d1:                                         # d3 distinto a d1 y d2
    print("\n - Tire nuevamente el dado distinto al resto:\n")
    d3 = random.randrange(1,6)
    print("\t\t\t▩",d1,"\t\t▩",d2,"\t\t▩",d3)
    input()


    if d1 == d2 and d2 == d3:
        puntosP2ronda1 = 6
        print("\nObtuviste 6 puntos!!! :o\n")
        input()
    else:
        puntosP2ronda1 = 3
        print("\nAcabas de obtener 3 puntos\n")
        input()


# Condicion 3
if d1!=d2 and d2!=d3 and d3!=d1:
    puntosP2ronda1 = 0
    print("\nObtuviste 0 puntos :(")
    input()

print(" - Fin de la primera ronda -\n")

########################### RONDA 2 ###########################

#El primer jugador vuelve a lanzar los 3 dados.
#a- apuesta a par o impar

print("Turno de juego para |",player1,"|",":\n")

p1apuesta = input("Elija si apostar a par o impar: ")
if p1apuesta == "par" or "impar":
    input()
else:
    print("escriba par o impar")
    p1apuesta = input("Elija si apostar a par o impar: ")

print("Lanzando dados...")
input()
d1 = random.randrange(1,7)
print ("\t\t▩",d1)
input()
d2 = random.randrange(1,7)
print ("\t\t▩",d2)
input()
d3 = random.randrange(1,7)
print ("\t\t▩",d3)
input()

#Suma de los 3 valores
sumaD = d1+d2+d3

print ("La suma de los dados es igual a: ",sumaD)

#Verificación de par o impar
valorpimp = sumaD % 2

if valorpimp==0:
    p1res="par"
else:
    p1res="impar"


#condiciones de ronda 2
#verif. dado mayor


if d1 > d2 and d1 > d3:
    dadomayor = d1
else:
    if d2>d3:
        dadomayor = d2
    else:
        dadomayor = d3

#verif. dado menor
if d1 < d2 and d1 < d3:
    dadomenor = d1
else:
    if d2<d3:
        dadomenor = d2
    else:
        dadomenor = d3

print("el dado mayor es",dadomayor)
print("el dado menor es",dadomenor)

#b-si acertó en la apuesta se suma el dado mayor al puntaje, de lo contrario se resta el dado menor

if p1res==p1apuesta:
    puntosP1ronda2 = puntosP1ronda1 + dadomayor
    print ('Acaba de sumar',dadomayor,"puntos")
    input()
else:
    puntosP1ronda2 = puntosP1ronda1 - dadomenor
    print ('Acaba de perder',dadomenor,"puntos")
    input()
#c-si ademas los dados son de la misma paridad, se duplica el puntaje

if (d1 % 2==0) and (d2 % 2==0) and (d3 % 2==0):
    puntosP1ronda2fin = puntosP1ronda2*2
    print ("Sus puntos fueron duplicados!")
    input()
else:
    puntosP1ronda2fin = puntosP1ronda2

print("puntaje ronda 2: ", player1 ,puntosP1ronda2fin)
input()
