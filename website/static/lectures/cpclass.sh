#!/bin/bash

# Verifica que se haya pasado un argumento
if [ -z "$1" ]; then
    echo "Uso: $0 SXX (donde XX es el número de la semana, ej. S01, S02, ...)"
    exit 1
fi

# Valida que el argumento tenga el formato correcto: S + dos dígitos
if [[ ! "$1" =~ ^S[0-9]{2}$ ]]; then
    echo "Argumento no válido. Debe tener el formato SXX (ejemplo: S01, S02, etc.)"
    exit 1
fi

# Extrae el número de semana (ej. "01", "02", ...)
week="${1:1}"

# Construye el nombre del directorio y de los archivos
week_dir="Semana${week}"
file1="../../../lectures/${week_dir}/${week_dir}-P1.pdf"
file2="../../../lectures/${week_dir}/${week_dir}-P2.pdf"

# Verifica la existencia de los archivos antes de copiarlos
if [ ! -f "$file1" ]; then
    echo "No se encontró el archivo: $file1"
fi

if [ ! -f "$file2" ]; then
    echo "No se encontró el archivo: $file2"
fi

# Copia los archivos (si no existen, se mostrará error de cp)
cp "$file1" .
cp "$file2" .

echo "Archivos de ${week_dir} copiados exitosamente."

