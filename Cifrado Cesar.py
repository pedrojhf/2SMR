# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 10:53:41 2020

@author: Pedro
"""
abecedario = 'abcdefghijklmnopqrstuvwxyz'

print("BIENVENIDO A MI CIFRADOR CÉSAR")

texto_claro=input("Escribe el texto a cifrar:")
clave=int(input("Escribe la clave de cifrado (un número del 1 al 27):"))


texto_cifrado=""

for letra in texto_claro:
    nueva_posicion = abecedario.find(letra) + clave
    letra_cifrada = int(nueva_posicion) % len(abecedario)
    texto_cifrado = texto_cifrado + str(abecedario[letra_cifrada])
print("\nEl mensaje cifrado es:",texto_cifrado)
texto_descifrado=""

for letra in texto_cifrado:
    nueva_posicion = abecedario.find(letra) - clave
    letra_cifrada = int(nueva_posicion) % len(abecedario)
    texto_descifrado = texto_descifrado + str(abecedario[letra_cifrada])

print("\nEl mensaje descifrado es:",texto_descifrado)