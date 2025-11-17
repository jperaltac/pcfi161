# Evaluación de m.peagonzlez@uandresbello.edu
## Cálculo de la nota final

| Problema | Puntaje obtenido |
|---|---:|
| P1 | 0.63 |
| P2 | 0.42 |
| P3 | 0.36 |

- Problemas considerados: **3** (P1, P2, P3).
- Puntaje total obtenido: **1.41** puntos.
- Puntaje máximo posible: **4.50** puntos.
- Resultado de la fórmula: **2.88** → registrado como **2.9** en escala 1.0–7.0.

Fórmula aplicada: `1.0 + 6.0*(puntos)/(max_points)`

```python
scores = {'p1': 0.6300, 'p2': 0.4200, 'p3': 0.3600}
puntos = 1.4100
max_points = 4.5000
max = 4.5000
nota = 1.0 + 6.0*(puntos)/(max_points)
```

## Resumen
- Valor por item: 0.3
- Total ítems: 5
- **P1**: 0.63 ptos
- **P2**: 0.42 ptos
- **P3**: 0.36 ptos

**Nota final:** 2.9

## Detalle P1
```python
import numpy as np 
import matplotlib.pyplot as plt
a = 1.0 #UA 
e = 0.40
t = np.linspace(0,2*np.pi,720)
r = a * (1 - e**2) / [1 + e*np.cos(t)]
x = [r * np.cos(t)]
y = [r * np.sin(t)]
plt.axis("equal")
```
- item 1: 0.27
- item 2: 0.18
- item 3: 0.12
- item 4: 0.06
- item 5: 0.00

**Total:** 0.63
**Comentarios:** Se crea el arreglo con 720 puntos (endpoint incluido, pequeño desvío). Ecuación de r y coordenadas intentan ser vectorizadas, pero al usar corchetes se genera una lista y el código falla; se reconoce la intención. Solo se ajusta el aspecto del gráfico, pero no se dibuja la curva. No se calculan los valores medios.
----
## Detalle P2
```python
import numpy as np 
import pandas as pd 
df = pd.read_csv("stars_brightness.csv")
resultado = df.groupby
```
- item 1: 0.30
- item 2: 0.12
- item 3: 0.00
- item 4: 0.00
- item 5: 0.00

**Total:** 0.42
**Comentarios:** El código sólo carga el archivo correctamente (item 1). Item 2 muestra un intento muy básico (‘df.groupby’) sin cálculos, por lo que se otorgan 0.12. No se implementan ni el ordenamiento, ni el gráfico, ni la interpretación, así que esos ítems reciben 0.
----
## Detalle P3
```python
import numpy as np 
import matplotlib.pyplot as plt 
a = np.array([0.39, 0.72, 1.00, 1.52])
t = np.array([0.24, 0.61, 1.00, 1.88])
plt.scatter(a, t)
```
- item 1: 0.30
- item 2: 0.03
- item 3: 0.03
- item 4: 0.00
- item 5: 0.00

**Total:** 0.36
**Comentarios:** Se genera correctamente el gráfico solicitado. No se calculan ni se muestran los cocientes R_i, tampoco se obtiene el promedio ni la desviación estándar. Los ítems 4 y 5 no están presentes.
----