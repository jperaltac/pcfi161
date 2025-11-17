# Evaluación de d.muozastete@uandresbello.edu
## Cálculo de la nota final

| Problema | Puntaje obtenido |
|---|---:|
| P1 | 1.05 |
| P2 | 1.26 |
| P3 | 0.90 |

- Problemas considerados: **3** (P1, P2, P3).
- Puntaje total obtenido: **3.21** puntos.
- Puntaje máximo posible: **4.50** puntos.
- Resultado de la fórmula: **5.28** → registrado como **5.3** en escala 1.0–7.0.

Fórmula aplicada: `1.0 + 6.0*(puntos)/(max_points)`

```python
scores = {'p1': 1.0500, 'p2': 1.2600, 'p3': 0.9000}
puntos = 3.2100
max_points = 4.5000
max = 4.5000
nota = 1.0 + 6.0*(puntos)/(max_points)
```

## Resumen
- Valor por item: 0.3
- Total ítems: 5
- **P1**: 1.05 ptos
- **P2**: 1.26 ptos
- **P3**: 0.90 ptos

**Nota final:** 5.3

## Detalle P1
```python
cos=np.cos(theta)
sen=np.sin(theta)
r=a*(1-e**2)/(1+e+cos)
x=r*cos
y=r*sen
plt.plot(x,y)
plt.axis("equal")
plt.title('Órbita Elíptica')
plt.legend('descripción orbital')
plt.xlabel('eje x')
plt.ylabel('eye y')
plt.grid(True, alpha=0.2)
plt.show()
xmed=np.mean(x)
ymed=np.mean(y)
print(xmed)
print(ymed)
```
- item 1: 0.06
- item 2: 0.18
- item 3: 0.27
- item 4: 0.30
- item 5: 0.24

**Total:** 1.05
**Comentarios:** Se omite la creación de theta (solo se usa), la expresión de r es vectorizada pero con la fórmula incorrecta (e*cos debería multiplicar), x e y se calculan bien sin bucles, la gráfica incluye plt.axis('equal'), y se promedian x e y aunque no se verifica explícitamente su cercanía a 0.
----
## Detalle P2
```python
import numpy as np
import pandas as pd
df=pd.read_csv("stars_brightness.csv")
x=df.groupby('spectral_class').agg({'temperature_K':['mean', 'std'],'magnitude_app':'min'})
y=x.sort_values(('temperature_K','mean'), ascending=False)
print(x)
plt.scatter(x,y,alpha=0.5)
plt.title('Mini catalogo')
plt.legend('spectral class')
plt.xlabel('temperature_K')
plt.ylabel('magnitude_app')
plt.grid(True, alpha=0.4)
plt.show()
#respuestas de punto e)
#el grafico tiene tendencia lineal, por lo que a mayor temperatura, mayor luminosidad
#si se ordenan de forma expectral  como la clase como la mayor y la clase o como la menor, seobserva un desenso de temperatura a medidad que se avanza de clase,
#a exepcion de la clase B y la clase O que se escapan de la tendencia segun la tabla de datos tanto en luminosidad como en temperatura
```
- item 1: 0.30
- item 2: 0.30
- item 3: 0.30
- item 4: 0.12
- item 5: 0.24

**Total:** 1.26
**Comentarios:** Lee correctamente el CSV a un DataFrame y calcula las métricas solicitadas por clase espectral, además de ordenarlas bien. El scatter presenta varios problemas (no importa matplotlib, usa variables incorrectas para los ejes), por lo que solo se otorga puntaje parcial. Incluye una breve interpretación, aunque algo superficial; se valora el esfuerzo.
----
## Detalle P3
```python
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
a=np.array([0.39,0.72,1.00,1.52])
T=np.array([0.24,0.64,1.00,1.88])
plt.plot(a,T)
plt.scatter(a,T)
plt.title('Ley de Kepler')
plt.legend('constante de Kepler?')
plt.xlabel('semieje Mayor')
plt.ylabel('periodo robital')
plt.show()
Ri=T/(a**(3/2))
print(Ri.round(3),'promedio = ', np.mean(Ri).round(3),'desviacion estandar = ', np.std(Ri).round(3))
```
- item 1: 0.30
- item 2: 0.30
- item 3: 0.30
- item 4: 0.00
- item 5: 0.00

**Total:** 0.90
**Comentarios:** El código cumple correctamente los 3 requisitos especificados (gráfico scatter, cálculo y muestra del cociente R_i con 3 decimales, y cálculo de promedio y desviación estándar). No hay criterios definidos para los ítems 4 y 5, por lo que se asignan 0.
----