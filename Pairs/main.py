#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # array pasa a ser un set para busquedas. esto es 0(1) , muy rápido
    numeros_set = set(arr)
    contador_pares = 0

    # se recorre cada número en arr 
    for b in arr: 
        if (b + k) in numeros_set:
            contador_pares += 1
    return contador_pares

# --- BLOQUE DE EJECUCIÓN INTERACTIVA ---
if __name__ == '__main__':
    print("--- Probando el problema PAIRS ---")
    
    try:
        # se pide K (la diferencia objetivo)
        k = int(input("Introduce el valor de la diferencia (K): "))
        
        # se pide la lista de números (arr)
        entrada_usuario = input("Introduce los números del arreglo separados por espacios:\n")
        
        # convierte la cadena de texto en una lista de enteros
        mi_arreglo = [int(x) for x in entrada_usuario.split()]
        
        # 3. Calculamos el resultado
        resultado = pairs(k, mi_arreglo)
        
        print("\n--- Resultado ---")
        print(f"Número de pares con diferencia {k}: {resultado}")
        
    except ValueError:
        print("\n[Error] Por favor, introduce solo números enteros válidos.")
