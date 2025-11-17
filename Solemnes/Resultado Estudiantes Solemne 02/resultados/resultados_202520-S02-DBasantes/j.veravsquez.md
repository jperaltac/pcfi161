# Evaluación de j.veravsquez@uandresbello.edu
## Cálculo de la nota final

| Problema | Puntaje obtenido |
|---|---:|
| P1 | 1.41 |
| P2 | 0.45 |
| P3 | 0.84 |

- Problemas considerados: **3** (P1, P2, P3).
- Puntaje total obtenido: **2.70** puntos.
- Puntaje máximo posible: **4.50** puntos.
- Resultado de la fórmula: **4.60** → registrado como **4.6** en escala 1.0–7.0.

Fórmula aplicada: `1.0 + 6.0*(puntos)/(max_points)`

```python
scores = {'p1': 1.4100, 'p2': 0.4500, 'p3': 0.8400}
puntos = 2.7000
max_points = 4.5000
max = 4.5000
nota = 1.0 + 6.0*(puntos)/(max_points)
```

## Resumen
- Valor por item: 0.3
- Total ítems: 5
- **P1**: 1.41 ptos
- **P2**: 0.45 ptos
- **P3**: 0.84 ptos

**Nota final:** 4.6

## Detalle P1
```python
import matplotlib.pyplot as plt
import numpy as np
a=1.0 
e=0.40
theta=np.linspace(0,2*np.pi,720)
r=(a*(1-e**2))/(1+e*np.cos(theta))
x=r*np.cos(theta)
y=r*np.sin(theta)
plt.plot(x,y,'r-',)
plt.title("orbita")
plt.xlabel("cos(theta)")
plt.ylabel("sin(theta)")
plt.axis('equal')
plt.show
valor_mediox=np.mean(x) 
valor_medioy=np.mean(y)
print("El valor medio para x es: " , valor_mediox ,"cercano a 0" )
print("El valor medio par y es:" ,valor_medioy , "cercano a 0")
```
- item 1: 0.27
- item 2: 0.30
- item 3: 0.30
- item 4: 0.24
- item 5: 0.30

**Total:** 1.41
**Comentarios:** El código cumple correctamente con casi todos los requerimientos: θ se genera con linspace (aunque incluye el extremo derecho), se calcula r de forma vectorizada, se obtienen x e y adecuadamente y se calculan los promedios. La gráfica usa axis('equal'), pero falta llamar a plt.show(), por lo que se descuenta ligeramente en el ítem 4.
----
## Detalle P2
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("stars_brightness.csv")
print(df)
plt.scatter
```
- item 1: 0.30
- item 2: 0.03
- item 3: 0.03
- item 4: 0.06
- item 5: 0.03

**Total:** 0.45
**Comentarios:** El código sólo carga el archivo en un DataFrame (bien). No calcula estadísticas por clase, no ordena los resultados y no ofrece interpretación. El intento de gráfico se limita a escribir plt.scatter sin argumentos. Puntajes mínimos otorgados por intento/entrega.
----
## Detalle P3
```python
import numpy as np
import matplotlib.pyplot as plt 
x=np.array([0.39,0.72,1.00,1.52])
y=np.array([0.24,0.61,1.00,1.88])
r=y/(x**(3/2))
print("El coeficionete para cada planeta es:", r.round(3))
plt.scatter(x,y)
plt.title("verificacion de la ley de kepler")
plt.xlabel("semi eje mayor en UA(unidades )")
plt.ylabel("periodo orbital T(años)")
plt.show
promedio=np.mean(r)
desviacion_estandar=np.std(r)
print("el promedio es:" ,promedio)
print("la desviacion_estandar:", desviacion_estandar)
```
- item 1: 0.24
- item 2: 0.30
- item 3: 0.30
- item 4: 0.00
- item 5: 0.00

**Total:** 0.84
**Comentarios:** Se genera correctamente el scatter, pero falta llamar a plt.show() (por eso se descuenta ligeramente). Los cocientes R_i se calculan y muestran con tres decimales, y se obtiene el promedio y la desviación estándar, todo correcto. Los ítems 4 y 5 no aparecen en la rúbrica provista, por lo que se califican con 0.
----