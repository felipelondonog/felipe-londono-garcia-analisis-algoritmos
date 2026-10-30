### Felipe Londoño García - Carné 21158186
### Grupo - 190304006-3

# Laboratorio #3 - Estructuras de datos

## Instrucciones para reproducir el experimento

### ¿Cómo preparar el entorno para correr los programas?
1. Inicie el entorno virtual, ejecute los comandos en CMD:
    - `python -m venv venv` para crearlo
    - `venv\Scripts\activate` para iniciarlo en Windows
    - `source venv/bin/activate` para iniciarlo en Linux/Mac

2. Instale las librerías del archivo de requerimientos en caso de no tenerlas instaladas. Ejecute en la terminal `pip install -r requirements.txt`

### Ejecute los archivos de Python
Ejecute cada programa directamente desde el entorno de desarrollo, o ejecute los siguientes comando en la terminal ubicándose en el directorio laboratorios\lab3-estructuras-datos:
- `python pruebas.py` -> [Ir a implementación de Parte 1 - Pruebas](pruebas.py)
- `python medicion.py` -> [Ir a implementación de Parte 2 - Medición](medicion.py)

>Al ejecutarse, cada programa imprimirá en la terminal el resultado de los rendimientos de cada experimento y mostrará en pantalla las gráficas, las cuáles además se guardan en la carpeta /gráficas.

# Parte 1 — Implementar y verificar las dos estructuras
[Ir a estructuras.py](estructuras.py)

[Ir a pruebas.py](pruebas.py)

Con el fin de verificar el correcto funcionamiento de las estructuras de datos desarrolladas en [estructuras.py](estructuras.py), se desarrollaron un conjunto de pruebas automatizadas en [pruebas.py](pruebas.py) usando instrucciones `assert` para comprobar que las funciones desarrolladas arrojan los resultados esperados.

Para la ejecución de las pruebas se desarrolló el método `poblarEstructuras()` para reducir la duplicidad de código en las pruebas, el método recibe un arreglo de guías y estados, y devuelve una lista enlazada y una tabla hash con los datos ingresados (la tabla hash recibe m = 7 por defecto).

Las pruebas se desarrollaron en 4 partes:

1. **Búsquedas exitosas y fallidas:**
   Se crearon dos arreglos con 3 guías y 3 estados para poblar las estructuras. Con la instrucción `assert` se verificó que al consultar por determinados números de guías en ambas colecciones, las búsquedas arrojan el resultado esperado o arrojan None si no existe el elemento.
2. **Colisiones en la TablaHash:**
   Se estableció `m = 7` y `guías = [10, 24, 17]` con el objetivo de que todas las guías colisionen en la casilla 3. Luego de poblar la tabla hash, se recorre la misma con un ciclo `for` para todas las guías. Por cada guía se evalúa si evalúa si la tabla devuelve el estado que corresponde para esa posición. Además, se verifica que cada guía realmente esté almacenada en la casilla 3.
3. **Prueba de factor de carga:**
    Esta prueba verifica que el factor de carga de la tabla hash corresponde al factor esperado teórico, que corresponde a `3/7` (número de guías sobre número de casillas). El resultado experimental es `0.4286...` que es igual a `3/7`.
4. **Pruebas con colecciones aleatorias:**
   Usando la función `random`, se generaron 20 guías aleatorias, y usando un arreglo por defecto con 5 estados, se llenó un arreglo `estados_random` con una selección aleatoria de 20 estados de los 5 por defecto. Se estableció un rango de 40 números de guías (de 10 dígitos) para que sean 20 guías las seleccionadas aleatoriamente, por lo tanto otras 20 guías dentro de este rango no deben existir. Usando un ciclo for, se recorre el rango de guías, y con una función `assert` se evalúa que el estado obtenido de la lista enlazada y la tabla hash sea el mismo para cada número de guía, incluyendo los que deben arrojar `None`.


# Parte 2 - Medir y graficar
[Ir a medición.py](medicion.py)

# Parte 3 - Análisis
## 1. Costo teórico
## 2. Lo medico contra lo esperado
## 3. Explique las colisiones
## 4. Tabla hash o árbol de búsqueda
## 5. Concepto para la jefa de operaciones