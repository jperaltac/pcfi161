# Documento de Instrucciones LaTeX para Curso de Python

Basado en el análisis de las presentaciones existentes, aquí presento un documento detallado de instrucciones para crear clases semanales de Python siguiendo el formato establecido.

## 📋 **ESTRUCTURA GENERAL DEL CURSO**

### **Progresión Temática Semanal**
```
Semana 01: Introducción a Python y sintaxis básica
Semana 02: Estructuras de control (if, elif, else, for, while)
Semana 03: Funciones (def) y módulos (import)
```

### **Estructura de Archivos**
```
lectures/
├── Semana01/
│   ├── Semana01-P1.tex (Clase teórica)
│   └── Semana01-P2.tex (Clase práctica)
├── Semana02/
│   ├── Semana02-P1.tex
│   └── Semana02-P2.tex
└── Semana03/
    ├── Semana03-P1.tex
    └── Semana03-P2.tex
```

### **Estructura Base para Cada Archivo .tex**

```latex
\documentclass[10pt]{beamer}
\usepackage{xcolor}

% Carga del preámbulo personalizado
\input{../preamble.tex}

\begin{document}

% Portada personalizada
\myfront{}

% Título de la sesión
\begin{frame}
  \titlepage
\end{frame}

% Índice
\begin{frame}
  \frametitle{Resumen - Semana X, Sesión Y}
  \tableofcontents
\end{frame}

% Configuración de bloques
\metroset{block=fill}

% CONTENIDO ESPECÍFICO SEGÚN TIPO P1/P2
% ...

\end{document}
```

## 🎯 **ESTRUCTURA ESPECÍFICA POR TIPO DE CLASE**

### **Clase P1 (Teórica)**

1. **Sección: Introducción de la Sesión**
   ```latex
   \section{Introducción y Repaso}
   
   \begin{frame}{Recapitulación de la Sesión Anterior}
     \begin{itemize}
       \item \textbf{Sesión anterior} se centró en:
         \begin{itemize}
           \item Punto clave 1
           \item Punto clave 2
         \end{itemize}
       \item \textbf{Conexión} con la sesión actual...
     \end{itemize}
   \end{frame}

   \begin{frame}{Objetivos de la Sesión X}
     \begin{itemize}
       \item \textbf{Comprender} [concepto principal 1]
       \item \textbf{Explorar} [concepto principal 2]
       \item \textbf{Aplicar} estos conceptos en ejercicios prácticos
       \item \textbf{Desarrollar} [habilidad específica]
     \end{itemize}
   \end{frame}
   ```

2. **Sección: Nuevos Conceptos**
   ```latex
   \section{Concepto Principal}

   \begin{frame}{Definición y Motivación}
     \begin{itemize}
       \item \textbf{Definición:} explicación clara del concepto
       \item \textbf{Motivación:} por qué es importante
       \item \textbf{Aplicaciones:} casos de uso relevantes
     \end{itemize}
   \end{frame}

   \begin{frame}[fragile]{Sintaxis y Ejemplos}
   \begin{minted}{python}
   # Ejemplo de código que ilustra el concepto
   resultado = operación_con_concepto()
   print(f"Resultado: {resultado}")
   \end{minted}
   
   \begin{itemize}
     \item \textbf{Punto clave 1} sobre la sintaxis
     \item \textbf{Punto clave 2} sobre buenas prácticas
   \end{itemize}
   \end{frame}
   ```

3. **Sección: Ejercicios Guiados**
   ```latex
   \section{Ejercicios Guiados}
   
   % Formato de ejercicio según las instrucciones
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
   
   % Formato de solución según las instrucciones
   % ------------------------------------------------------------------------
   % Slide Y: Solución N de Referencia - Título
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

4. **Sección: Actividad Práctica**
   ```latex
   \section{Actividad Práctica}
   
   \begin{frame}{Organización para Actividad Práctica}
     \begin{itemize}
       \item Formar \textbf{equipos} de 2-3 estudiantes
       \item Cada estudiante crea su propio notebook
       \item Tiempo asignado: XX minutos
       \item \textbf{Objetivo:} [descripción del objetivo pedagógico]
     \end{itemize}
   \end{frame}
   
   % Formato para actividades extra
   % ------------------------------------------------------------------------
   % Slide Z: Actividad Extra N
   % ------------------------------------------------------------------------
   \begin{frame}{Actividad Extra N: \hfill \textcolor{blue}{$\clubsuit$} \\ Título}
     Descripción breve del objetivo.
     \begin{block}{Enunciado}
       \begin{itemize}
         \item Instrucción específica 1.
         \item Instrucción específica 2.
       \end{itemize}
     \end{block}
     \textbf{Objetivo:} Meta pedagógica específica.
   \end{frame}
   ```

5. **Sección: Consolidación y Retroalimentación**
   ```latex
   \section{Consolidación y Retroalimentación}
   
   \begin{frame}{Puesta en Común - ¿Cómo les fue?}
     \begin{itemize}
       \item ¿Qué concepto resultó más difícil de entender?
       \item ¿Encontraron errores comunes? ¿Cómo los solucionaron?
       \item ¿Descubrieron algún truco o patrón interesante?
     \end{itemize}
     
     \begin{alertblock}{Objetivo}
       Aprender de las experiencias colectivas y normalizar los errores como parte del aprendizaje.
     \end{alertblock}
   \end{frame}
   
   \begin{frame}{Errores Comunes con [Concepto del Día]}
     \begin{block}{Errores frecuentes}
       \begin{itemize}
         \item Error específico 1: explicación y solución
         \item Error específico 2: explicación y solución
       \end{itemize}
     \end{block}
     
     \begin{alertblock}{Consejo}
       Técnica específica para depuración o comprensión del concepto.
     \end{alertblock}
   \end{frame}
   ```

6. **Sección: Conclusiones**
   ```latex
   \section{Conclusiones}
   
   \begin{frame}{Resumen de la Sesión}
     \begin{itemize}
       \item \textbf{Aprendimos} [concepto principal 1]
       \item \textbf{Practicamos} [concepto principal 2]
       \item \textbf{Exploramos} aplicaciones en problemas físicos
       \item \textbf{Desarrollamos} habilidades de [tipo específico]
     \end{itemize}
     
     \begin{block}{Habilidad adquirida}
       Descripción concreta de la competencia desarrollada hoy.
     \end{block}
   \end{frame}
   
   \begin{frame}{Próximos Pasos}
     \begin{itemize}
       \item \textbf{Sesión siguiente:} Introducción a [próximo tema]
       \item \textbf{Recomendación de estudio:} recursos específicos
       \item \textbf{Práctica sugerida:} ejercicios complementarios
     \end{itemize}
   \end{frame}
   ```

### **Clase P2 (Práctica)**

1. **Sección: Introducción de la Sesión**
   ```latex
   \section{Introducción y Conexión}
   
   \begin{frame}{Repaso de la Sesión Previa}
     \begin{itemize}
       \item \textbf{Sesión anterior (P1)} dominamos:
         \begin{itemize}
           \item [Concepto clave 1] y su sintaxis
           \item [Concepto clave 2] y su aplicación
         \end{itemize}
       \item \textbf{Objetivo de hoy:} Aplicar y consolidar estos conceptos en problemas más elaborados y colaborativos.
     \end{itemize}
   \end{frame}
   
   \begin{frame}{Objetivos de la Sesión P2}
     \begin{itemize}
       \item \textbf{Consolidar} el uso de [conceptos clave]
       \item \textbf{Aplicar} en problemas físicos y matemáticos complejos
       \item \textbf{Desarrollar} habilidades de resolución colaborativa
       \item \textbf{Integrar} múltiples conceptos en aplicaciones prácticas
     \end{itemize}
   \end{frame}
   ```
2. **Sección: Ejercicios Prácticos Integrados**
   ```latex
   \section{Ejercicios Prácticos Integrados}
   
   \begin{frame}{Enfoque de la Sesión: Aplicación Práctica}
     \begin{itemize}
       \item \textbf{Enfoque 100\% práctico:} Resolver problemas complejos
       \item \textbf{Integración de conceptos:} Combinar múltiples herramientas
       \item \textbf{Aplicación contextualizada:} Física, astronomía, datos reales
     \end{itemize}
     
     \begin{block}{Meta de la Sesión}
       Lograr que cada estudiante se sienta cómodo aplicando [conceptos clave] en problemas reales.
     \end{block}
   \end{frame}
   
   % Ejercicios integrados (3-5 ejercicios)
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

3. **Sección: Soluciones de Referencia**
   ```latex
   \section{Soluciones de Referencia}
   
   % Soluciones correspondientes a los ejercicios
   % ------------------------------------------------------------------------
   % Slide Y: Solución N de Referencia - Título
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
   
   \begin{frame}{Análisis de las Soluciones}
     \begin{itemize}
       \item \textbf{Estructuras y conceptos integrados:}
         \begin{itemize}
           \item [Concepto 1] en Ejercicios X, Y
           \item [Concepto 2] en Ejercicios Z
         \end{itemize}
       \item \textbf{Buenas prácticas observadas:}
         \begin{itemize}
           \item Comentarios explicativos
           \item Nombres descriptivos de variables
           \item Manejo de errores
         \end{itemize}
     \end{itemize}
   \end{frame}
   ```


# Instrucciones para Formato de Código Python en LaTeX/Beamer

## Regla de Formato por Longitud de Código

### **Criterio de División en Columnas**

Cuando el código Python en un frame de LaTeX/Beamer **supere las 24 líneas**, debe aplicarse automáticamente el formato de **dos columnas** para mejorar la legibilidad y el aprovechamiento del espacio en la presentación.

### **Formato para Código ≤ 24 líneas (Columna Única)**

```latex
\begin{frame}[fragile]{Título del Frame: \hfill \textcolor{green}{$\checkmark$} \\ Subtítulo}
\begin{minted}[fontsize=\tiny]{python}
# Código Python aquí
# Máximo 24 líneas
import numpy as np
# ... resto del código
\end{minted}
\textbf{Discusión:} Comentario explicativo del código.
\end{frame}
```

### **Formato para Código > 24 líneas (Dos Columnas)**

```latex
\begin{frame}[fragile]{Título del Frame: \hfill \textcolor{green}{$\checkmark$} \\ Subtítulo}
\begin{columns}
\begin{column}{0.5\textwidth}
\begin{minted}{python}
# Primera parte del código
# Líneas 1-N (aproximadamente la mitad)
import numpy as np
import matplotlib.pyplot as plt

# Generar datos aleatorios normales
np.random.seed(42)
datos = np.random.normal(50, 10, 100)

# Calcular estadísticas
media = np.mean(datos)
mediana = np.median(datos)
std = np.std(datos)

print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desviación estándar: {std:.2f}")
\end{minted}
\end{column}
\begin{column}{0.5\textwidth}
\begin{minted}[firstnumber=16]{python}
# Segunda parte del código
# Líneas N+1 hasta el final
# Crear histograma
plt.figure(figsize=(8, 6))
plt.hist(datos, bins=15, alpha=0.7, 
         color='skyblue', edgecolor='black')
plt.axvline(media, color='red', 
            linestyle='--', linewidth=2, 
            label=f'Media: {media:.1f}')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Distribución de Datos Aleatorios')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
\end{minted}
\end{column}
\end{columns}
\vspace{0.3cm}
\textbf{Discusión:} Comentario explicativo del código.
\end{frame}
```

### **Consideraciones Importantes para la División en Columnas**

1. **Punto de división lógico**: Dividir el código en un punto que tenga sentido semánticamente (después de imports, al cambiar de sección lógica, etc.).

2. **Numeración continua**: Usar `[firstnumber=X]` en la segunda columna donde X es el número de línea donde continúa el código.

3. **Distribución equilibrada**: Intentar que ambas columnas tengan aproximadamente el mismo número de líneas.

4. **Anchura de columnas**: Mantener `0.5\textwidth` para cada columna para aprovechamiento óptimo del espacio.

5. **Espaciado**: Incluir `\vspace{0.3cm}` después del entorno `columns` para separar visualmente del texto de discusión.

### **Casos Especiales**

- **Código muy largo (>40 líneas)**: Considerar dividir en múltiples frames en lugar de forzar en un solo frame.
- **Código con bloques muy específicos**: Priorizar la división lógica sobre la división exacta por número de líneas.
- **Comentarios extensos**: Los comentarios cuentan para el total de líneas, pero se puede ser flexible si mejora la comprensión.

### **Ejemplo de Aplicación Automática**

**Código de 30 líneas** → Automáticamente formato de dos columnas
**Código de 20 líneas** → Formato de columna única
**Código de exactamente 24 líneas** → Formato de columna única (≤ 24)
**Código de 25 líneas** → Formato de dos columnas (> 24)




4. **Sección: Tarea (si corresponde)**
   ```latex
   \section{Tarea N}
   
   % Formato para tareas
   \begin{frame}{Tarea Pregunta N: \hfill \textcolor{blue}{$\bigstar$} \\ Título de la Tarea}
     \begin{block}{Enunciado}
       \begin{itemize}
         \item Definir [función/estructura] que:
           \begin{itemize}
             \item Requisito específico 1
             \item Requisito específico 2
             \item Aplicar [concepto específico]
           \end{itemize}
         \item Ejemplo de uso esperado:
           \begin{itemize}
             \item [Ejemplo concreto]
           \end{itemize}
       \end{itemize}
     \end{block}
     
     \textbf{Entrega:} Formato y fecha de entrega.\\
     \textbf{Relevancia:} Conexión con los conceptos del curso.
   \end{frame}
   ```

5. **Sección: Evaluación y Retroalimentación (si corresponde)**
   ```latex
   \section{Evaluación y Retroalimentación}
   
   \begin{frame}{Tarea Semanal: Entrega en Canvas}
     \begin{block}{Entrega Obligatoria}
       \begin{itemize}
         \item Completar los ejercicios con código funcional
         \item Incluir comentarios explicativos
         \item Documentar dificultades y soluciones
       \end{itemize}
     \end{block}
     
     \begin{block}{Criterios de Evaluación}
       \begin{itemize}
         \item Código funcional (40\%)
         \item Uso correcto de conceptos (30\%)
         \item Comentarios y documentación (20\%)
         \item Creatividad y extensiones (10\%)
       \end{itemize}
     \end{block}
   \end{frame}
   
   \begin{frame}{Retroalimentación Colectiva}
     \begin{itemize}
       \item ¿Dificultades específicas con algún ejercicio?
       \item ¿Estrategias efectivas para manejar errores?
       \item ¿Preparación para los próximos temas?
     \end{itemize}
     
     \begin{alertblock}{Importante}
       La colaboración es clave, pero cada estudiante debe entender completamente su código.
     \end{alertblock}
   \end{frame}
   ```

6. **Sección: Conclusiones**
   ```latex
   \section{Conclusiones}
   
   \begin{frame}{Síntesis de la Sesión}
     \begin{itemize}
       \item \textbf{Consolidamos:} aplicación práctica de [conceptos clave]
         \begin{itemize}
           \item [Detalle específico 1]
           \item [Detalle específico 2]
         \end{itemize}
       \item \textbf{Aplicamos:} programación a problemas físicos reales
       \item \textbf{Desarrollamos:} habilidades de debugging y trabajo colaborativo
     \end{itemize}
   \end{frame}
   
   \begin{frame}{Preparación para la Próxima Unidad}
     \begin{itemize}
       \item \textbf{Próximamente:} [siguiente unidad/tema]
       \item \textbf{Preparación recomendada:}
         \begin{itemize}
           \item [Recurso específico 1]
           \item [Técnica o práctica 2]
         \end{itemize}
     \end{itemize}
     
     \begin{center}
       \textbf{¡Nos vemos en la próxima sesión!}
     \end{center}
   \end{frame}
   ```

## 🎨 **ELEMENTOS DE FORMATO Y ESTILO**

### **Colores y Símbolos:**

```latex
% Para ejercicios
\textcolor{red}{$\clubsuit$}

% Para soluciones
\textcolor{green}{$\checkmark$}

% Para actividades extra
\textcolor{blue}{$\clubsuit$}

% Para tareas
\textcolor{blue}{$\bigstar$}
```

### **Bloques Especiales:**

```latex
% Bloque de enunciado
\begin{block}{Enunciado}
  ...
\end{block}

% Bloque de alerta (advertencias o consejos importantes)
\begin{alertblock}{Título}
  ...
\end{alertblock}
```

### **Comentarios para Organización del Código:**

```latex
% ------------------------------------------------------------------------
% Slide N: Descripción Clara del Contenido
% ------------------------------------------------------------------------
```

### **Formato para Código Python:**

```latex
\begin{frame}[fragile]{Título del Frame}
\begin{minted}{python}
# Este es un comentario en español
variable_descriptiva = float(input("Ingrese valor con unidades: "))

# Cálculo con explicación clara
resultado = fórmula_matemática_aplicada

# Salida formateada con unidades
print(f"El resultado es: {resultado} unidades")
\end{minted}
\end{frame}
```

## 💻 **CONTENIDO ESPECÍFICO POR SEMANA**

### **Semana 01: Introducción a Python**
- **P1 (Teórica):** Sintaxis básica, variables, tipos de datos, operadores
- **P2 (Práctica):** Input/output, cálculos simples, conversiones

### **Semana 02: Estructuras de Control**
- **P1 (Teórica):** Condicionales (if-elif-else), bucles (for, while)
- **P2 (Práctica):** Aplicación en problemas físicos, validaciones, simulaciones simples

### **Semana 03: Funciones y Módulos**
- **P1 (Teórica):** Definición de funciones, parámetros, retorno, alcance de variables
- **P2 (Práctica):** Creación de módulos propios, uso de librerías externas

## 📝 **PATRONES DE EJERCICIOS RECOMENDADOS**

### **Para Semana 01:**
1. Cálculos matemáticos simples (área, perímetro)
2. Conversiones de unidades físicas
3. Fórmulas físicas básicas (F=ma, etc.)
4. Entrada/salida con validación simple

### **Para Semana 02:**
1. Clasificaciones mediante condicionales
2. Cálculos repetitivos con bucles
3. Simulaciones físicas iterativas
4. Validación de datos con bucles

### **Para Semana 03:**
1. Funciones para cálculos físicos específicos
2. Módulos temáticos (conversiones, mecánica, etc.)
3. Integración de librerías externas
4. Proyectos pequeños estructurados

## ⚡ **MEJORES PRÁCTICAS PARA CREACIÓN DE MATERIALES**

1. **Progresión lógica:**
   - Introducir conceptos antes de aplicarlos
   - Ejemplos simples → ejercicios guiados → problemas más complejos

2. **Contextualización física:**
   - Usar ejemplos relevantes para física/astronomía
   - Mencionar aplicaciones reales de los conceptos

3. **Código comentado:**
   - Comentarios explicativos en español
   - Bloques separados por funcionalidad
   - Nombres de variables descriptivos

4. **Visualización:**
   - Usar indentación clara en el código
   - Incluir resultados esperados
   - Añadir imágenes o diagramas cuando sea útil

5. **Interacción:**
   - Fomentar preguntas y discusiones
   - Incluir actividades colaborativas
   - Ofrecer retos adicionales para quienes terminan antes

## 🔧 **ERRORES COMUNES A EVITAR**

1. No crear texto antes de `\begin{document}`
2. Usar ">" en lugar de "}" para cerrar entornos
3. Olvidar importar paquetes necesarios
4. Mezclar indentación en código Python
5. No incluir unidades en problemas físicos
6. Olvidar secciones de retroalimentación
7. No cerrar correctamente entornos de minted

## 📊 **EJEMPLOS DE EJERCICIOS POR SEMANA**

### **Semana 01 (Sintaxis básica):**
- Calculadora de conversiones físicas
- Cálculo de área y perímetro
- Calculadora de energía cinética/potencial

### **Semana 02 (Estructuras de control):**
- Simulador de caída libre
- Clasificador de temperaturas
- Tabla de conversión con rangos

### **Semana 03 (Funciones y módulos):**
- Calculadora científica modular
- Biblioteca de funciones físicas
- Integración con numpy para cálculos

## 🚀 **RECOMENDACIONES FINALES**

1. **Consistencia:** Mantén el mismo estilo y formato en todas las presentaciones
2. **Progresión:** Asegúrate que cada clase construya sobre la anterior
3. **Retroalimentación:** Incluye siempre espacios para discusión y preguntas
4. **Tiempo:** Planifica ejercicios que puedan completarse en el tiempo disponible
5. **Flexibilidad:** Incluye actividades extra para estudiantes más avanzados
6. **Recursos:** Proporciona enlaces a documentación oficial y tutoriales adicionales

Este documento sirve como guía exhaustiva para mantener la consistencia y calidad en la creación de materiales para el curso de Python aplicado a Física y Astronomía.