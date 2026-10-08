### Felipe Londoño García - Carné 21158186
### Grupo - 190304006-3

# Instrucciones para reproducir el experimento

## ¿Cómo preparar el entorno para el ejercicio de clase?
1. Inicie el entorno virtual, ejecute los comandos en CMD:
    - `python -m venv venv` para crearlo
    - `venv\Scripts\activate` para iniciarlo en Windows
    - `source venv/bin/activate` para iniciarlo en Linux/Mac
  
2. Asegúrese que el entorno virtual está activo. La terminal debería mostrar el texto (venv) como se ve en la imagen:
![](venv_cmd.png)

3. Instale las librerías del archivo de requerimientos. Ejecute en la terminal `pip install -r requirements.txt`

## Ejecute los archivos de Python
Ejecute cada programa directamente desde el entorno de desarrollo, o ejecute los los siguientes comando en la terminal:
- `pruebas.py`

>Al ejecutarse, cada programa imprimirá en la terminal el resultado de los rendimientos de cada experimento y mostrará en pantalla las gráficas, las cuáles además se guardan en la carpeta /graficas.

# Parte 1 — Implementar y verificar las dos soluciones

Link a las implementaciones:
- [Subarreglo.py](subarreglo.py)
- [Pruebas.py](pruebas.py)

Para verificar la correcta implementación de los algoritmos de fuerza bruta y divide y vencerás implementados en [Subarreglo.py](subarreglo.py), se creó el archivo [Pruebas.py](pruebas.py), el cual contiene pruebas automatizadas mediante instrucciones `assert`. En cada caso se comparó principalmente la suma máxima obtenida, ya que el enunciado establece que, cuando existen varios subarreglos con la misma suma óptima, cualquiera de ellos es válido.

Las pruebas cubren los siguientes escenarios:

1. Serie de ejemplo de la situación problema: `[-3, 5, -2, 8, -6, 3, 9, -4]`, verificando que ambos algoritmos obtengan una suma máxima de `17`.
2. Serie con un único elemento, para validar el caso base de la solución recursiva.
3. Serie con todos los valores negativos, comprobando que el algoritmo seleccione correctamente el valor menos negativo.
4. Serie con todos los valores positivos, donde la solución óptima corresponde a toda la lista.
5. Caso en el que el mejor subarreglo cruza el punto medio, con el fin de verificar la correcta implementación del caso cruzado en el algoritmo de divide y vencerás.
6. Veinte listas aleatorias reproducibles, generadas con una semilla fija, en las cuales se comprobó que ambos algoritmos producen exactamente la misma suma máxima.

Estas pruebas permitieron validar tanto la corrección de los resultados como el cumplimiento de las restricciones establecidas en el laboratorio, especialmente la correcta resolución de los casos izquierdo, derecho y cruzado en el algoritmo de divide y vencerás.

# Parte 2 - Medir y graficar

# Parte 3 — Análisis en el README.md