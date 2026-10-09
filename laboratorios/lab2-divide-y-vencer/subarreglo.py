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
    mejor_inicio, mejor_fin = 0, 0
    suma_maxima = float('-inf')
    
    # Implementación de fuerza bruta reutilizando la suma acumulada
    # para no recalcular sumas de subarreglo, complejidad teórica Θ(n²)
    for i in range(n):
        suma = 0
        
        for j in range(i, n):
            suma += valores[j]
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
    # Inicializar variables para encontrar la mejor suma en la mitad izquierda
    suma = 0
    suma_max_izquierda = float('-inf')
    mejor_izquierda = medio
    
    # Buscar la mejor suma en la mitad izquierda
    for i in range(medio, inicio - 1, -1):
        suma += valores[i]
        if suma > suma_max_izquierda:
            suma_max_izquierda = suma
            mejor_izquierda = i
    
    # Inicializar variables para encontrar la mejor suma en la mitad derecha
    suma = 0
    suma_max_derecha = float('-inf')
    mejor_derecha = medio + 1
    
    # Buscar la mejor suma en la mitad derecha
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
    # Caso base: si el rango tiene un solo elemento, ese es el mejor tramo
    if inicio == fin:
        return inicio, fin, valores[inicio]
    
    # Dividir el rango en dos mitades y encontrar el mejor tramo en cada mitad y el mejor tramo cruzando el punto medio
    medio = (inicio + fin) // 2
    
    # Llamadas recursivas para encontrar el mejor tramo en la mitad izquierda, derecha y cruzando el medio
    inicio_izq, fin_izq, suma_izq = subarreglo_maximo(valores, inicio, medio)
    inicio_der, fin_der, suma_der = subarreglo_maximo(valores, medio + 1, fin)
    inicio_cruz, fin_cruz, suma_cruz = suma_cruzada(valores, inicio, medio, fin)
    
    # Comparar las tres sumas y devolver la mejor
    if suma_izq >= suma_der and suma_izq >= suma_cruz:
        return inicio_izq, fin_izq, suma_izq
    elif suma_der >= suma_izq and suma_der >= suma_cruz:
        return inicio_der, fin_der, suma_der
    else:
        return inicio_cruz, fin_cruz, suma_cruz
