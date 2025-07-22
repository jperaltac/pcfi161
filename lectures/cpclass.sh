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

# Construye el nombre del directorio y de los archivos de origen
week_dir="Semana${week}"
source_file1="../../../lectures/${week_dir}/${week_dir}-P1.pdf"
source_file2="../../../lectures/${week_dir}/${week_dir}-P2.pdf"

# Define los nombres de destino (manteniendo el mismo prefijo del directorio)
dest_file1="${week_dir}-C1.pdf"
dest_file2="${week_dir}-C2.pdf"

# Verifica la existencia de los archivos de origen
if [ ! -f "$source_file1" ]; then
    echo "No se encontró el archivo de origen: $source_file1"
    exit 1
fi

if [ ! -f "$source_file2" ]; then
    echo "No se encontró el archivo de origen: $source_file2"
    exit 1
fi

# Copia y renombra los archivos
cp "$source_file1" "$dest_file1"
cp "$source_file2" "$dest_file2"

echo "Archivos copiados y renombrados a ${dest_file1} y ${dest_file2}."

