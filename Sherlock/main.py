#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    # se cuentan las letras
    cuenta_letras = Counter(s)

    # se cuenta la frecuencia de cada una 
    cuenta_frecuencias = Counter(cuenta_letras.values())

    # tienen la misma frecuencia? 
    if len(cuenta_frecuencias) == 1:
        return "YES"
    
    # Si hay más de 2 frecuencias distintas
    if len(cuenta_frecuencias) > 2:
        return "NO"
    
    # Si hay exactamente 2 frecuencias 
    f1, f2 = list(cuenta_frecuencias.keys())
    f_min, f_max =min(f1,f2), max(f1, f2)

    # Caso A. Eliminar una sola letra 
    if f_min == 1 and cuenta_frecuencias[f_min] == 1:
        return "YES"

    # Caso B. reducir la letra que tiene exceso 
    if f_max - f_min == 1 and cuenta_frecuencias[f_max] == 1:
        return "YES"

    # Si no se cumplen ninguno de los casos 
    return "NO"

if __name__ == '__main__':
    print("Escribe una cadena de texto para probar:")
    s = input()
    result = isValid(s)
    print(f"Resultado Sherlock: {result}")
