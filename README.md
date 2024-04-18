Análisis Estadístico Básico en Python
Este script de Python proporciona una función para realizar un análisis estadístico básico de una lista de números. Calcula varias estadísticas descriptivas, como la frecuencia de cada valor, la frecuencia acumulada, la frecuencia relativa y los porcentajes de frecuencia relativa.

Requisitos
Python 3.x
pandas (puede instalarse mediante pip install pandas)
Uso
Clona este repositorio o descarga el script analisis_estadistico.py.
Importa la función analisis_estadistico en tu script de Python.
Llama a la función analisis_estadistico con una lista de números como argumento.
La función devolverá un DataFrame de pandas con las estadísticas calculadas.
python
Copy code
import pandas as pd
from analisis_estadistico import analisis_estadistico

# Ejemplo de uso
lista_edades = [19, 29, 19, 22, 23, 19, 30, 19, 19, 19, 20, 20, 20, 18, 22, 19, 34, 34, 21,  21, 22, 28,  29, 19, 20, 19, 25, 28, 21, 22]
resultado = analisis_estadistico(lista_edades)
print(resultado)
Funcionalidades
Verifica si la lista está vacía o si los elementos no son números enteros.
Calcula la frecuencia de cada valor en la lista.
Calcula la frecuencia acumulada.
Calcula la frecuencia relativa.
Calcula la frecuencia relativa acumulada.
Calcula los porcentajes de frecuencia relativa y su acumulación.