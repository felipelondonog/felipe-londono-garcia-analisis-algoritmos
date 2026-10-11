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
Ejecute cada programa directamente desde el entorno de desarrollo, o ejecute los siguientes comando en la terminal ubicándose en el directorio laboratorios\lab2-divide-y-vencer:
- `python pruebas.py` > [Pruebas - Parte 1](pruebas.py)
- `python medicion.py` > [Medicion - Parte 2](medicion.py)

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

![alt text](graficas/tiempo_vs_n.png)

Para comparar el rendimiento de los algoritmos de fuerza bruta y divide y vencerás, se implementó el experimento en el archivo [Medicion.py](medicion.py). Se utilizaron seis tamaños de entrada: 10, 50, 100, 500, 1000 y 5000 elementos. Los datos se generaron mediante números enteros aleatorios entre -100 y 100, utilizando una semilla fija (42) para favorecer la reproducibilidad de las mediciones.

El tiempo de ejecución se midió con `time.perf_counter()`, registrando el tiempo inmediatamente antes y después de cada llamada a los algoritmos. Para cada tamaño se utilizó la misma lista de entrada en ambas implementaciones, lo que permite comparar sus tiempos bajo las mismas condiciones.

La gráfica compara los tiempos de ejecución de ambos algoritmos en función del tamaño de entrada. Se utilizaron escalas logarítmicas en los ejes horizontal y vertical para facilitar la visualización de las diferencias de rendimiento entre las dos soluciones.Los resultados permiten observar cómo varía el tiempo de ejecución al aumentar el tamaño de la entrada y comparar el comportamiento práctico de ambas implementaciones. La gráfica sirve como base para contrastar las mediciones con las complejidades teóricas de fuerza bruta, `θ(n^2)`, y divide y vencerás, `θ(nlog n)`.

# Parte 3 — Análisis en el README.md

## 3.1 Recurrencia
El algoritmo `subarreglo_maximo`, basado en divide y vencerás, divide el arreglo en dos mitades, resuelve recursivamente cada una y calcula el mejor subarreglo que cruza el punto medio. Su recurrencia es:
`T(n) = 2T(n/2)+θ(n)`

En este caso, `a=2`, `b=2` y `f(n) = θ(n)`, porque el cálculo del subarreglo cruzado requiere recorrer ambas mitades. Aplicando el teorema maestro, obtenemos `n^(logb a) = n^(log2 2) = n`. Como `f(n) = θ(n)`, corresponde al caso 2 y la complejidad resultante es `θ(nlogn)`.

Por otro lado, la fuerza bruta tiene complejidad `θ(n^2)`, puesto que examina todos los subarreglos posibles. Existen `n(n+1)/2` subarreglos y, al acumular las sumas incrementalmente, cada uno se procesa mediante una actualización constante. Por tanto, el número de operaciones crece cuadráticamente.

## 3.2 Lo medido contra lo esperado
La gráfica muestra que, a medida que aumenta el tamaño de entrada, el tiempo de fuerza bruta crece más rápidamente que el de divide y vencerás. Por ejemplo, al pasar de 500 a 1000 elementos, el tiempo de fuerza bruta aumenta aproximadamente de `0,0055` a `0,023` segundos, es decir, se multiplica por cuatro. Esto coincide con la predicción cuadrática, según la cual duplicar la entrada multiplica el tiempo por aproximadamente cuatro.

En divide y vencerás, el tiempo aumenta aproximadamente de `0,0007` a `0,0013` segundos, un factor cercano a `2`. Este comportamiento es compatible con la complejidad `θ(nlogn)`, que predice un factor aproximado de `2` al duplicar la entrada de 500 a 1000 elementos. Aunque las mediciones pueden variar por las condiciones del equipo, los resultados observados concuerdan con las tendencias teóricas.

## 3.3 Tamaños pequeños

Para `n = 10`, la gráfica muestra que fuerza bruta tarda aproximadamente `0,000008` segundos, mientras que divide y vencerás tarda `0,000027` segundos. En este caso, fuerza bruta es más rápido. Sin embargo, para `n = 50`, divide y vencerás ya presenta un tiempo ligeramente menor, de `0,000054` segundos contra el tiempo de `0,000058` segundos de fuerza bruta.

Esta diferencia se explica porque la complejidad asintótica describe el crecimiento para entradas grandes, pero no considera por sí sola los costes constantes. La recursión implica llamadas a funciones, división del problema y combinación de resultados. Para entradas pequeñas, estos costes pueden superar el trabajo adicional de fuerza bruta. El punto de equilibrio depende de la implementación.

## 3.4 ¿Cuándo conviene dividir?

Dividir un problema no garantiza una mejora del rendimiento. Por ejemplo, para encontrar el elemento máximo de un arreglo, se puede dividir la entrada en dos mitades y comparar los máximos obtenidos. La recurrencia sería `T(n) = 2T(n/2)+θ(1)`, cuya solución es `θ(n)`. Un recorrido iterativo también tiene complejidad `θ(n)`, pero evita la sobrecarga de la recursión.

Por tanto, divide y vencerás resulta conveniente cuando la división permite reducir el trabajo total, resolver subproblemas independientes o aprovechar una estructura que facilite su combinación. La elección debe considerar tanto la complejidad teórica como los costes prácticos de implementación.

## 3.5 Recomendación para la gerente

Recomendaría utilizar divide y vencerás para analizar los historiales de la cooperativa, porque sus mediciones muestran un mejor rendimiento para entradas grandes y su complejidad crece más lentamente. Según la gráfica, para 5000 elementos, fuerza bruta tarda aproximadamente `0,56` segundos, mientras que divide y vencerás tarda `0,007` segundos.

Para estimar el comportamiento con un millón de registros, podemos extrapolar estos valores utilizando las complejidades teóricas. Para fuerza bruta:

`T(10^6) ≈ 0,5(10^6/5000)^2 = 20000s`

Esto equivale aproximadamente a 5,6 horas. Para divide y vencerás:

`T(10^6) ≈ 0,007(10^6*log(10^6)/5000log(5000)) ≈ 2,1s`

Estas cifras son estimaciones, no mediciones directas. Además, deben interpretarse con cautela, especialmente porque el comportamiento real puede variar según la implementación y el equipo. Aun así, los resultados respaldan la elección de divide y vencerás para procesar entradas grandes.