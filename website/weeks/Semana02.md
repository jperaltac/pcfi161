---
title: Semana 02
---
## Python

En esta sección encontrarán los recursos básicos para iniciar este curso de *Programación para la Física y Astronomía*. Durante esta primera semana se revisarán los elementos básicos de GNU/Linux, poniendo énfasis en el uso del terminal, junto con la administración de archivos y directorios dentro del sistema.

A continuación encontrarán los archivos con el contenido de las clases, algunos videos de ayuda, y también documentación adicional para complementar los contenidos.

### Archivos de clases y lecturas obligatorias

* [PCFI161\_S02.pdf](/lectures/PCFI161\_S02.pdf)
> Este archivo contiene los *slides* presentados en la clase. Estos suelen incluir ejercicios al final de cada presentación.
* Fases en resolución de problemas [frp.pdf](/others/frp.pdf)
> Este documento corresponde a un capítulo introductorio a los elementos básicos para el uso de GNU/Linux. Es una lectura obligatoria del curso.
* Escritura de Algoritmos [ea.pdf](/others/ea.pdf)
> Este codumento corresponde a la escritura de algoritmos.

### Páginas de ayuda para el lenguaje Python

* [Introducción a la Programación con Python](https://www.mclibre.org/consultar/python/index.html)
* [Free Code Camp](https://www.freecodecamp.org/espanol/news/tag/python/)

------

## Instalar Python en un ambiente de Ubuntu

Tiempo estimado de Instalación, 60 minutos.

### Instalar Python en WSL

Ejecutar los siguientes comandos, abril un terminal y escribir (también puede copiar y pegar usando el mouse)

    sudo apt update
    sudo apt upgrade
    sudo apt install python3 python3-matplotlib python3-numpy vim gnuplot-x11

### Instalar en MSYS2

Ejecutar los siguientes comandos, abril un terminal y escribir (también puede copiar y pegar usando el mouse)

    pacman -Syu
    pacman -Su
    pacman -S mingw-w64-x86_64-python mingw-w64-x86_64-python-matplotlib mingw-w64-x86_64-python-numpy mingw-w64-x86_64-gnuplot

### Usar Python dentro de un IDE (Integrated Development Environment)

Un ambien IDE puede ser de gran ayuda para aquellas/os que aún no se acostumbran al uso de un terminal. Esto nos permitirá avanzar en Python, mientras vamos reforzando los conocimientos previos.

#### Anaconda

* Acceder a la pagina oficial de [Anaconda](https://www.anaconda.com/).
* Entrar a Products->Individual Edition (Open source Distribution).
* seleccionar el sistema operativo y bajar el archivo seleccionado **Download**.
* Después ejecutar el programa y seguir las indicaciones del instalador.

#### Visual Studio Code

* Acceder a la pagina oficial de [Code](https://code.visualstudio.com/).
* Bajar el instalador para el sistema operativo que utiliza.
* Después ejecutar el programa y seguir las indicaciones del instalador.
