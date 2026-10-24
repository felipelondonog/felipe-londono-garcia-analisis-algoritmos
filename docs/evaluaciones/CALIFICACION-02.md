# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Felipe Londoño García · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `0916ff9`

Muy buen trabajo: las dos soluciones funcionan y su informe se apoya en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 17 / 20 |
| Calidad de la explicación teórica | 16 / 20 |
| Corrección de la implementación | 22 / 25 |
| Calidad del análisis de las gráficas | 22 / 25 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **85 / 100** |
| **Nota (0–5)** | **4.25** |

## 1. Corrección conceptual (17 / 20)
**Lo que hizo bien:**
- Identifica que divide y vencerás empieza a ganar hacia n = 50 y explica por qué en n = 10 pierde (costo de las llamadas recursivas).
- En el ejemplo del máximo de un arreglo plantea `T(n) = 2T(n/2) + Θ(1)` y concluye `Θ(n)`.
- Recomienda divide y vencerás y da una estimación para 1.000.000 de registros, declarada como estimación.

**Lo que puede mejorar:**
- En la pregunta 4 diga con claridad que dividir NO mejora el máximo: el costo de combinar es constante y el resultado es el mismo `Θ(n)`.
- En la cuenta de fuerza bruta a 1.000.000 usa `0,5 s` como base, pero antes dijo `0,56 s`; con ese valor el resultado cambia (unas 6 horas).

## 2. Calidad de la explicación teórica (16 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)`, aplica el método maestro (caso 2) y obtiene `Θ(n log n)`.
- Justifica el `Θ(n²)` de la fuerza bruta contando los `n(n+1)/2` tramos.

**Lo que puede mejorar:**
- Explique de dónde sale cada término: por qué son 2 subproblemas, por qué de tamaño n/2 y por qué el caso cruzado cuesta `Θ(n)`.
- Escriba la verificación del caso 2 de forma explícita: `f(n)` es del mismo orden que `n^(log_b a)`.

## 3. Corrección de la implementación (22 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden en las listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos sin usar la fuerza bruta y no modifica la lista.
- `pruebas.py` cubre todos los casos pedidos.

**Lo que puede mejorar:**
- Faltan dos líneas en blanco entre funciones en `subarreglo.py` y `medicion.py`.
- `medicion.py` no sigue el estilo de docstring pedido (Args/Returns bien formados) y `main` no tiene tipo de retorno.

## 4. Calidad del análisis de las gráficas (22 / 25)
**Lo que hizo bien:**
- La gráfica tiene ambas curvas en los mismos ejes, título, ejes rotulados y leyenda, con seis tamaños.
- Los valores que cita coinciden con la gráfica (por ejemplo, fuerza bruta cerca de 0,023 s y divide y vencerás cerca de 0,0014 s en n = 1000).
- Calcula el factor al duplicar n (500 a 1000) y lo contrasta con `Θ(n²)` y `Θ(n log n)`.

**Lo que puede mejorar:**
- Un solo par de tamaños es poca evidencia; compare también otros pares.
- La medición se hizo una sola vez por tamaño; repetirla y promediar reduce el ruido, y debió decirlo en el informe.
- El experimento no comprueba que ambos algoritmos den la misma suma en cada tamaño (solo la imprime).

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- Carpeta bien ubicada, con todos los archivos pedidos, enlaces al código y gráfica incrustada que se ve.
- Instrucciones de reproducción presentes y 7 commits sobre el laboratorio.

**Lo que puede mejorar:**
- La imagen `venv_cmd.png` del README no existe en esta carpeta, así que no se ve.
- Las instrucciones hablan de "ejercicio de clase" y de `requirements.txt` en un lugar que no corresponde a este laboratorio; ajústelas.

## ¿El código funciona?
Sí. Las pruebas pasan, ambas funciones coinciden en listas aleatorias y la medición corre y genera la gráfica.

## Para el próximo laboratorio
- Explique cada término de las recurrencias, no solo el resultado.
- Compare varios pares de tamaños y repita las mediciones.
- Verifique en el propio experimento que los resultados coinciden.
- Deje dos líneas en blanco entre funciones y revise que los docstrings tengan Args y Returns y que todas las funciones tengan type hints.
- Compruebe que las imágenes del README se vean antes de entregar.
