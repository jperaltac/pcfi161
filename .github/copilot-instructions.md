# 📋 **FORMATO LATEX PARA EJERCICIOS DE CLASE**

## 🎯 **ESTRUCTURA GENERAL DE EJERCICIOS**

### **1. Frame de Ejercicio (Enunciado)**

```latex
% ------------------------------------------------------------------------
% Slide X: Ejercicio N - Título Descriptivo
% ------------------------------------------------------------------------
\begin{frame}{Ejercicio N: \hfill \textcolor{red}{$\clubsuit$} \\ Título del Ejercicio}
  \begin{block}{Enunciado}
    \begin{itemize}
      \item Instrucción específica 1.
      \item Instrucción específica 2 con fórmula: \(F = ma\).
      \item Instrucción específica 3 con unidades.
    \end{itemize}
  \end{block}
  
  \textbf{Conceptos:} Breve explicación conceptual relevante.
  \\
  \textbf{Física relevante:} Aplicación en el contexto físico.
\end{frame}
```

### **2. Frame de Solución**

```latex
% ------------------------------------------------------------------------
% Slide Y: Ejemplo de Solución (Título del Ejercicio)
% ------------------------------------------------------------------------
\begin{frame}[fragile]{Solución N de Referencia: \hfill \textcolor{green}{$\checkmark$} \\ Título del Ejercicio}
\begin{minted}{python}
# Comentario explicativo
variable = float(input("Mensaje descriptivo con unidades: "))

# Cálculos con comentarios
resultado = formula_aplicada

# Salida formateada
print(f"Resultado: {resultado} unidades")
\end{minted}
\textbf{Discusión:} Punto de reflexión o consideración especial.
\end{frame}
```

## 🎨 **ELEMENTOS DE FORMATO**

### **Colores y Símbolos:**

- **Ejercicios**: `\textcolor{red}{$\clubsuit$}` (rojo con símbolo de trébol)
- **Soluciones**: `\textcolor{green}{$\checkmark$}` (verde con check)
- **Actividades Extra**: `\textcolor{blue}{$\clubsuit$}` (azul con trébol)

### **Bloques Especiales:**

- **Enunciado**: `\begin{block}{Enunciado}...\end{block}`
- **Alertas**: `\begin{alertblock}{Título}...\end{alertblock}`
- **Información**: Texto directo sin bloque especial

## 📝 **CONVENCIONES DE NUMERACIÓN**

### **Ejercicios Principales:**

```latex
Ejercicio 1: Área y Perímetro de un Rectángulo
Ejercicio 2: Calculadora de Masa y Peso  
Ejercicio 3: Suma de Dos Variables
Ejercicio 4: Promedio de Tres Notas
Ejercicio 5: Conversión de Temperatura
```

### **Soluciones Correspondientes:**

```latex
Solución 1 de Referencia: Área y Perímetro de un Rectángulo
Solución 2 de Referencia: Calculadora de Masa y Peso
Solución 3 de Referencia: Suma de Dos Variables
Solución 4 de Referencia: Promedio de Tres Notas
Solución 5 de Referencia: Conversión de Temperatura
```

## 💻 **FORMATO DE CÓDIGO PYTHON**

### **Configuración de Minted:**

```latex
\begin{minted}{python}
# Código aquí
\end{minted}
```

### **Estilo de Código Recomendado:**

```python
# 1. Entrada de datos con mensajes descriptivos
variable = float(input("Descripción con unidades: "))

# 2. Constantes bien documentadas  
g_tierra = 9.81  # m/s²

# 3. Cálculos con nombres descriptivos
resultado = formula * variable

# 4. Salida con f-strings y unidades
print(f"Resultado: {resultado} unidades")
```

## 🔧 **ELEMENTOS ADICIONALES**

### **Actividades Extra:**

```latex
\begin{frame}{Actividad Extra N: \hfill \textcolor{blue}{$\clubsuit$} \\ Título}
  Descripción del objetivo de la actividad.
  \begin{block}{Enunciado}
    \begin{itemize}
      \item Instrucciones específicas.
    \end{itemize}
  \end{block}
  \textbf{Objetivo:} Meta pedagógica específica.
\end{frame}
```

### **Comentarios de Slides:**

```latex
% ------------------------------------------------------------------------
% Slide N: Descripción Clara del Contenido
% ------------------------------------------------------------------------
```

## ⚡ **TIPS PARA APLICAR A CLASES SIGUIENTES**

### **1. Mantener Consistencia:**

- Siempre usar la misma numeración correlativa
- Colores consistentes para cada tipo de contenido
- Formato uniforme en comentarios de slides

### **2. Contenido Educativo:**

- Incluir conceptos físicos relevantes
- Agregar discusiones o reflexiones
- Mencionar casos especiales (ej: división por cero)

### **3. Código Python:**

- Comentarios explicativos en español
- Variables con nombres descriptivos
- Incluir unidades en input y output
- Usar f-strings para salidas formateadas

### **4. Estructura Progresiva:**

- Ejercicios de menor a mayor complejidad
- Soluciones inmediatamente después o en sección separada
- Actividades extra para reforzamiento

### **Errores tipicos que cometes:**
- Creas los textos en la parte de arriba del codigo y no donde corresponde siempre debajo de \begin{document}
- Al terminar de escribir los frames usas ">" en vez de usar "}" 
