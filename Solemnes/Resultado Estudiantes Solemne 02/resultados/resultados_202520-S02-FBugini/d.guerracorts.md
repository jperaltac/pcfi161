# Evaluación de d.guerracorts@uandresbello.edu
## Cálculo de la nota final

| Problema | Puntaje obtenido |
|---|---:|
| P1 | 1.35 |
| P2 | 0.78 |
| P3 | 0.60 |

- Problemas considerados: **3** (P1, P2, P3).
- Puntaje total obtenido: **2.73** puntos.
- Puntaje máximo posible: **4.50** puntos.
- Resultado de la fórmula: **4.64** → registrado como **4.6** en escala 1.0–7.0.

Fórmula aplicada: `1.0 + 6.0*(puntos)/(max_points)`

```python
scores = {'p1': 1.3500, 'p2': 0.7800, 'p3': 0.6000}
puntos = 2.7300
max_points = 4.5000
max = 4.5000
nota = 1.0 + 6.0*(puntos)/(max_points)
```

## Resumen
- Valor por item: 0.3
- Total ítems: 5
- **P1**: 1.35 ptos
- **P2**: 0.78 ptos
- **P3**: 0.60 ptos

**Nota final:** 4.6

## Detalle P1
```python
import pandas as pd 
a = 1.0
e = 0.40
theta = np.linspace(0, 2*np.pi, 720)
r = a*(1-e**2)/[1+e*np.cos(theta)]
 
x= r * np.cos(theta)
y = r* np.sin(theta)
plt.plot(x,y)
plt.axis('equal')
plt.title('orbita eliptica')
plt.xlabel('x (UA)')
plt.ylabel('y (UA)')
plt.show()
print('x =', np.mean(x))
print('y =', np.mean(y))
```
- item 1: 0.27
- item 2: 0.27
- item 3: 0.30
- item 4: 0.24
- item 5: 0.27

**Total:** 1.35
**Comentarios:** Buen uso de linspace (incluye 2π pero no afecta mucho), cálculo vectorizado de r aunque con sintaxis poco usual ([ ... ]), transformación a coordenadas cartesianas correcta. Gráfica con axis('equal') presente, pero faltan importaciones de NumPy y matplotlib, lo que impediría ejecutar el código tal cual; se descuenta un poco por ello. Se calculan y muestran los promedios <x> y <y>, cumpliendo la verificación de simetría. Código en general correcto con pequeños detalles.
----
## Detalle P2
```python
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv("stars_brightness.csv")
grupo = df.groupby('spectral_class')
resumen = grupo.agg(
  temperatura_promedio=('temperatura_k', 'mean'),
  desviacion_temp=('temperatura_k', 'std'),
  magnitud_min=('magnitude_app', 'min')
  ).reset_index()
  
resumen = resumen.sort_values('temperatura_promedio',asending=False)
print(resumen)
plt.scatter(df['temperature_k'],df['magnitude_app'])
plt.xlabel('temperature [K]')
plt.ylabel('magnitude aparente')
plt.show()
```
- item 1: 0.30
- item 2: 0.24
- item 3: 0.06
- item 4: 0.18
- item 5: 0.00

**Total:** 0.78
**Comentarios:** Lee correctamente el CSV (1). Calcula estadísticos por clase pero usa nombres de columnas distintos a los solicitados, aunque la lógica está (2). El ordenamiento falla por error tipográfico en 'ascending' y columna, por lo que probablemente arroja error (3). El scatter se intenta con nombres de columnas que podrían no existir; aun así la intención es clara (4). No hay ninguna interpretación escrita (5).
----
## Detalle P3
```python
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
a = np.array [0.39, 0.72, 1.00, 1.52]
t = np.array [0.24, 0.61, 1.00, 1.88]
plt.scatter(a,t)
plt.xlabel('unidades de medida')
plt.ylabel('años')
plt.show()
R = t**2/a**(3/2)
print('R',np.round(R,3))
print('promedio',np.mean(R))
print('desviacion', np.std(R))
```
- item 1: 0.24
- item 2: 0.18
- item 3: 0.18
- item 4: 0.00
- item 5: 0.00

**Total:** 0.60
**Comentarios:** El scatter está codificado, pero el uso incorrecto de np.array[...] impediría que se ejecute; por eso se descuenta ligeramente. El cociente R se calcula con T^2 en vez de T, por lo que la fórmula no es correcta; aun así se intenta redondear a 3 decimales. Se calculan promedio y desviación estándar, pero parten de un R erróneo. No hay ítems 4 y 5 definidos en la rúbrica, se dejan en 0.
----