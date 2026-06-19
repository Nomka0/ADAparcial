# Parcial ADA - Soluciones HackerRank

Este repositorio contiene las soluciones en python para dos problemas de HackerRank: **Pairs** y **Sherlock and the Valid String**.

---

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
.
├── Pairs
│   ├── main.py       # Algoritmo de búsqueda de diferencias en tiempo O(N)
│   └── README.md
├── Sherlock
│   ├── main.py       # Algoritmo de validación de cadenas en tiempo O(N)
│   └── README.md
└── README.md         # Instrucciones generales (Este archivo)
```
---

## Instrucciones de Ejecución

Ambos programas están diseñados para ser interactivos, lo que significa que se pueden probar con tus propios datos desde la terminal.

Asegúrate de estar parado en la raíz del proyecto (`./parcialADA`) antes de ejecutar los comandos.

### 1. Ejecutar el Problema: Pairs
Este programa calcula cuántos pares de números en un arreglo tienen una diferencia exacta de K.

* **Comando de ejecución:**
    `python3 Pairs/main.py`

* **Ejemplo de uso en terminal:**

```
    --- Probando el problema PAIRS ---
    Introduce el valor de la diferencia (K): 2
    Introduce los números del arreglo separados por espacios:
    1 5 3 4 2

    --- Resultado ---
    Número de pares con diferencia 2: 3
```
---

### 2. Ejecutar el Problema: Sherlock and the Valid String
Este programa determina si una cadena de texto es válida bajo las condiciones de frecuencias de HackerRank (permitiendo eliminar como máximo 1 carácter).



* **Comando de ejecución:**
    `python3 Sherlock/main.py`
```
* **Ejemplo de uso en terminal:**
    Escribe una cadena de texto para probar:
    aabbcc
    Resultado Sherlock: YES
```
---

## Resumen de Complejidad Computacional

Ambas soluciones han sido optimizadas utilizando estructuras de dispersión (Hash Maps y Sets) para evitar soluciones de fuerza bruta de orden O(N^2), logrando pasar todos los casos de prueba de la plataforma:

| Problema | Enfoque | Complejidad Temporal | Complejidad Espacial |
| :--- | :--- | :---: | :---: |
| **Pairs** | Hash Set | O(N) | O(N) |
| **Sherlock** | Double Frequency Counter | O(N) | O(1) Espacio acotado por el alfabeto (26) |

---
