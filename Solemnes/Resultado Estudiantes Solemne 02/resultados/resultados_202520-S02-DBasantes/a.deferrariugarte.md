# Evaluación de a.deferrariugarte@uandresbello.edu

## Cálculo de la nota final

| Problema | Puntaje obtenido |
| -------- | ---------------: |
| P1       |             0.96 |
| P2       |             1.38 |
| P3       |             0.90 |

- Problemas considerados: **3** (P1, P2, P3).
- Puntaje total obtenido: **3.24** puntos.
- Puntaje máximo posible: **4.50** puntos.
- Resultado de la fórmula: **5.32** → registrado como **5.3** en escala 1.0–7.0.

Fórmula aplicada: `1.0 + 6.0*(puntos)/(max_points)`

```python
scores = {'p1': 0.9600, 'p2': 1.3800, 'p3': 0.9000}
puntos = 3.2400
max_points = 4.5000
max = 4.5000
nota = 1.0 + 6.0*(puntos)/(max_points)
```

## Resumen

- Valor por item: 0.3
- Total ítems: 5
- **P1**: 0.96 ptos
- **P2**: 1.38 ptos
- **P3**: 1.5 ptos

**Nota final:** 5.3

## Detalle P1

```python
e = 0.40 #excentricidad
theta = np.linspace(0, 2*np.pi, 720)
r = a*(1-e**2)/(1 + e*np.cos(theta))
x = r * np.cos(theta)
y = r * np.sin(theta)
plt.figure(figsize=(8,6))
plt.plot(x, y, 'r-', linewidth  =2 )
plt.title('orbita eliptica parametrizada')
plt.xlabel('funcion coseno x r')
plt.ylabel('funcion seno x r')
plt.axis("equal")
plt.grid(True)
plt.show()
valor_media_x = np.mean(x)
valor_media_y = np.mean(y)
print('el valor de la media de x e y es:')
print(f'{valor_media_x},{valor_media_y}')
```

- item 1: 0.24
- item 2: 0.12
- item 3: 0.12
- item 4: 0.24
- item 5: 0.24

**Total:** 0.96
**Comentarios:** La idea general está bien, pero hay omisiones que impedirían ejecutar el código tal cual. Falta definir la constante a (provoca error en r, x, y y gráficas). En linspace no se excluye 2π (endpoint=False). Aun así, la mayoría de los pasos están planteados correctamente y de forma vectorizada.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Detalle P2

```python
import numpy as np 
import pandas as pd 
df = pd.read_csv("stars_brightness.csv")
resultado = df.groupby('spectral_class').agg({'temperature_K':['mean','std', 'min']})
print('para cada clase espectral, la temperatura, la desviacion estandar y la magnitud minima son:')
print(resultado)
print('---------------------------------------------------------------------')
resultado_ordenado = resultado.sort_values(('temperature_K','mean'), ascending=False)
print('tabla ordenada por temperatura promedio es:')
print(resultado_ordenado)
plt.figure(figsize= (8,6))
plt.scatter(df['temperature_K'], df['magnitude_app'])
plt.grid(True)
plt.xlabel('temperature K')
plt.ylabel('magnitude app')
plt.title('grafico de dispersion')
print('respondiendo a las preguntas de desarrollo, las estrellas mas calientes no necesariamente tienden a ser las mas brillantes y se puede ver como tendencia que encontramos la mayor cantidad de estrellas bajo los 10.000 K')
```

- item 1: 0.30
- item 2: 0.24
- item 3: 0.30
- item 4: 0.24
- item 5: 0.30

**Total:** 1.38
**Comentarios:** Lee correctamente el CSV (item1). Agrega media y desviación de temperatura, pero calcula el mínimo de temperature_K en vez de magnitude_app (item2 parcialmente). Ordena bien por temperatura promedio (item3). El scatter está bien planteado aunque falta importar matplotlib.pyplot, por lo que es parcialmente correcto (item4). Incluye una breve interpretación respondiendo ambas preguntas (item5).
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Detalle P3

```python
import matplotlib.pyplot as plt 
import numpy as np 
a = np.array([0.39,0.72,1.00,1.52])
T = np.array([0.24,0.61,1.00,1.88])
R = T/(a**(3/2))
print('4 valores de R igual a=')
print(R.round(3))
R_promedio = np.mean(R)
R_std = np.std(R)
print('el promedio y la desviacion estandar de los valores de R es:')
print(R_promedio.round(3),R_std.round(3))
plt.figure(figsize=(8,6))
plt.scatter(a,T)
plt.xlabel('semieje mayor')
plt.ylabel('periodo orbital')
plt.title('grafica de dispersion')
plt.grid(True)
plt.show()
```

- item 1: 0.30
- item 2: 0.30
- item 3: 0.30
- item 4: 0.00
- item 5: 0.00

**Total:** 0.90
**Comentarios:** El código cumple correctamente con los tres ítems solicitados: genera el scatter a-T, calcula y muestra los cuatro valores de R con tres decimales, y obtiene promedio y desviación estándar. No hay implementación para otros ítems, por lo que se asigna 0 en los restantes.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
