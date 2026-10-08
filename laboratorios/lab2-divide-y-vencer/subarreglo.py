"""Subarreglo maximo: fuerza bruta y divide y venceras."""
 
 
def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias (i, j).
 
    Args:
        valores: variacion diaria de caja, una por dia. Tiene al menos
            un elemento.
 
    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    
    n = len(valores)
    mejor_inicio, mejor_fin = 0
    suma_maxima = float('-inf')
    
    for i in range(n):
        for j in range(i, n):
            suma = 0
            for k in range(i, j + 1):
                suma += valores[k]
            if suma > suma_maxima:
                suma_maxima = suma
                mejor_inicio = i
                mejor_fin = j
                
    return mejor_inicio, mejor_fin, suma_maxima
 
 
def suma_cruzada(
    valores: list[float], inicio: int, medio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.
 
    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango considerado (inclusive).
        medio: indice del ultimo elemento de la mitad izquierda.
        fin: indice final del rango considerado (inclusive).
 
    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al
        menos un elemento de cada mitad.
    """
    
    suma = 0
    suma_max_izquierda = float('-inf')
    mejor_izquierda = medio
    
    for i in range(medio, inicio - 1, -1):
        suma += valores[i]
        if suma > suma_max_izquierda:
            suma_max_izquierda = suma
            mejor_izquierda = i
    
    suma = 0
    suma_max_derecha = float('-inf')
    mejor_derecha = medio + 1
    for j in range(medio + 1, fin + 1):
        suma += valores[j]
        if suma > suma_max_derecha:
            suma_max_derecha = suma
            mejor_derecha = j
            
    return mejor_izquierda, mejor_derecha, suma_max_izquierda + suma_max_derecha
    
 
def subarreglo_maximo(
    valores: list[float], inicio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra la mejor racha por divide y venceras.
 
    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango a considerar (inclusive).
        fin: indice final del rango a considerar (inclusive).
 
    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro de
        valores[inicio..fin].
    """
    
    if inicio == fin:
        return inicio, fin, valores[inicio]
    
    medio = (inicio + fin) // 2
    
    inicio_izq, fin_izq, suma_izq = subarreglo_maximo(valores, inicio, medio)
    inicio_der, fin_der, suma_der = subarreglo_maximo(valores, medio + 1, fin)
    inicio_cruz, fin_cruz, suma_cruz = suma_cruzada(valores, inicio, medio, fin)
    
    if suma_izq >= suma_der and suma_izq >= suma_cruz:
        return inicio_izq, fin_izq, suma_izq
    elif suma_der >= suma_izq and suma_der >= suma_cruz:
        return inicio_der, fin_der, suma_der
    else:
        return inicio_cruz, fin_cruz, suma_cruz
