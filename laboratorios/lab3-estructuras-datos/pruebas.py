import random
from estructuras import ListaEnlazada, TablaHash

def poblar_estructuras(guias: list[int], estados: list[str]) -> tuple[ListaEnlazada, TablaHash]:
    """Puebla una lista enlazada y una tabla hash con guías y estados.
    Args:
        guías: lista de guías a insertar.
        estados: lista de estados correspondientes a las guías.

    Returns:
        Una tupla con la lista enlazada y la tabla hash pobladas.
    """

    lista_enlazada = ListaEnlazada() 
    tabla_hash = TablaHash(7) # Se establece m = 7 para todas las pruebas con tablas hash

    for n in range(len(guias)):
        lista_enlazada.insertar(guias[n], estados[n])
        tabla_hash.insertar(guias[n], estados[n])

    return lista_enlazada, tabla_hash

# --------------Parte 1-------------- #
# Prueba de búsqueda exitosa y fallida en Lista Enlazada y Tabla Hash.
# Si la guía no existe, debe retornar None, si existe, debe retornar el estado.

print("-- Prueba de búsqueda en ListaEnlazada y TablaHash --")

guias = [10, 24, 17]
estados = ["En bodega", "Entregado", "En camino"]

lista_enlazada, tabla_hash = poblar_estructuras(guias, estados)

# Insertar guías en la lista enlazada
assert lista_enlazada.buscar(24) == "Entregado"
assert lista_enlazada.buscar(99) is None
assert tabla_hash.buscar(17) == "En camino"
assert tabla_hash.buscar(11) is None

print("Pruebas de búsqueda (exitosa y fallida) en ListaEnlazada y TablaHash pasadas.")
print(f"Lista enlazada: Guía {24}: {lista_enlazada.buscar(24)}")
print(f"Lista enlazada: Guía {99}: {lista_enlazada.buscar(99)}")
print(f"Tabla hash: Guía {17}: {tabla_hash.buscar(17)}")
print(f"Tabla hash: Guía {11}: {tabla_hash.buscar(11)}\n")


# --------------Parte 2-------------- #
# Colisión forzada en TablaHash: m = 7, guías = [10, 24, 17]
# Todas deben colisionar en la casilla 3

print("-- Prueba de colisión forzada en TablaHash --")
guias = [10, 24, 17]
estados = ["En bodega", "Entregado", "En camino"]
_, tabla_hash = poblar_estructuras(guias, estados)

for i in range(len(guias)):
    # Verificar que las 3 guías se pueden buscar
    guia_actual = guias[i]
    assert tabla_hash.buscar(guia_actual) == estados[i]
    print(f"Guía {guia_actual}: {tabla_hash.buscar(guia_actual)}")
    
    # Verificar que todas las guías colisionan en la casilla 3
    casilla = tabla_hash.hash(guia_actual)
    assert casilla == 3
    print(f"\tUbicada en la casilla {casilla}, con tamaño de lista {tabla_hash.casillas[casilla].tamano}")

print("\nPruebas de colisión forzada en Tabla Hash exitosas, los datos se ingresaron y buscaron correctamente."
      "\nLas listas de cada casilla tienen tamaño = 3 ")


# --------------Parte 3-------------- #
# Prueba de factor de carga, debe ser igual a 3/7 ≈ 0.4286

print("\n-- Prueba de factor de carga --")
assert tabla_hash.factor_carga() == 3 / 7
print(f"Factor de carga: {tabla_hash.factor_carga()} ≈ 3/7")


# ---------------Parte 4 ------------- #
# Prueba con al menos 20 colecciones aleatoria existentes e inexistentes.
# La lista y la tabla deben devolver lo mismo.

print("\n-- Prueba aleatoria con 20 colecciones --")

random.seed(42)
rango_min, rango_max = 1000000000, 1000000040 # rango para asignar las guías aleatorias de 10 dígitos
estados = ["En bodega", "Entregado", "En camino", "Retrasado", "En aduana"]

guias_random = random.sample(range(rango_min, rango_max), 20) # Escoge 20 números aleatorios sin repetir dentro del rango
estados_random = random.choices(estados, k=20)

lista_random, tabla_random = poblar_estructuras(guias_random, estados_random)

# Verificar que efectivamente ambas estructuras tengas los mismos datos y devuelvan lo mismo al ser consultadas
# Busca todos los números de guías en el rango para también hacer consultas sin resultado
j = 1
for i in range(rango_min, rango_max):
    assert lista_random.buscar(i) == tabla_random.buscar(i)
    print(f"{j})\tLista enlazada: Número de guía {i} - Estado:{lista_random.buscar(i)}")
    print(f"\tTabla Hash: Número de guía {i} - Estado:{tabla_random.buscar(i)}")
    j += 1

print("Prueba aleatoria pasada con éxito.")
print("Todas las pruebas fueron exitosas.")



