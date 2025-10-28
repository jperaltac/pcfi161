# 📚 Sistema de Estructura Base para Canvas

## ✨ Nuevas Funcionalidades

### 1. **Estructura Base Completa**
El sistema ahora genera automáticamente una estructura base con **posiciones predefinidas** para todos los elementos:

```python
estructura_base = {
    "UNIDAD I: ELEMENTOS BÁSICOS": {
        'position': 1,
        'semanas': {
            1: {'titulo': 'Semana 01', 'position': 2, ...},
            2: {'titulo': 'Semana 02', 'position': 5, ...}
        }
    },
    ...
}
```

### 2. **Función `ver_estructura_base()`**
Visualiza toda la estructura con posiciones:

```python
import Canvas_Key

Canvas_Key.ver_estructura_base()
```

**Salida:**
```
================================================================================
📚 ESTRUCTURA BASE DEL MÓDULO
================================================================================

[1] UNIDAD I: ELEMENTOS BÁSICOS (indent=0)
  [2] Semana 01 (indent=1)
    [3] Semana01-P1.pdf (indent=2)
    [4] Semana01-P2.pdf (indent=2)
  [5] Semana 02 (indent=1)
    [6] Semana02-P1.pdf (indent=2)
    [7] Semana02-P2.pdf (indent=2)

[8] UNIDAD II: PROGRAMACIÓN EN PYTHON (indent=0)
  [9] Semana 03 (indent=1)
    [10] Semana03-P1.pdf (indent=2)
    [11] Semana03-P2.pdf (indent=2)
  ...

Total de items en estructura base: 96
================================================================================
```

### 3. **Reordenamiento Mejorado**
La función `_reordenar_unidades()` ahora:
- ✅ Compara contra la estructura base
- ✅ Asigna posiciones exactas (1, 2, 3, ...)
- ✅ Reposiciona solo lo necesario
- ✅ Muestra detalles de cada cambio

## 🎯 Uso

### Ordenar Módulo Completo
```python
import Canvas_Key

# Conectar
Canvas_Key.select_user('David')

# Ordenar todo según estructura base
Canvas_Key.ordenar_modulo()
```

### Ver Estructura Base
```python
# Ver la estructura completa con posiciones
Canvas_Key.ver_estructura_base()
```

### Subir Contenido (automáticamente ordena)
```python
# Al subir contenido, se ordena automáticamente
Canvas_Key.subir_contenido(10)
```

## 📊 Estructura Completa

```
UNIDAD I: ELEMENTOS BÁSICOS
    Semana 01
        Semana01-P1.pdf
        Semana01-P2.pdf
    Semana 02
        Semana02-P1.pdf
        Semana02-P2.pdf

UNIDAD II: PROGRAMACIÓN EN PYTHON
    Semana 03
        Semana03-P1.pdf
        Semana03-P2.pdf
    Semana 04
        Semana04-P1.pdf
        Semana04-P2.pdf
    Semana 05
        Semana05-P1.pdf
        Semana05-P2.pdf

UNIDAD III: CONTROLADORES Y ARREGLOS
    Semana 06
        Semana06-P1.pdf
        Semana06-P2.pdf
    Semana 07
        Semana07-P1.pdf
        Semana07-P2.pdf

UNIDAD IV: EL CICLO FOR, GRÁFICAS
    Semana 08
        Semana08-P1.pdf
        Semana08-P2.pdf
    Semana 09
        Semana09-P1.pdf
        Semana09-P2.pdf
    Semana 10
        Semana10-P1.pdf
        Semana10-P2.pdf

UNIDAD V: CLASES & ANALISIS DE DATOS
    Semana 11
        Semana11-P1.pdf
        Semana11-P2.pdf
    Semana 12
        Semana12-P1.pdf
        Semana12-P2.pdf

UNIDAD VI: ALGORITMOS, & PERFORMANCE
    Semana 13
        Semana13-P1.pdf
        Semana13-P2.pdf
    Semana 14
        Semana14-P1.pdf
        Semana14-P2.pdf
    Semana 15
        Semana15-P1.pdf
        Semana15-P2.pdf
```

## 🔧 Ventajas del Nuevo Sistema

1. **Posiciones Predefinidas**: Cada elemento tiene una posición fija (1-96)
2. **Reordenamiento Preciso**: Compara contra estructura ideal
3. **Debugging Fácil**: Visualiza estructura completa
4. **Mantenimiento Simple**: Modificar solo el diccionario `unidades`
5. **Escalable**: Agregar nuevas unidades/semanas es fácil

## 📝 Notas

- El sistema maneja 6 unidades
- Total de 15 semanas
- Asume 2 PDFs por semana (P1 y P2)
- Semana 10 y 15 pueden tener solo 1 archivo
- Las posiciones se calculan automáticamente
