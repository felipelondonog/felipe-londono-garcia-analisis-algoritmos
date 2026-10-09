import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

# ---------------------------------------------------------
# 1. Serie de ocho días de la situación problema

serie = [-3, 5, -2, 8, -6, 3, 9, -4]

resultado_fuerza = subarreglo_fuerza_bruta(serie)
resultado_divide = subarreglo_maximo(serie, 0, len(serie) - 1)

assert resultado_fuerza[2] == 17
assert resultado_divide[2] == 17

print("1. Serie de ocho días de la situación problema. Prueba superada correctamente.")
print(f"Serie: {serie}")
print(f"Fuerza bruta: {resultado_fuerza}")
print(f"Divide y vencerás: {resultado_divide}")

# ---------------------------------------------------------
# 2. Serie de un solo elemento

serie = [7]

resultado_fuerza = subarreglo_fuerza_bruta(serie)
resultado_divide = subarreglo_maximo(serie, 0, len(serie) - 1)
# El mejor tramo es el único elemento de la lista
assert resultado_fuerza[2] == 7
assert resultado_divide[2] == 7

print("\n2. Serie de un solo elemento. Prueba superada correctamente.")
print(f"Serie: {serie}")
print(f"Fuerza bruta: {resultado_fuerza}")
print(f"Divide y vencerás: {resultado_divide}")

# ---------------------------------------------------------
# 3. Serie con todos los valores negativos

serie = [-8, -3, -10, -2, -7]

resultado_fuerza = subarreglo_fuerza_bruta(serie)
resultado_divide = subarreglo_maximo(serie, 0, len(serie) - 1)

# El mejor tramo es el elemento -2, el valor menos negativo
assert resultado_fuerza[2] == -2
assert resultado_divide[2] == -2

print("\n3. Serie con todos los valores negativos. Prueba superada correctamente.")
print(f"Serie: {serie}")
print(f"Fuerza bruta: {resultado_fuerza}")
print(f"Divide y vencerás: {resultado_divide}")

# ---------------------------------------------------------
# 4. Serie con todos los valores positivos

serie = [3, 5, 2, 8, 4]

resultado_fuerza = subarreglo_fuerza_bruta(serie)
resultado_divide = subarreglo_maximo(serie, 0, len(serie) - 1)

# La mejor racha contiene todos los elementos
assert resultado_fuerza[2] == 22
assert resultado_divide[2] == 22

print("\n4. Serie con todos los valores positivos. Prueba superada correctamente.")
print(f"Serie: {serie}")
print(f"Fuerza bruta: {resultado_fuerza}")
print(f"Divide y vencerás: {resultado_divide}")

# ---------------------------------------------------------
# 5. Caso donde el mejor tramo cruza el punto medio

serie = [4, -1, 2, -1, 5]

resultado_fuerza = subarreglo_fuerza_bruta(serie)
resultado_divide = subarreglo_maximo(serie, 0, len(serie) - 1)

# El mejor tramo es toda la lista cuya suma es 9 y cruza el punto medio.
assert resultado_fuerza[2] == 9
assert resultado_divide[2] == 9

print("\n5. Caso donde el mejor tramo cruza el punto medio. Prueba superada correctamente.")
print(f"Serie: {serie}")
print(f"Fuerza bruta: {resultado_fuerza}")
print(f"Divide y vencerás: {resultado_divide}")

# ---------------------------------------------------------
# 6. Al menos veinte listas aleatorias

random.seed(42)

print("\n6. Al menos veinte listas aleatorias.")
# Generar al menos veinte listas aleatorias de longitud entre 1 y 30, con valores entre -100 y 100
for _ in range(20):
    longitud = random.randint(1, 30)

    serie = [
        random.randint(-100, 100)
        for _ in range(longitud)
    ]

    resultado_fuerza = subarreglo_fuerza_bruta(serie)
    resultado_divide = subarreglo_maximo(
        serie,
        0,
        len(serie) - 1
    )
    # Asegurarse de que ambos algoritmos produzcan la misma suma máxima
    assert resultado_fuerza[2] == resultado_divide[2]
    print(f"Serie: {serie}")
    print(f"Fuerza bruta: {resultado_fuerza}")
    print(f"Divide y vencerás: {resultado_divide}")

print("Todas las pruebas fueron superadas correctamente.")