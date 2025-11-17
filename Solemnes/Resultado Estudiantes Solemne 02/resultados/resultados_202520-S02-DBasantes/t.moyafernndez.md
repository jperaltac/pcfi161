# Evaluación de t.moyafernndez@uandresbello.edu
## Cálculo de la nota final

| Problema | Puntaje obtenido |
|---|---:|
| P1 | 1.14 |
| P2 | 1.26 |
| P3 | 0.57 |

- Problemas considerados: **3** (P1, P2, P3).
- Puntaje total obtenido: **2.97** puntos.
- Puntaje máximo posible: **4.50** puntos.
- Resultado de la fórmula: **4.96** → registrado como **5.0** en escala 1.0–7.0.

Fórmula aplicada: `1.0 + 6.0*(puntos)/(max_points)`

```python
scores = {'p1': 1.1400, 'p2': 1.2600, 'p3': 0.5700}
puntos = 2.9700
max_points = 4.5000
max = 4.5000
nota = 1.0 + 6.0*(puntos)/(max_points)
```

## Resumen
- Valor por item: 0.3
- Total ítems: 5
- **P1**: 1.14 ptos
- **P2**: 1.26 ptos
- **P3**: 0.57 ptos

**Nota final:** 5.0

## Detalle P1
```python
import matplotlib.pyplot as plt
thetha = np.linspace(0,2*np.pi,720)
#print(thetha)
a = 1 
e = 0.4
r = a*(1- e**2)/(1+ e *np.cos(thetha))
#print(r)
x = r * np.cos(thetha)
y = r * np.sin(thetha)
#print(x)
#print(y)
x_max = np.mean(x)
print(x_max)
y_max = np.mean(y)
print(y_max)
plt.plot(x,y,'g-', linewidth=2 , label='Orbita eliptica')
plt.title("Orbita eliptica parametrizada")
plt.ylabel("r*sin()")
plt.xlabel("r*cos()")
plt.grid(True)
```
- item 1: 0.24
- item 2: 0.24
- item 3: 0.24
- item 4: 0.18
- item 5: 0.24

**Total:** 1.14
**Comentarios:** En general cumple la lógica de cada apartado, usando operaciones vectorizadas y calculando los promedios. Sin embargo, falta importar numpy (el código no corre tal cual), la malla de theta incluye el punto 2π y no se fuerza endpoint=False, no se usa plt.axis('equal') y la ‘verificación’ de <x>,<y> sólo se imprime sin comprobar tolerancia. Por ello se descuentan décimas en cada punto afectado.
----
## Detalle P2
```python
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("stars_brightness.csv")
#print(df)
clase = df.groupby('spectral_class').agg({
  'temperature_K':['mean', 'std'],'magnitude_app': 'min'
}).round(2)
print(clase)
clase_ordenado = clase.sort_values(('temperature_K','mean'),ascending = False)
print(clase_ordenado)
plt.scatter(df['temperature_K'],df['magnitude_app'])
```
- item 1: 0.30
- item 2: 0.30
- item 3: 0.30
- item 4: 0.30
- item 5: 0.06

**Total:** 1.26
**Comentarios:** El código carga correctamente el CSV en un DataFrame, calcula las estadísticas por clase espectral, ordena por temperatura descendente y genera el scatter solicitado. Sin embargo, no incluye la interpretación pedida sobre la relación entre temperatura y brillo, por lo que el ítem 5 recibe un puntaje muy bajo.
----
## Detalle P3
```python
#print(T)
plt.scatter(a,T)
plt.xlabel("Semi eje Mayor")
plt.ylabel("Periodo Orbital")
plt.title("Ley Kepler")
plt.grid(True)
Ri = T / a**3/2
print(Ri.round(3))
Ri_prom = np.mean(Ri)
print(Ri_prom)
Ri_dsv = np.std(Ri_prom)
print(Ri_dsv)
```
- item 1: 0.30
- item 2: 0.18
- item 3: 0.09
- item 4: 0.00
- item 5: 0.00

**Total:** 0.57
**Comentarios:** Se genera correctamente el scatter con etiquetas y rejilla (item 1). Para el cociente R_i se intenta la operación y se redondea, pero la expresión T / a**3/2 no corresponde a T/(a**1.5), por lo que el valor es incorrecto; sin embargo hay esfuerzo y salida (item 2). Se calcula el promedio, pero la desviación estándar se aplica al promedio escalar en lugar del arreglo Ri, por lo que es errónea (item 3). No hay implementación para otros ítems.
----