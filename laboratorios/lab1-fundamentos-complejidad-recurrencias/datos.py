import random
import algoritmos as al

"""Generadores de lotes de registros para los escenarios de Tamiza."""
 
def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).
 
    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    
    lista_random = []
    random.seed(semilla)
    
    for _ in range(n):
        lista_random.append(random.randint(0, 1000))
        
    return lista_random
 
 
def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).
 
    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """

    lista_random = generar_aleatorio(n, semilla)
    
    lista_ordenada = lista_random[:int(n*0.98)]
    lista_ordenada = al.insertion_sort_inverso(lista_ordenada)[0]
    
    lista_desordenada = lista_random[int(n*0.98):]
    
    return (lista_ordenada + lista_desordenada)
 
def generar_inverso(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).
 
    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    
    lista_random = generar_aleatorio(n, semilla)
    lista_inversa = al.insertion_sort(lista_random)[0]

    return lista_inversa

if __name__ == "__main__":
    print("lista aleatoria---------------------------------")
    print(generar_aleatorio(10))
    print("lista casi ordenada----------------------------")
    print(generar_casi_ordenado(10))
    print("lista inversa-----------------------------------")
    print(generar_inverso(10))