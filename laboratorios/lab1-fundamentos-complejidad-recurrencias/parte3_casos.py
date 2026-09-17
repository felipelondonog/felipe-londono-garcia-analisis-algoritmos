import datos as d
import algoritmos as al
import time
from pathlib import Path
import matplotlib.pyplot as plt

# Comparación de casos para el algoritmo de ordenamiento por inserción.

class rendimiento:
    """
    Clase para almacenar el rendimiento de un caso de ordenamiento.
    
    Atributos:
        n_entradas (int): Tamaño de la entrada.
        tiempo (float): Tiempo de ejecución.
        comparaciones (int): Número de comparaciones realizadas.
    """
    def __init__(self):
        self.n_entradas = int
        self.tiempo = float
        self.comparaciones = int
        
    def __str__(self):
        return f"n_entradas: {self.n_entradas}, T: {self.tiempo:.6f} s, Comparaciones: {self.comparaciones}"

def probar_caso(lista_entradas: list[int], caso: str, semilla: int = 42) -> rendimiento:
    """Prueba cada uno de los casos de ordenamiento para cada n en lista_entradas.
    
    Args:
        lista_entradas: lista de enteros positivos, cada uno representando
            un tamaño de lote a ordenar.
        caso: cadena que representa el caso de ordenamiento a probar.
            Puede ser "A" (aleatorio), "B" (casi ordenado) o "C" (inverso).
        semilla: semilla para el generador aleatorio.
    """
    try:
        rendimientos = []    
        for n in lista_entradas:
            rendimiento_caso = rendimiento()
            
            # Generar la lista de entrada según el caso especificado
            if caso == "A":
                lista = d.generar_aleatorio(n, semilla)
            elif caso == "B":
                lista = d.generar_casi_ordenado(n, semilla)
            elif caso == "C":
                lista = d.generar_inverso(n, semilla)
            else:
                raise ValueError("Caso desconocido: debe ser 'A', 'B' o 'C'.")
            
            inicio = time.perf_counter()  # Reinicia el contador de tiempo
            _, comparaciones = al.insertion_sort_inverso(lista)
            fin = time.perf_counter()  # Detiene el contador de tiempo
           
            # Almacenar los resultados del rendimiento
            rendimiento_caso.n_entradas = n
            rendimiento_caso.tiempo = fin - inicio
            rendimiento_caso.comparaciones = comparaciones
            
            rendimientos.append(rendimiento_caso)
            
        return rendimientos
    
    except ValueError as error:
        print(f"Error: {error}")
        return {}, {}
    
 
def imprimir_grafico_tiempo(rendimientos_aleatorio, rendimientos_casi_ordenado, rendimientos_inverso):
    """ Imprime un grafico de lineas con los resultados de los tres casos de ordenamiento.
        
        Args:
            rendimientos_aleatorio: lista de objetos rendimiento para el caso A (aleatorio).
            rendimientos_casi_ordenado: lista de objetos rendimiento para el caso B (casi ordenado).
            rendimientos_inverso: lista de objetos rendimiento para el caso C (inverso).    
    """
    plt.plot([r.n_entradas for r in rendimientos_aleatorio], [r.tiempo for r in rendimientos_aleatorio], label="Caso A (aleatorio)")
    plt.plot([r.n_entradas for r in rendimientos_casi_ordenado], [r.tiempo for r in rendimientos_casi_ordenado], label="Caso B (casi ordenado)")
    plt.plot([r.n_entradas for r in rendimientos_inverso], [r.tiempo for r in rendimientos_inverso], label="Caso C (inverso)")
    
    plt.xlabel("Tamaño de entrada")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempo de ejecución de Insertion Sort")

    plt.legend()
    plt.grid()
    carpeta = Path(__file__).resolve().parent / "graficas" # Crea la carpeta "graficas" en el mismo directorio que este script
    carpeta.mkdir(exist_ok=True)
    plt.savefig(carpeta / "tiempos_insertion_sort.png")
    plt.show()
    
def imprimir_grafico_comparaciones(rendimientos_aleatorio, rendimientos_casi_ordenado, rendimientos_inverso):
    """ Imprime un grafico de lineas con los resultados de los tres casos de ordenamiento.
        
        Args:
            rendimientos_aleatorio: lista de objetos rendimiento para el caso A (aleatorio).
            rendimientos_casi_ordenado: lista de objetos rendimiento para el caso B (casi ordenado).
            rendimientos_inverso: lista de objetos rendimiento para el caso C (inverso).    
    """
    plt.plot([r.n_entradas for r in rendimientos_aleatorio], [r.comparaciones for r in rendimientos_aleatorio], label="Caso A (aleatorio)")
    plt.plot([r.n_entradas for r in rendimientos_casi_ordenado], [r.comparaciones for r in rendimientos_casi_ordenado], label="Caso B (casi ordenado)")
    plt.plot([r.n_entradas for r in rendimientos_inverso], [r.comparaciones for r in rendimientos_inverso], label="Caso C (inverso)")
    
    plt.ticklabel_format(axis='y', style='plain')  # Formato científico para el eje y
    
    plt.xlabel("Tamaño de entrada")
    plt.ylabel("Número de comparaciones")
    plt.title("Comparaciones de Insertion Sort")

    plt.legend()
    plt.grid()
    carpeta = Path(__file__).resolve().parent / "graficas" # Crea la carpeta "graficas" en el mismo directorio que este script
    carpeta.mkdir(exist_ok=True)
    plt.savefig(carpeta / "comparaciones_insertion_sort.png")
    plt.show()

def main():
    # Definir los tamaños de entrada y la semilla para reproducibilidad
    lista_entradas = [100, 200, 400, 800, 1600, 3200, 6400]
    semilla = 42  # Semilla para reproducibilidad de los resultados
    
    # Probar cada caso y almacenar los resultados
    rendimientos_aleatorio = probar_caso(lista_entradas, "A", semilla)
    rendimientos_casi_ordenado = probar_caso(lista_entradas, "B", semilla)
    rendimientos_inverso = probar_caso(lista_entradas, "C", semilla)\
    
    # Imprimir los resultados de cada caso
    print("################## Resultados del caso A (aleatorio): ##################")
    for _ in range(len(lista_entradas)):
        print(rendimientos_aleatorio[_].__str__())
    
    print("\n################## Resultados del caso B (casi ordenado): ##################")
    for _ in range(len(lista_entradas)):
        print(rendimientos_casi_ordenado[_].__str__())
    
    print("\n################## Resultados del caso C (inverso): ##################")
    for _ in range(len(lista_entradas)):
        print(rendimientos_inverso[_].__str__())

    # Imprimir y guardar gráficos de tiempo y comparaciones
    imprimir_grafico_tiempo(rendimientos_aleatorio, rendimientos_casi_ordenado, rendimientos_inverso)
    
    imprimir_grafico_comparaciones(rendimientos_aleatorio, rendimientos_casi_ordenado, rendimientos_inverso)

if __name__ == "__main__":
    main()
