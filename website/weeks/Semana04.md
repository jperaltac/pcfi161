---
title: Semana 04
---
## Estudiando

Esta semana recuperaremos cualquier contenido que no se cubriera en las semanas previas, y adicionalmente ejercitaremos en los distintos ejercicios de las guías.

### Actividades adicionales para la semana 4

*   [trabajo\_personal\_semana04\_v04.pdf](/others/s04/trabajo_personal_semana04_v04.pdf)
*   f1
*   f2
*   f3

----------------------

## Archivos ZIP

**¿Qué es un archivo ZIP?**

ZIP es un formato de archivos que se usa ampliamente para comprimir uno o más archivos juntos en una sola ubicación, con lo cual se reduce el tamaño en general y se facilita la transportación de los archivos.

Se requiere el programa `unzip` para descomprimir archivos .zip y el programa zip para comprimir archivos.

Los comandos para instalar los programas `unzip` y `zip`, si no se encuentra instalado son:

### MSYS2/windows

Abrir el terminal "msys2" y ejecute el siguiente comandos    

```
pacman -S unzip zip
```

### **WSL/ubuntu**

Abra un terminal en WSL/ubuntu y ejecute el siguiente comando

```bash
sudo apt install unzip zip  
```

### **Ayuda de unzip**

Para descomprimir el archivo en el directorio actual, usa el siguiente comando.

```bash
unzip your-file.zip  
```


Para descomprimir el archivo en un directorio diferente, usa este comando en su lugar.

```bash
unzip your-file.zip -d directory
```

