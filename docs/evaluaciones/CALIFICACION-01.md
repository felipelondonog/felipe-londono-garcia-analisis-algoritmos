# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Felipe Londoño García · **Laboratorio:** Fundamentos, complejidad y recurrencias (Plataforma Tamiza)
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `e7dd1fb`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 25 |
| Calidad de la explicación teórica | 16 / 25 |
| Corrección de la implementación | 9 / 20 |
| Calidad del análisis de las gráficas | 13 / 20 |
| Documentación y organización del informe | 6 / 10 |
| **Total** | **63 / 100** |
| **Nota (0–5)** | **3.15** |

## 1. Corrección conceptual (19 / 25)
**Lo que hizo bien:**
- Distingue entre un algoritmo correcto y uno eficiente y explica que duplicar el servidor solo reduce el tiempo a la mitad, sin cambiar cómo crece.
- Presenta un segundo ejemplo propio (la casa de apuestas) y, en la Parte 2, dos perjuicios con quién asume el costo: el paciente y los operadores.

**Lo que puede mejorar:**
- No nombra con claridad la restricción incumplida (terminar antes de las 6:00 a. m.).
- En el ejemplo de la casa de apuestas faltan la ventana de tiempo concreta y el tamaño de los datos que se incumplen.
- En el cálculo de energía hay un error: 10 minutos extra por 365 días son 3650 minutos, no 3640. Además no se habla de consumo de energía real (vatios, kWh).
- La reflexión sobre "a quién se llama primero" es muy corta.

## 2. Calidad de la explicación teórica (16 / 25)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)`, explica cada término y lo resuelve con el método maestro verificando la condición del caso 2.
- Escribe la predicción antes del experimento y la tabla de complejidades es correcta.

**Lo que puede mejorar:**
- Las definiciones de peor, mejor y caso promedio no dicen sobre qué conjunto de entradas se toma el máximo, el mínimo o el promedio.
- La cota de insertion sort no se calcula línea a línea: solo se muestra una captura de pantalla con resultados de n = 10 y frases generales. Faltan cuántas veces se ejecuta cada línea y la suma de costos.
- En 3.1 dice que usaría el peor caso, pero no lo relaciona con el escenario C ni con la ventana de cuatro horas.

## 3. Corrección de la implementación (9 / 20)
**Lo que hizo bien:**
- `insertion_sort` ordena bien, no cambia la lista recibida y cuenta bien las comparaciones.
- No usa `sorted()` ni `list.sort()`, y `merge_sort` tiene mezcla recursiva propia y ordena correctamente.

**Lo que puede mejorar:**
- `merge_sort` cuenta mal las comparaciones: solo cuenta las del primer nivel y descarta las de las llamadas internas (para 6400 datos da 6398, cuando debería ser cerca de 70.000).
- Los generadores no producen índices distintos: usan números al azar que se repiten (en 1000 datos solo hay unos 640 distintos).
- Agregó `insertion_sort_inverso` y dejó `insertion_sort` ordenando de menor a mayor, mientras que Tamiza necesita de mayor a menor. Funciona, pero no sigue la firma pedida y el experimento no usa la función oficial.
- Faltan *docstrings* en varias funciones y clases, no hay *type hints* completos, hay `import` antes del texto de descripción del módulo y numerosas líneas largas.

## 4. Calidad del análisis de las gráficas (13 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, están incrustadas, tienen título, leyenda y las curvas pedidas en los mismos ejes.
- Identifica con datos que B es el mejor caso, C el peor y A el intermedio, y lo contrasta con su predicción.
- Recomienda merge sort, cita el dato medido (n = 6400) para responder al servidor, y declara que la extrapolación es una estimación.

**Lo que puede mejorar:**
- La gráfica de comparaciones no tiene nombre en el eje vertical, y los ejes no indican unidades de los tamaños.
- Las cifras del texto (0.94 s, 1.63 s, 0.93 s) no coinciden del todo con lo que muestran las gráficas y las mediciones.
- Como `merge_sort` cuenta mal, no se puede usar el conteo de comparaciones para respaldar la conclusión.
- En la extrapolación de merge sort repite "0,93 s" y dice "cuadrático" por un descuido; el cálculo debía partir de 0,0165 s y de `n log n`.
- No explica el comportamiento de las curvas para tamaños pequeños ni menciona repetir las mediciones.
- Faltó la estimación en horas para merge sort frente a la ventana de cuatro horas, y la discusión de otras consideraciones (estabilidad, mantenimiento) es breve.

## 5. Documentación y organización del informe (6 / 10)
**Lo que hizo bien:**
- Siguió la ubicación acordada (`laboratorios/lab1-fundamentos-complejidad-recurrencias/`), tiene las partes en orden, enlaza el código de cada parte y las gráficas se ven.

**Lo que puede mejorar:**
- Las instrucciones dicen ejecutar `parte4_casos.py`, pero el archivo se llama `parte4_complejidad.py`.
- El informe incluye la imagen `venv_cmd.png`, que no está en el repositorio, así que no se ve.
- Solo hay 4 commits que tocan el laboratorio (se pedían al menos 5), y el último, "Creado READM.md", concentra casi todo el informe.
- Hay un archivo extra suelto (`insertion_sort_n_10.png`) fuera de la carpeta `graficas/`.

## ¿El código funciona?
Sí: los scripts corren sin errores y generan las gráficas. Los dos algoritmos ordenan bien, pero el conteo de comparaciones de merge sort es incorrecto y los lotes de datos tienen valores repetidos.

## Para el próximo laboratorio
- Sume las comparaciones de las llamadas recursivas en merge sort y verifíquelo con casos pequeños.
- Genere valores distintos (por ejemplo con `random.sample`) y use una sola función de ordenamiento con el sentido que declare.
- Escriba el análisis de insertion sort línea a línea, con cuántas veces se ejecuta cada línea.
- Revise ejes, unidades y cifras del informe contra lo que realmente produce el programa, y que cada imagen y comando exista.
- Haga commits más pequeños y frecuentes, con mensajes que describan cada avance, y añada type hints y docstrings a todas las funciones.
