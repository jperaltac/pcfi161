# Evaluación de e.sezsez@uandresbello.edu
## Cálculo de la nota final

| Problema | Puntaje obtenido |
|---|---:|
| P1 | 0.60 |
| P2 | 1.26 |
| P3 | 0.60 |

- Problemas considerados: **3** (P1, P2, P3).
- Puntaje total obtenido: **2.46** puntos.
- Puntaje máximo posible: **4.50** puntos.
- Resultado de la fórmula: **4.28** → registrado como **4.3** en escala 1.0–7.0.

Fórmula aplicada: `1.0 + 6.0*(puntos)/(max_points)`

```python
scores = {'p1': 0.6000, 'p2': 1.2600, 'p3': 0.6000}
puntos = 2.4600
max_points = 4.5000
max = 4.5000
nota = 1.0 + 6.0*(puntos)/(max_points)
```

## Resumen
- Valor por item: 0.3
- Total ítems: 5
- **P1**: 0.60 ptos
- **P2**: 1.26 ptos
- **P3**: 0.60 ptos

**Nota final:** 4.3

## Detalle P1
```python
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
a = 1             
e = 0.40
#a).
theta = np.linspace(0, 2*np.pi, 720)  #creamos un arrego theta con 720 valores 
#b). calcular r
r = a * (1 - e**2) / [1 + e *np.cos(theta)]   # calculamos r 
#c). coordenadas cartesianas 
x = r * np.cos(theta)             
y = r * np.sin(theta)   
#d). graficar todos los puntos (x, y) 
plt.axis("equal") 
plt.xlabel("X")
plt.ylabel("Y")
plt.title("orbita eliptica")
plt.grid(True)
plt.show()
```
- item 1: 0.24
- item 2: 0.12
- item 3: 0.18
- item 4: 0.06
- item 5: 0.00

**Total:** 0.60
**Comentarios:** 1) Usa np.linspace con 720 puntos, pero incluye el extremo 2π, por lo que el intervalo es [0,2π] y no [0,2π). 2) Intenta vectorizar la fórmula de r, pero el uso de corchetes crea una lista y provoca un error de tipo. 3) La conversión a coordenadas cartesianas está escrita correctamente, aunque depende de r (que falla). 4) Se ajusta la relación de aspecto, pero falta la llamada a plt.plot o similar para dibujar los puntos. 5) No calcula los valores medios <x> y <y>.
----
## Detalle P2
```python
})
print(xe)
 
#c). ordenar tabla de mayor a menor
xe_ordenado = xe.sort_values(('temperature_K', 'mean'), ascending = False)
print("\nxe_ordenado:")
print(xe_ordenado)
#d). grafico
plt.figure(figsize = (10, 6))
plt.scatter(df['temperature_K'], df['magnitude_app'], alpha= 0.6, edgecolors= 'red')
plt.xlabel("temperature_k")
plt.ylabel("magnitude_app")
plt.title("stars brightness")
plt.grid(True)
plt.show()
#E). 1 ¿las extrellas más calientes tienden a se mas brillates?
#    r. A interpretación del grafico a mayor temperatura menos brillantes son las extrellas.
# 
#    2 ¿hay alguna tendencia según la clase espectral?
#    r. según la clase espectral a menor temperatura más brillantes son las extrellas.
```
- item 1: 0.18
- item 2: 0.24
- item 3: 0.30
- item 4: 0.30
- item 5: 0.24

**Total:** 1.26
**Comentarios:** Se aprecia el uso de pandas (df, xe) pero no se muestra la carga explícita del archivo, por lo que se otorga un puntaje parcial. El agrupamiento parece calcular media y se infiere std/min aunque no se ve completo; buena intención, leve descuento. El ordenamiento y el scatter están implementados correctamente. La interpretación existe pero es muy breve y algo confusa, se le reconoce esfuerzo moderado.
----
## Detalle P3
```python
import numpy as np 
import matplotlib.pyplot as plt 
x = np.array([0.39, 0.72, 1.00, 1.52])     #semieje mayor
y = np.array([0.24, 0.61, 1.00, 1.88])     #periodo orbital
k = 1                         # como el periodo orbital se mide en (UA) y el periodo en años entonces k =1
 
y = k * x**(3/2)              # y = T, y = periodo orbital
                              # x = a , x = semieje mayor 
# a). crear un grafico de dispersión 
plt.scatter(x,y)
plt.title("Datos de los planetas interiores del sistema solar")
plt.xlabel("semieje mayor")
plt.ylabel("periodo orbital")
plt.grid(True)
plt.show()
#b). calcular para cada planeta el cociente
ri = y/(x)**(3/2)
print(ri.round(3))             # 3 decimales 
#ri = np.mean(ri)                 #calcular el promedio
#ri = np.std(ri)                  #calcular la deviacion estandar
```
- item 1: 0.24
- item 2: 0.24
- item 3: 0.12
- item 4: 0.00
- item 5: 0.00

**Total:** 0.60
**Comentarios:** Se genera un gráfico scatter, pero usa valores calculados en vez de los datos originales; el cociente R_i se calcula y se muestra con 3 decimales, aunque todos resultan 1.00. El promedio y la desviación estándar se dejan comentados, por lo que no se obtienen. No hay evidencias para los ítems 4 y 5.
----