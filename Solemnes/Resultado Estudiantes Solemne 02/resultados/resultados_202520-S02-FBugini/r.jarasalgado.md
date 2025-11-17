# Evaluación de r.jarasalgado@uandresbello.edu
## Cálculo de la nota final

| Problema | Puntaje obtenido |
|---|---:|
| P1 | 0.18 |
| P2 | 0.36 |
| P3 | 0.18 |

- Problemas considerados: **3** (P1, P2, P3).
- Puntaje total obtenido: **0.72** puntos.
- Puntaje máximo posible: **4.50** puntos.
- Resultado de la fórmula: **1.96** → registrado como **2.0** en escala 1.0–7.0.

Fórmula aplicada: `1.0 + 6.0*(puntos)/(max_points)`

```python
scores = {'p1': 0.1800, 'p2': 0.3600, 'p3': 0.1800}
puntos = 0.7200
max_points = 4.5000
max = 4.5000
nota = 1.0 + 6.0*(puntos)/(max_points)
```

## Resumen
- Valor por item: 0.3
- Total ítems: 5
- **P1**: 0.18 ptos
- **P2**: 0.36 ptos
- **P3**: 0.18 ptos

**Nota final:** 2.0

## Detalle P1
```python
import numpy as np  
a = 1.0 UA # (UA=unidad astronómica)
e = 0.40   # (excentricidad; si e = 0, la órbita es circular)
# A: 
theta =
```
- item 1: 0.06
- item 2: 0.03
- item 3: 0.03
- item 4: 0.03
- item 5: 0.03

**Total:** 0.18
**Comentarios:** El programa se queda a la mitad: solo importa NumPy y define constantes; la creación de theta está inconclusa y no hay cálculos posteriores ni la gráfica ni la verificación de los promedios. Se reconoce un esfuerzo mínimo por comenzar (item 1), pero el resto de los requisitos no se abordan.
----
## Detalle P2
```python
import numpy as numpy
import pandas as pd  
# Leer archivo en un dataframe 
df = pd.read_csv("stars_brightness.csv")
#print(df)
# Para cada clase espectral calcular
temperature_K = ("temperatura promedio")
temperature_K = ("std")
spectral_class = ("magnitude")
```
- item 1: 0.30
- item 2: 0.06
- item 3: 0.00
- item 4: 0.00
- item 5: 0.00

**Total:** 0.36
**Comentarios:** Se lee correctamente el archivo con pandas (0.30). Para los cálculos por clase espectral solo hay asignaciones de texto, sin groupby ni operaciones numéricas; se valora como intento muy pobre (0.06). No hay ordenamiento, ni gráfico, ni interpretación, por lo que esos ítems obtienen 0.00.
----
## Detalle P3
```python
import numpy as np  
k = 1
x = np.array("0.39, 0.72, 1.00, 1.52") # semieje mayor a [UA]
y = np.array("0,24, 0.61, 1.00, 1.88") # período orbital T [años]
y = k*x**(3/2)
#print(x,y)
plt.scatter(x,y)
```
- item 1: 0.12
- item 2: 0.03
- item 3: 0.03
- item 4: 0.00
- item 5: 0.00

**Total:** 0.18
**Comentarios:** El código intenta graficar pero los datos están mal construidos (strings en lugar de floats) y falta importar matplotlib, por lo que el scatter no se genera correctamente. No calcula R_i ni su promedio ni desviación estándar. No hay más ítems abordados.
----