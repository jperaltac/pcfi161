# Evaluación de g.lpezastorga@uandresbello.edu
## Cálculo de la nota final

| Problema | Puntaje obtenido |
|---|---:|
| P1 | 0.93 |
| P2 | 0.54 |
| P3 | 0.30 |

- Problemas considerados: **3** (P1, P2, P3).
- Puntaje total obtenido: **1.77** puntos.
- Puntaje máximo posible: **4.50** puntos.
- Resultado de la fórmula: **3.36** → registrado como **3.4** en escala 1.0–7.0.

Fórmula aplicada: `1.0 + 6.0*(puntos)/(max_points)`

```python
scores = {'p1': 0.9300, 'p2': 0.5400, 'p3': 0.3000}
puntos = 1.7700
max_points = 4.5000
max = 4.5000
nota = 1.0 + 6.0*(puntos)/(max_points)
```

## Resumen
- Valor por item: 0.3
- Total ítems: 5
- **P1**: 0.93 ptos
- **P2**: 0.54 ptos
- **P3**: 0.30 ptos

**Nota final:** 3.4

## Detalle P1
```python
r = (a * 1 - (e ** 2)) / 1 + e * np.cos(theta)
x = r * np.cos(theta)
y = r * np.sin(theta)
plt.title('Órbita elíptica parametrizada')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.plot(x, y)
plt.axis('equal')
plt.grid()
plt.show()
valores_medios_x = np.meand(x)
valores_medios_y = np.meand(y)
print(f'valores medios de x = {valores_medios_x}')
print(f'valores medios de y = {valores_medios_y}')
```
- item 1: 0.03
- item 2: 0.18
- item 3: 0.30
- item 4: 0.30
- item 5: 0.12

**Total:** 0.93
**Comentarios:** Falta crear el arreglo theta; el cálculo de r es vectorizado pero la fórmula y variables son incorrectas. Las coordenadas x,y y la gráfica están bien implementadas con axis equal. El intento de medias usa np.meand, por lo que falla aunque la idea es correcta.
----
## Detalle P2
```python
print("La desviación estandar de temperature_K es:")
print(np.std(df.temperature_K))
print('=' * 60)
print("Tabla general de datos:")
print()
print(df.describe())
print()
tabla_ordenada = df.temperature_K.sort_values(('temperature_K'), ascending = False)
print(tabla_ordenada)
x = df.temperature_K
y = df.magnitude_app
plt.figure(figsize = ( 6, 8))
plt.scatter(x, y)
plt.xlabel('temperature_K')
plt.ylabel('magnitude_app')
plt.grid()
plt.show()
```
- item 1: 0.06
- item 2: 0.06
- item 3: 0.12
- item 4: 0.30
- item 5: 0.00

**Total:** 0.54
**Comentarios:** Se observa un DataFrame ya existente, pero no se muestra la lectura del archivo. Sólo se calcula la desviación estándar global y se ordena una serie, sin agrupar por clase espectral ni obtener el mínimo de magnitud. El ordenamiento muestra intención, aunque es parcial. El scatter está correctamente implementado. Falta por completo la interpretación de resultados.
----
## Detalle P3
```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
a = np.array([0.39, 0.72, 1.00, 1.52])
T = np.array([0.24, 0.61, 1.00, 1.88])
k = 1
print(f'El semieje mayor "a" medido en [UA] es:')
print(a)
print()
print(f'El periodo orbital "T" medido en Años es:')
print(T)
print("=" * 41)
x = a
y = T
plt.title("Grafico de Dispersión Scatter")
plt.xlabel("Semieje mayor")
plt.ylabel("Periodo Orbital")
```
- item 1: 0.24
- item 2: 0.03
- item 3: 0.03
- item 4: 0.00
- item 5: 0.00

**Total:** 0.30
**Comentarios:** Se carga la información y se preparan etiquetas para un scatter, pero no se llama plt.scatter() ni se muestra la figura, por lo que el gráfico queda incompleto. No se calcula ni se imprime el cociente R_i, ni su promedio ni su desviación estándar. El código solo refleja un intento parcial del ítem 1; los demás ítems no se abordan.
----