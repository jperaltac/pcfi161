# Evaluación de e.portillocarrasco@uandresbello.edu
## Cálculo de la nota final

| Problema | Puntaje obtenido |
|---|---:|
| P1 | 1.02 |
| P2 | 0.42 |
| P3 | 0.00 |

- Problemas considerados: **3** (P1, P2, P3).
- Puntaje total obtenido: **1.44** puntos.
- Puntaje máximo posible: **4.50** puntos.
- Resultado de la fórmula: **2.92** → registrado como **2.9** en escala 1.0–7.0.

Fórmula aplicada: `1.0 + 6.0*(puntos)/(max_points)`

```python
scores = {'p1': 1.0200, 'p2': 0.4200, 'p3': 0.0000}
puntos = 1.4400
max_points = 4.5000
max = 4.5000
nota = 1.0 + 6.0*(puntos)/(max_points)
```

## Resumen
- Valor por item: 0.3
- Total ítems: 5
- **P1**: 1.02 ptos
- **P2**: 0.42 ptos
- **P3**: 0.00 ptos

**Nota final:** 2.9

## Detalle P1
```python
import matplotlib.pyplot as plt 
x=np.linspace(0, 2*np.pi, 720)
r = 1.0 * (1- 0.40**2) / (1 + 0.40 * np.cos(x))
X = r * np.cos(x)
y = r * np.sin(x)
plt.plot(x, y, linewidth=4, label="X", color="blue")
plt.scatter(x="x", y="y")
plt.xlabel("x", fontsize=0.2)
plt.ylabel("y", fontsize=0.5)
plt.axis("equal")
plt.grid(True, alpha=0.6)
plt.legend()
plt.show()
print(f"La media de x es: {np.mean(x)}")
print(f"la media de y es: {np.mean(y)}")
print(f"Datos de las orbitas: {r}")
print(f"Coordenadas seno: {x}")
print(f"Coordenadas cos: {y}")
```
- item 1: 0.27
- item 2: 0.30
- item 3: 0.27
- item 4: 0.12
- item 5: 0.06

**Total:** 1.02
**Comentarios:** Se crea el arreglo θ con 720 puntos y el radio de forma vectorizada. Las coordenadas cartesianas se calculan, aunque con nombres confusos. Al graficar se usa θ en vez de X, el scatter es erróneo y falta la importación de NumPy, por lo que la figura no es la órbita esperada. La comprobación de medias usa θ en lugar de x_cartesiano, así <x> no resulta ≈0.
----
## Detalle P2
```python
import numpy as np 
import pandas as pd 
df = pd.read_csv("stars_brightness.csv")
print(df.describe())
print(df.head())
print(df.info())
print(df['temperature_K'].np.mean())
print(df['temperature_K'].np.std())
print(df.['magnitude_app'].np.min())
```
- item 1: 0.30
- item 2: 0.12
- item 3: 0.00
- item 4: 0.00
- item 5: 0.00

**Total:** 0.42
**Comentarios:** Se lee correctamente el CSV en un DataFrame. Se intenta calcular estadísticas, pero no se agrupa por spectral_class y además contiene errores de sintaxis; por eso se otorga un puntaje bajo. No hay intento de ordenar la tabla, crear el scatter o interpretar resultados.
----
## Detalle P3
```python
# Sin código
```

**Total:** 0.00
**Comentarios:** Este ejercicio no tuvo respuesta
----