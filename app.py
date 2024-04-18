import pandas as pd

def analisis_estadistico(l: list):
    # Comprueba si la lista está vacía
    if len(l) == 0:
        raise ValueError('La lista debe tener al menos un elemento')
    
    # Comprueba si el primer elemento de la lista es un entero
    if not isinstance(l[0], int):
        raise TypeError('Los elementos de la lista deben ser numeros')
    
    try:
        # Ordena la lista para facilitar el cálculo
        l.sort()
        
        # Crea un diccionario para almacenar la frecuencia de cada elemento
        fi = {}
        for i in l:
            if i in fi:
                fi[i] += 1
            else:
                fi[i] = 1

        # Extrae las claves y los valores del diccionario
        edades_keys = fi.keys()
        edades_values = fi.values()

        # Crea un DataFrame de pandas a partir de las claves y valores del diccionario
        df = pd.DataFrame({'Edades': edades_keys, 'fi': edades_values})
        
        # Calcula la frecuencia acumulada
        df['Fi'] = df['fi'].cumsum()
        
        # Calcula la frecuencia relativa
        df['ri'] = df['fi'] / df['fi'].sum()
        
        # Calcula la frecuencia relativa acumulada
        df['Ri'] = df['ri'].cumsum()
        
        # Calcula los porcentajes de frecuencia relativa
        df['pi%'] = df['ri'] * 100
        
        # Calcula los porcentajes de frecuencia relativa acumulada
        df['Pi%'] = df['pi%'].cumsum()

        return df
    except TypeError:
        print('Error en el tipo de dato')
    except ValueError:
        print('Error en el valor')

# Ejemplo de uso
l = [19, 29, 19, 22, 23, 19, 30, 19, 19, 19, 20, 20, 20, 18, 22, 19, 34, 34, 21,  21, 22, 28,  29, 19, 20, 19, 25, 28, 21, 22]
print(analisis_estadistico(l))
