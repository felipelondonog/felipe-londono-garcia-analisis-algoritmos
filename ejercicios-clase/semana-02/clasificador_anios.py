"""Clasificador de años bisiestos.
 
Complete las funciones siguiendo la especificación de cada docstring.
"""
 
def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.
 
    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.
 
    Args:
        anio: año a evaluar (número entero).
 
    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    try:
        if (anio % 4 == 0):
            if (anio % 100 == 0):
                if (anio % 400 == 0):
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un año válido.")
        return False
 
def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.
 
    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).
 
    Returns:
        Lista de años como enteros.
    """
    try:
        anios_str = input("Ingrese años separados por comas (ej. 2000,2023,2024):")
        lista_anios = list(map(int, anios_str.split(',')))
        for anio in lista_anios:
            if anio < 0:
                raise ValueError("Los años no pueden ser negativos.")
        return lista_anios
    except ValueError as e:
        print("Entrada inválida. Por favor, ingrese una lista válida de años separados por comas." + "\n" + str(e))
        return None
 
def main() -> None:
    """Punto de entrada del script."""
    try:
        lista_anios = leer_anios()
        if lista_anios is None:
            print("No se pudo procesar la lista de años ingresada.")
            return
        anios_bisiestos = []
        for anio in lista_anios:
            if es_bisiesto(anio):
                anios_bisiestos.append(anio)
        print(f"Lista de años ingresados: {lista_anios}")
        print(f"Años bisiestos: {anios_bisiestos}")
        print(f"Cantidad de años bisiestos: {len(anios_bisiestos)} de {len(lista_anios)} años ingresados.")
    except ValueError:
        print("Ocurrió un error al procesar los años ingresados. Por favor, intente nuevamente.")
    finally:
        print("Programa finalizado.")
 
if __name__ == "__main__":
    main()