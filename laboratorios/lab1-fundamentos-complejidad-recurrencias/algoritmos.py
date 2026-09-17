"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""
 
def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.
    De menor a mayor.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    lista_ordenada = datos.copy()
    comparaciones = 0
    
    for i in range(1, len(lista_ordenada)):
        j = i - 1
        key = lista_ordenada[i]
        
        while j >= 0 and lista_ordenada[j] > key:
            comparaciones += 1
            lista_ordenada[j + 1] = lista_ordenada[j]
            j -= 1
        
        lista_ordenada[j + 1] = key
        
    return lista_ordenada, comparaciones

def insertion_sort_inverso(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.
    De mayor a menor.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    lista_ordenada = datos.copy()
    comparaciones = 0
    
    for i in range(1, len(lista_ordenada)):
        j = i - 1
        key = lista_ordenada[i]
        
        while j >= 0 and lista_ordenada[j] < key:
            comparaciones += 1
            lista_ordenada[j + 1] = lista_ordenada[j]
            j -= 1
        
        lista_ordenada[j + 1] = key
        
    return lista_ordenada, comparaciones

def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    
    lista_desordenada = datos.copy()
    comparaciones = 0
    
    if len(lista_desordenada) <= 1:
        return lista_desordenada, comparaciones
    
    mitad = len(lista_desordenada) // 2
    
    izquierda = merge_sort(lista_desordenada[:mitad])
    derecha = merge_sort(lista_desordenada[mitad:])
    
    lista_ordenada = []
    i = 0
    j = 0
    
    while i < len(izquierda[0]) and j < len(derecha[0]):
        comparaciones += 1
        if izquierda[0][i] < derecha[0][j]:
            lista_ordenada.append(izquierda[0][i])
            i += 1
        else:
            lista_ordenada.append(derecha[0][j])
            j += 1
            
    lista_ordenada.extend(izquierda[0][i:])
    lista_ordenada.extend(derecha[0][j:])
    
    return lista_ordenada, comparaciones