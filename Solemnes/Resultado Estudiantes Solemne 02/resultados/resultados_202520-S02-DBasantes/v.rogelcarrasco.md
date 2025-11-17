# Evaluación de v.rogelcarrasco@uandresbello.edu
## Cálculo de la nota final

| Problema | Puntaje obtenido |
|---|---:|
| P1 | 1.26 |
| P2 | 1.32 |
| P3 | 0.60 |

- Problemas considerados: **3** (P1, P2, P3).
- Puntaje total obtenido: **3.18** puntos.
- Puntaje máximo posible: **4.50** puntos.
- Resultado de la fórmula: **5.24** → registrado como **5.2** en escala 1.0–7.0.

Fórmula aplicada: `1.0 + 6.0*(puntos)/(max_points)`

```python
scores = {'p1': 1.2600, 'p2': 1.3200, 'p3': 0.6000}
puntos = 3.1800
max_points = 4.5000
max = 4.5000
nota = 1.0 + 6.0*(puntos)/(max_points)
```

## Resumen
- Valor por item: 0.3
- Total ítems: 5
- **P1**: 1.26 ptos
- **P2**: 1.32 ptos
- **P3**: 0.60 ptos

**Nota final:** 5.2

## Detalle P1
```python
a = 1.0
e = 0.40
theta = np.linspace(0, 2*np.pi, 720)
#colocamos nuestra función principal y calculamos los 720 valores
r = a*(1-e**2)/(1 + e*np.cos(theta))
#obtenemos nuestras coordenadas cartesianas
x = r * np.cos(theta)
y = r * np.sin(theta)
print(x), print(y)
print('-'*60)
#graficamos los puntos
plt.plot(x,y, color = 'r')
plt.xlabel("eje x")
plt.ylabel("eje y")
plt.title("Visualización de la órbita elíptica")
plt.grid(True)
plt.show()
#finalmente calculamos los valores medios y luego verificamos que sean cercanos a cercanos
prom_x = np.mean(x)
prom_y = np.mean(y)
print(f'el valor medio de x es {prom_x}')
print(f'el valor medio de y es {prom_y}')
print("los valores de ambos son cercanos a cero")
```
- item 1: 0.24
- item 2: 0.30
- item 3: 0.30
- item 4: 0.18
- item 5: 0.24

**Total:** 1.26
**Comentarios:** Se utiliza linspace con 720 puntos y operaciones vectorizadas; se calculan x e y correctamente y se grafica, pero falta plt.axis('equal') y linspace incluye 2π. La comprobación de medias solo se imprime, sin verificación formal.
----
## Detalle P2
```python
print(tem)
#ordenamos de menor a mayor la tabla que nos quedó
mayor_a_menor = tem.sort_values(('temperature_K', 'mean'), ascending = False)
print("\n mayor_a_menor:")
print(mayor_a_menor)
#creamos nuestro scatter
x = df["temperature_K"]
y = df['magnitude_app']
plt.figure(figsize=(20,8)) #le damos un tamaño a nuestra tabla
plt.scatter(x,y, color = 'black')
plt.title("Temperatura en kelvin vs. Magnitud Aparente")
plt.xlabel("temperatura")
plt.ylabel("magnitud")
plt.grid(True) #grilla para el gráfico
plt.show()
#aquí respondo las preguntas planteadas en la guía
print("pregunta 1")
print("No, de hecho es todo lo contrario, como se puede ver en el gráfico, las estrellas más calientes suelen ser las menos brillantes.")
print("pregunta 2")
print("Al analizar este gráfico, se puede ver que hay un número muy elevado de estrellas que su temperatura es menor de los 10000K")
print("Además, mientras más calientes se ponen las estrellas, hay menos de ellas.")
```
- item 1: 0.18
- item 2: 0.24
- item 3: 0.30
- item 4: 0.30
- item 5: 0.30

**Total:** 1.32
**Comentarios:** Se aprecian variables df y tem, lo que sugiere que el archivo fue leído previamente, pero el código mostrado no incluye explícitamente la instrucción de lectura, por lo que se otorga un puntaje medio-bajo. El agrupamiento parece calcular al menos la media (temperature_K) y probablemente la desviación estándar; no se visualiza la magnitud mínima, por eso no llega al máximo. El ordenamiento y el scatter están correctamente implementados. Las respuestas interpretativas existen y son coherentes aunque breves.
----
## Detalle P3
```python
#el semieje mayor es nuestro eje X
x = np.array([0.39, 0.72, 1.00, 1.52])
#el período orbital es nuestro eje Y
y = np.array([0.24, 0.61, 1.00, 1.88])
#creamos el gráfico
plt.scatter(x,y)
plt.title("Semieje Mayor vs. Período Orbital")
plt.xlabel("s.m (a) en UA") #semieje mayor (a) en unidades astronomicas
plt.ylabel("p.o (T) en años") #período orbital (T) en años
plt.grid(True) #grilla para nuestro gráfico
plt.show()
#calculamos el cociente
R = y / (x)**3/2
print("el cociente es:", R.round(2)) #round 2 para redondear los decimales a 2
#calculamos el promedio y la desviación estándar de R
prom_R = np.mean(R)
desv_R = np.std(R)
print(f'el promedio de los datos es de {prom_R}')
print(f'la desviación estandar de los datos es de {desv_R}')
```
- item 1: 0.30
- item 2: 0.12
- item 3: 0.18
- item 4: 0.00
- item 5: 0.00

**Total:** 0.60
**Comentarios:** El gráfico scatter está correctamente construido (item 1). Para el cociente R se intenta la operación pero se usa la expresión y/(x)**3/2, que corresponde a y/(x^3)/2 y no a y/(x^(3/2)); además se redondea a 2 y no a 3 decimales, por lo que el resultado es incorrecto pero muestra intención (item 2). El promedio y la desviación estándar se calculan y muestran adecuadamente, aunque basados en valores de R erróneos; se otorga crédito parcial (item 3). Los ítems 4 y 5 no están presentes en el código.
----