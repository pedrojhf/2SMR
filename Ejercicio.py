# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:04:19 2020

@author: Pedro
"""
print("BIENVENIDO A EMPERAJENDO.COM")
print("Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal")
nombre=str(input("Tu nombre:"))
nacimiento=int(input("Año de nacimiento:"))
edad=(2020-nacimiento)
musica=str(input("¿Te gusta Taburete?"))
print("Hola,",nombre,". Si no me equivoco tienes ",edad," años.")
si=("si","Si","sI","SI")
if musica=="si":
    print("OK Boomer, lo tuyo va a ser un caso difícil")
else:
    print("Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.")
print("\n")

print("Felicitación de Cumpleaños")
i=1
while i != edad:
    print("Que no cumple ",i)
    i=i+1
print("¡Qué si cumple",i,"!")
i=0
for i in range(1,edad):
    print("Que no cumple ",i)
i=i+1
print("¡Qué si cumple",i,"!")
print("\n")

usuario=[nombre,edad,musica]
for dato in usuario:
    print(dato)
print("\n")

usuario={
        "nombre":nombre,
        "edad":edad,
        "musica":musica
        }

for dato in usuario.values():
    print(dato)
    