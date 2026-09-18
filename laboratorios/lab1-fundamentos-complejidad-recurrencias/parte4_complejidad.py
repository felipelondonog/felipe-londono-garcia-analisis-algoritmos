import datos as d
import algoritmos as al
import time
from pathlib import Path
import matplotlib.pyplot as plt

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


def probar_caso_aleatorio(algoritmo, lista_entradas: list[int], semilla: int = 42) -> list[rendimiento]:
    """Prueba cada uno de los casos de ordenamiento para cada n en lista_entradas.
        
        Args:
            lista_entradas: lista de enteros positivos, cada uno representando
                un tamaño de lote a ordenar.
            algoritmo: cadena que determina el algoritmo a probar. Puede ser "merge" o "insertion".
            semilla: semilla para el generador aleatorio.
        """
    try:
        rendimientos = []    
        for n in lista_entradas:
            rendimiento_caso = rendimiento()
            
            # Generar la lista de entradas aleatoria
            lista = d.generar_aleatorio(n, semilla)
            
            inicio = time.perf_counter()  # Reinicia el contador de tiempo
            
            if (algoritmo == "merge"):
                _, comparaciones = al.merge_sort(lista)
            elif (algoritmo == "insertion"):
                _, comparaciones = al.insertion_sort(lista)
            
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

def imprimir_grafico_tiempo(rendimientos_insertion, rendimientos_merge):
    """ Imprime un grafico de lineas con los resultados de los tres casos de ordenamiento.
        
        Args:
            rendimientos_aleatorio: lista de objetos rendimiento para el caso A (aleatorio).
    """
    plt.plot([r.n_entradas for r in rendimientos_insertion], [r.tiempo for r in rendimientos_insertion], label="Insertion Sort")
    plt.plot([r.n_entradas for r in rendimientos_merge], [r.tiempo for r in rendimientos_merge], label="Merge Sort")

    plt.xlabel("Tamaño de entrada")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempo de ejecución por algoritmo")

    plt.legend()
    plt.grid()
    carpeta = Path(__file__).resolve().parent / "graficas" # Crea la carpeta "graficas" en el mismo directorio que este script
    carpeta.mkdir(exist_ok=True)
    plt.savefig(carpeta / "parte4_tiempo.png")
    plt.show()
    
def main():
    # Definir los tamaños de entrada a probar
    lista_entradas = [100, 200, 400, 800, 1600, 3200, 6400]
    semilla = 42  # Semilla para reproducibilidad de los resultados
    
    # Probar cada caso y almacenar los resultados
    rendimientos_insertion = probar_caso_aleatorio("insertion", lista_entradas, semilla)
    rendimientos_merge = probar_caso_aleatorio("merge", lista_entradas, semilla)
    
    # Imprimir los resultados de cada caso
    print("################## Resultados del algoritmo Insertion Sort: ##################")
    for _ in range(len(lista_entradas)):
        print(rendimientos_insertion[_].__str__())
        
    print("################## Resultados del algoritmo Merge Sort: ##################")
    for _ in range(len(lista_entradas)):
        print(rendimientos_merge[_].__str__())
             
     # Imprimir y guardar gráficos de tiempo y comparaciones
    imprimir_grafico_tiempo(rendimientos_insertion, rendimientos_merge)
     
if __name__ == "__main__":
    main()