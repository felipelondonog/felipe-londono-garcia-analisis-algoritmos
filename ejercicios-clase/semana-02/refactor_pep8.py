def calcular_promedio(lista_numeros: list) -> float:
    """Calcula el promedio de una lista de números.
 
    Args:
        lista_numeros: lista de números a evaluar.
 
    Returns:
        float: promedio aritmético de los números en la lista.
    """
    sumatoria = 0
    for x in lista_numeros:
        sumatoria = sumatoria + x
    return sumatoria / len(lista_numeros)

def main() -> None:
    """Función principal del programa."""
    lista = [1, 2, 3, 4, 5]
    promedio = calcular_promedio(lista)
    print(promedio)

if __name__ == "__main__":
    main()