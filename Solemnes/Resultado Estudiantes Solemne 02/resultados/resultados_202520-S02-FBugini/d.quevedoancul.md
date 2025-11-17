# Evaluación de d.quevedoancul@uandresbello.edu
## Cálculo de la nota final

| Problema | Puntaje obtenido |
|---|---:|
| P1 | 0.54 |
| P2 | 0.57 |
| P3 | 0.57 |

- Problemas considerados: **3** (P1, P2, P3).
- Puntaje total obtenido: **1.68** puntos.
- Puntaje máximo posible: **4.50** puntos.
- Resultado de la fórmula: **3.24** → registrado como **3.2** en escala 1.0–7.0.

Fórmula aplicada: `1.0 + 6.0*(puntos)/(max_points)`

```python
scores = {'p1': 0.5400, 'p2': 0.5700, 'p3': 0.5700}
puntos = 1.6800
max_points = 4.5000
max = 4.5000
nota = 1.0 + 6.0*(puntos)/(max_points)
```

## Resumen
- Valor por item: 0.3
- Total ítems: 5
- **P1**: 0.54 ptos
- **P2**: 0.57 ptos
- **P3**: 0.57 ptos

**Nota final:** 3.2

## Detalle P1
```python
import numpy as np 
import matplotlib.pyplot as plt 
# Datos
a = 1.0   # (UA = unidad astronomica)
e = 0.40   # (excrentricidad; si e = 0, la orbita es circular)
# Datos para el grafico
b = np.linspace(0, 2*np.pi, 720)  # Crear arreglo theta
r = a * (1 - np.e**2)/[1 + np.e * np.cos(x)]
# Coordenadas cartesianas 
x = r * np.cos(0)
y = r * np.sin(0)
# Grafico 
plt.axis("equal")
plt.show
# Valores nedio de "x" e "y" con Numpy
```
- item 1: 0.27
- item 2: 0.12
- item 3: 0.06
- item 4: 0.06
- item 5: 0.03

**Total:** 0.54
**Comentarios:** Se creó el arreglo con linspace, aunque incluye el punto final y se nombró 'b', no 'theta' (leve descuento). El cálculo de r falla: usa np.e en vez del parámetro e y una variable x inexistente; el intento es reconocible pero incorrecto. Las coordenadas cartesianas se evalúan en θ=0, por lo que no generan la órbita; intento mínimo. No se grafican puntos, sólo se fija axis y ni se llama plt.show(), por lo que la visualización no aparece. No se calculan los promedios <x>,<y>.
----
## Detalle P2
```python
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
# a. Leer el archivo DataFrame
df = pd.read_csv("stars_brightness.csv") 
df.info()
# b. Calcular para cada "spectral_class"
df.groupby("spectral_class")
# Ordenar la tabla "temperature_K" de mayor a menor
# Grafico de dispersión
plt.scatter(x= temperature_K, y= magnitude_app, color="red", alpha= 0.5)
plt.xlabel("temperature_K")
plt.ylabel("magnitude_app")
plt.title("Grafico de dispersión de estrellas")
plt.show()
```
- item 1: 0.30
- item 2: 0.12
- item 3: 0.03
- item 4: 0.12
- item 5: 0.00

**Total:** 0.57
**Comentarios:** Se lee correctamente el CSV en un DataFrame (0.30). Se inicia un groupby pero no se realizan las agregaciones solicitadas (0.12). No se implementa la ordenación, solo un comentario (0.03). El scatter se intenta, pero las variables no existen, por lo que fallaría (0.12). Falta por completo la interpretación (0.00).
----
## Detalle P3
```python
import numpy as np 
import matplotlib.pyplot as plt 
# Datos                                                 
a = np.array([0.39, 0.72, 1.00, 1.52]) # Semieje mayor a UA [unidades astronomicas]
T = np.array([0.24, 0.61, 1.00, 1.88]) # Periodo orbital T [años]
# Grafico de dispersion 
plt.scatter(x= a, y= T, color="red", alpha=0.7)
plt.xlabel("Semieje Mayor [UA]")
plt.ylabel("Periodo Orbital [T]")
plt.show()
# Calcular para cada planeta
R = T/(a)**(3/2)
print(R)
# Calcular promedio y desviacion estandar de los R
```
- item 1: 0.30
- item 2: 0.24
- item 3: 0.03
- item 4: 0.00
- item 5: 0.00

**Total:** 0.57
**Comentarios:** Se genera correctamente el gráfico scatter (item 1). Se calculan y muestran los R_i, pero sin el formato solicitado de 3 decimales, por lo que se otorga puntaje parcial (item 2). No se calcula ni el promedio ni la desviación estándar, apenas se avanza hasta obtener R, de ahí la mínima puntuación posible (item 3). Los ítems 4 y 5 no están definidos en la rúbrica y no se evidencian en el código, por lo que reciben 0.
----