---
title: Semana 04
---
## Estudiando

Esta semana recuperaremos cualquier contenido que no se cubriera en las semanas previas, y adicionalmente ejercitaremos en los distintos ejercicios de las guías.

### Video explicativo de como realizar su evaluación Solemne

Este video muestra como trabajar con la plataforma Hacker Rank luego de recibir la invitación para realizar su evaluación.

* https://youtu.be/0ypt8_u6eyo

### Video explicativo

Este video muestra como acceder para copiar/pegar ficheros desde su interfaz WSL a su sistema Windows.

* https://youtu.be/ayibXP69VVE 


### Actividades adicionales para la semana 4

* [trabajando\_en\_el\_terminal\_v02.pdf](/others/s04/trabajando_en_el_terminal_v02.pdf)
> Altamente recomendado, sobre todo realizar en clases.
* [practica_linux.zip](/others/s04/practica_linux.zip)
> Este set de archivos sirve para realizar algunos de los ejercicios anteriores.

### Más actividades
* [trabajo\_personal\_semana04\_v04.pdf](/others/s04/trabajo_personal_semana04_v04.pdf)
* [datos2.txt](/others/s04/datos2.txt) 

----------------------

## Trabajando con archivos ZIP

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

