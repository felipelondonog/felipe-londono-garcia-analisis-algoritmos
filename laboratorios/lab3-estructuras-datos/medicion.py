import matplotlib.pyplot as plt
import random
import time
from pathlib import Path
from estructuras import ListaEnlazada, TablaHash

random.seed(7) # Semilla determinada para todas las funciones aleatorias del experimento

def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guías de diez dígitos que no están en la colección.
 
    Args:
        existentes: guías almacenadas en las estructuras.
        cantidad: cuantas guías inexistentes generar.
        semilla: semilla del generador, para reproducir la medición.
 
    Returns:
        Una lista con `cantidad` guías que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes

def generar_guias_aleatorias(n: int) -> list[int]:
    """Genera n cantidad de guías aleatorias de diez dígitos.

    Args:
        n (int): número de guías a generar.

    Returns:
        list[int]: _description_
    """
    guias = random.sample(range(10**9, 10**10 - 1), n)
    
    return guias

def insertar_guias(guias: list[int], lista_enlazada: ListaEnlazada, tabla_hash: TablaHash) -> tuple[ListaEnlazada, TablaHash]:
    """Inserta las guías generadas en ambas estructuras de datos usando estados aleatorios de una lista de estados.

    Args:
        guias (list[int]): Listado de guías aleatorias.
        lista_enlazada (ListaEnlazada): lista enlazada que se va a poblar
        tabla_hash (TablaHash): tabla hash que se va a poblar

    Returns:
        tuple[ListaEnlazada, TablaHash]: Tupla con la lista enlazada y la tabla hash pobladas
    """
    estados = ["En bodega", "Entregado", "En camino", "Retrasado", "En aduana"]
    
    for guia in guias:
        estado = random.choice(estados)
        lista_enlazada.insertar(guia, estado)
        tabla_hash.insertar(guia, estado)
        
    return [lista_enlazada, tabla_hash]

def es_primo(number: int) -> bool:
    """Calcula si un número n es primo, retorna True si es primo, False sí no.

    Args:
        number (int): número a evaluar.

    Returns:
        bool: True si n es primo. False sí no es primo.
    """    
    if number < 2: return False
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True
    

def calcular_m(number: int) -> int:
    """Calcula un m que sea el primo más cercano a n/2.

    Args:
        number (int): cantidad de guías que van en la tabla hash.

    Returns:
        int: valor de m para la tabla hash.
    """    
    objetivo = number // 2
    distancia = 0
    
    while True:
        inferior = objetivo - distancia
        superior = objetivo + distancia

        if es_primo(inferior):
            return inferior

        if es_primo(superior):
            return superior

        distancia += 1

def graficar_operaciones(
    valor_x: list[int], 
    valor_y1: list[float], 
    valor_y2: list[float] | None, 
    titulo: str,
    label_x: str,
    label_y: str,
    label_y1: str | None,
    label_y2: str | None
    ) -> None:
    """Grafica los resultados de un experimento, muestra la gráfica y la guarda en /graficas

    Args:
        valor_x (list[int]): Valores del eje x.
        valor_y1 (list[float]): Valores del eje y.
        valor_y2 (list[float] | None): Valores secundarios del eje y.
        titulo (str): Título de la gráfica.
        label_x (str): Descripción del eje x.
        label_y (str): Descripción del eye y.
        label_y1 (str): Leyenda eje y.
        label_y2 (str | None): Leyenda eye y secundario.
    """    
    plt.plot(valor_x, valor_y1, label=label_y1)
    
    if valor_y2 is not None:
        plt.plot(valor_x, valor_y2, label=label_y2)
    
    plt.xscale('log')
    plt.yscale('log')
    
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    
    plt.title(titulo)
    plt.legend()
    plt.grid()
    
    carpeta = Path(__file__).resolve().parent / "graficas"
    carpeta.mkdir(exist_ok=True)
    plt.savefig(carpeta / titulo)
    plt.show()

def experimento_A() -> None:
    """Ejecuta los pasos necesarios para el Experimento A del taller.
    """    
    cantidades = [100, 500, 1000, 5000, 20000, 50000]
    tiempos_lista = []
    tiempos_tabla = []
    
    for n in cantidades:
        print(f"n = {n}")
        # Generar el conjunto de guias aleatorias e inexistentes
        guias = generar_guias_aleatorias(n)
        guias_inexistentes = generar_guias_inexistentes(guias, 200)
        
        # calcular m para cada n
        m = calcular_m(n)
        
        lista_enlazada = ListaEnlazada()
        tabla_hash = TablaHash(m)
        
        insertar_guias(guias, lista_enlazada, tabla_hash)
        
        #Probar que para 20 guías existentes, ambas estructuras devuelvan el mismo estado
        for i in range(20):
            guia = random.choice(guias)
            assert lista_enlazada.buscar(guia) == tabla_hash.buscar(guia)
        
        print(f"Pruebas assert superadas con éxito\n")
        
        # Calcular tiempo de consulta de lista enlazada con 200 guías inexistentes
        start_time = time.perf_counter()
        
        for guia in guias_inexistentes:
            lista_enlazada.buscar(guia)
            
        end_time = time.perf_counter()
        tiempos_lista.append(end_time - start_time)
        
        print(f"Tiempo de ejecución para lista enlazada: {end_time - start_time}")
        
        # Calcular tiempo de consulta de tabla hash con 200 guías inexistentes
        start_time = time.perf_counter()
        
        for guia in guias_inexistentes:
            tabla_hash.buscar(guia)
            
        end_time = time.perf_counter()
        tiempos_tabla.append(end_time - start_time)
        
        print(f"Tiempo de ejecución para tabla hash: {end_time - start_time}")
        print("-" * 80)
        
    # Graficar los resultados
    titulo = "lista_vs_tabla"
    label_x = "Cantidad de guías"
    label_y = "Tiempo de ejecución"
    label_y1 = "Lista enlazada"
    label_y2 = "Tabla hash"
    
    graficar_operaciones(cantidades, tiempos_lista, tiempos_tabla, titulo, label_x, label_y, label_y1, label_y2)
           
    
def experimento_B() -> None:
    """Ejecuta los pasos necesarios para el Experimento B del taller.
    """    
    n = 20000
    ejemplos_m = [2000, 5000, 20000, 40000]
    tiempos = []
    valores_alfa = []
    
    guias = generar_guias_aleatorias(n)
    guias_inexistentes = generar_guias_inexistentes(guias, 200)
    
    for m in ejemplos_m:
        tabla_hash = TablaHash(m)
        _ = ListaEnlazada()
        
        _, tabla_hash = insertar_guias(guias, _, tabla_hash)
        
        # Calcular tiempo de consulta de tabla hash con 200 guías inexistentes variando el valor de m
        start_time = time.perf_counter()
        
        for guia in guias_inexistentes:
            tabla_hash.buscar(guia)
            
        end_time = time.perf_counter()
        tiempos.append(end_time - start_time)
        valores_alfa.append(tabla_hash.factor_carga())
        
        print(f"m = {m}. alfa = {tabla_hash.factor_carga()}")
        print(f"Tiempo de ejecución de tabla hash: {end_time - start_time}")
        print("-" * 80)
    
    #Graficar los resultados
    titulo = "tiempo_vs_alfa"
    label_x = "Valores de alfa (factor de carga)"
    label_y = "Tiempo de ejecución"
    
    graficar_operaciones(valores_alfa, tiempos, None, titulo, label_x, label_y, None, None)
        

def main():
    """Ejecuta ambos experimentos necesarios para la parte 2 del taller.
    """    
    print("--------------------EJECUCIÓN DE EXPERIMENTO A-----------------------")
    experimento_A()
    print("\n--------------------EJECUCIÓN DE EXPERIMENTO B-----------------------")
    experimento_B()
    
if __name__ == "__main__":
    main()
    