import matplotlib.pyplot as plt
import random
import time
from pathlib import Path
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

def generar_entradas(n: int) -> list[int]:
    """
    Genera una lista de n números aleatorios entre 1 y 1000.
    
    Args:
        n (int): Número de entradas a generar.
        
    Returns:
        list[int]: Lista de números aleatorios.
    """
    # Fijar la semilla para reproducibilidad
    random.seed(42)
    # Generar una lista de n números aleatorios entre -100 y 100
    entradas = [random.randint(-100, 100) for _ in range(n)]
    # Mezclar la lista para asegurar aleatoriedad
    random.shuffle(entradas)
    
    return entradas

def graficar_operaciones(entradas: list[int], tiempos_fuerza: list[float], tiempos_divide: list[float]) -> None:
    """
    Grafica el tiempo de ejecución de los algoritmos de fuerza bruta y divide y vencerás.
    
    Args:
        entradas: Lista de tamaños de entrada.
        tiempos_fuerza: Lista de tiempos de ejecución del algoritmo de fuerza bruta.
        tiempos_divide: Lista de tiempos de ejecución del algoritmo divide y vencerás.
    """
    plt.plot(entradas,
             tiempos_fuerza,
             label='Fuerza Bruta',
             marker='o')
    
    plt.plot(entradas,
             tiempos_divide,
             label='Divide y Vencerás',
             marker='D')
    
    # Configuración de la escala logarítmica para ambos ejes
    plt.xscale('log')
    plt.yscale('log')
    
    plt.xlabel('Tamaño de Entrada (n)')
    plt.ylabel('Tiempo de Ejecución (s)')
    plt.title('Comparación\nTiempos de Ejecución vs Tamaño de Entrada por algoritmo')
    plt.legend()
    plt.grid()
    
    carpeta = Path(__file__).resolve().parent / "graficas" # Crea la carpeta "graficas" en el mismo directorio que este script
    carpeta.mkdir(exist_ok=True)
    plt.savefig(carpeta / "tiempo_vs_n.png")
    plt.show()

def main():
    """
    Genera y grafica los tiempos de ejecución de los algoritmos de fuerza bruta y divide y vencerás
    """
    # Definir los tamaños de entrada para las pruebas
    tamanos = [10, 50, 100, 500, 1000, 5000]
    tiempos_fuerza = []
    tiempos_divide = []
    suma_fuerza = 0
    suma_divide = 0
    
    for n in tamanos:
        # Generar entradas aleatorias
        entradas = generar_entradas(n)
        
        # Medir tiempo de ejecución para fuerza bruta
        start_time = time.perf_counter()
        suma_fuerza = (subarreglo_fuerza_bruta(entradas)[2])
        end_time = time.perf_counter()
        tiempos_fuerza.append(end_time - start_time)
        print(f"Tiempo de ejecución para fuerza bruta con n={n}: {end_time - start_time:.6f} segundos")
        print(f"Suma máxima encontrada por fuerza bruta: {suma_fuerza}")

        # Medir tiempo de ejecución para divide y vencerás
        start_time = time.perf_counter()
        suma_divide = (subarreglo_maximo(entradas, 0, n - 1)[2])
        end_time = time.perf_counter()
        tiempos_divide.append(end_time - start_time)
        print(f"Tiempo de ejecución para divide y vencerás con n={n}: {end_time - start_time:.6f} segundos")
        print(f"Suma máxima encontrada por divide y vencerás: {suma_divide}")
        
        print("-" * 50)

    # Graficar los resultados
    graficar_operaciones(tamanos, tiempos_fuerza, tiempos_divide)

if __name__ == "__main__":
    main()