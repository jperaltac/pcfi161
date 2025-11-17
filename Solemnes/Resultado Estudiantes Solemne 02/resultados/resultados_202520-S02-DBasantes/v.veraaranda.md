# Evaluación de v.veraaranda@uandresbello.edu
## Cálculo de la nota final

| Problema | Puntaje obtenido |
|---|---:|
| P1 | 1.00 |
| P2 | 0.39 |
| P3 | 0.18 |

- Problemas considerados: **3** (P1, P2, P3).
- Puntaje total obtenido: **1.57** puntos.
- Puntaje máximo posible: **4.50** puntos.
- Resultado de la fórmula: **3.09** → registrado como **3.1** en escala 1.0–7.0.

Fórmula aplicada: `1.0 + 6.0*(puntos)/(max_points)`

```python
scores = {'p1': 1.0000, 'p2': 0.3900, 'p3': 0.1800}
puntos = 1.5700
max_points = 4.5000
max = 4.5000
nota = 1.0 + 6.0*(puntos)/(max_points)
```

## Resumen
- Valor por item: 0.3
- Total ítems: 5
- **P1**: 1.00 ptos
- **P2**: 0.39 ptos
- **P3**: 0.18 ptos

**Nota final:** 3.1

## Detalle P1
```python
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
a = 1.0 
e = 0.40 
theta = np.linspace(0,2*np.pi, 720)
r = a * (1 - e**2) / (1 + e * np.cos(theta))
x = r * np.cos(theta)
y = r * np.sin(theta)
plt.axis("equal")
```
- item 1: 0.28
- item 2: 0.30
- item 3: 0.30
- item 4: 0.09
- item 5: 0.03

**Total:** 1.00
**Comentarios:** Cumple casi por completo la generación de theta (incluye 2π, pequeño desvío). El cálculo vectorizado de r y las coordenadas cartesianas están correctos. Para la gráfica solo configura el aspecto igual pero no dibuja los puntos, por lo que se otorga puntaje bajo. No se calculan los promedios <x>,<y>.
----
## Detalle P2
```python
import numpy as np
import pandas as pd
df = pd.read_csv("stars_brightness.csv")
df[['temperatura_K','magnitude_app','spectral_class']]
print(df)
```
- item 1: 0.27
- item 2: 0.03
- item 3: 0.03
- item 4: 0.03
- item 5: 0.03

**Total:** 0.39
**Comentarios:** El código solo lee el CSV en un DataFrame (bien cumplido). No realiza los cálculos por clase espectral, ni ordena resultados, ni genera el scatter, ni incluye interpretación. Solo hay un intento mínimo de seleccionar columnas, por lo que se otorga el puntaje mínimo de cortesía en los ítems 2-5.
----
## Detalle P3
```python
import numpy as np 
import matplotlib.pyplot as plt 
s = np.array[0.39, 0.72, 1.00, 1.52]
p = np.array[0.24, 0.61, 1.00, 1.88]
T = k * a**(3/2)
plt.scatter()
```
- item 1: 0.06
- item 2: 0.03
- item 3: 0.03
- item 4: 0.03
- item 5: 0.03

**Total:** 0.18
**Comentarios:** Se importan las librerías y se intenta definir datos y hacer un scatter, pero la sintaxis de np.array es incorrecta, no se pasan argumentos a plt.scatter, no se calculan R_i ni sus estadísticas y no hay otros elementos pedidos. Solo se reconoce un intento muy básico.
----