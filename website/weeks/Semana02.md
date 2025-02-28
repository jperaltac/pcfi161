---
title: Semana 02
---
## Python

Esta semana comenzaremos a trabajar con nuevas funcionalidades y características en Python. 

A continuación encontrarán los archivos con el contenido de las clases, algunos videos de ayuda, y también documentación adicional para complementar los contenidos.

### Archivos de clases y lecturas obligatorias

* [Semana02-C1.pdf](/lectures/Semana02-C1.pdf)
> Este archivo contiene los *slides* presentados en la primera clase de la segunda semana. Estos suelen incluir ejercicios al final de cada presentación.
* [Semana02-C2.pdf](/lectures/Semana02-C2.pdf)
> Este archivo contiene los *slides* de la segunda clase de esta semana. Además incorpora la actividad de tarea semanal a ser entregada.

## Documentación de Apoyo y complementario

* Fases en resolución de problemas [frp.pdf](/others/frp.pdf)
> Este documento corresponde a un capítulo introductorio a como resolver problemas, desde una perspectiva más relacionado a lo que se conoce como psudocódigos. Acá no hay un enfoque a pseudocódigos en el curso, ya que *per se* Python es un lenguaje que facilita ese tipo de razonamiento.
* Escritura de Algoritmos [ea.pdf](/others/ea.pdf)
> Este documento da una descripción en la escritura de algoritmos, mediante el uso de pseudocódigos principalmente.

### Páginas de ayuda para el lenguaje Python

* [Introducción a la Programación con Python](https://www.mclibre.org/consultar/python/index.html)
* [Free Code Camp](https://www.freecodecamp.org/espanol/news/tag/python/)

------

## Instalar Python en un ambiente de Ubuntu

Tiempo estimado de Instalación, 60 minutos.

### Instalar Python en WSL

Ejecutar los siguientes comandos, abril un terminal y escribir (también puede copiar y pegar usando el mouse)

```bash
sudo apt update
sudo apt upgrade
sudo apt install python3 python3-matplotlib python3-numpy vim gnuplot-x11
```

### Instalar en MSYS2

Ejecutar los siguientes comandos, abril un terminal y escribir (también puede copiar y pegar usando el mouse)

    pacman -Syu
    pacman -Su
    pacman -S mingw-w64-x86_64-python mingw-w64-x86_64-python-matplotlib mingw-w64-x86_64-python-numpy mingw-w64-x86_64-gnuplot

### Usar Python dentro de un IDE (Integrated Development Environment)

Un ambiente IDE puede ser de gran ayuda para aquellas/os que aún no se acostumbran al uso de un terminal. Esto nos permitirá avanzar en Python, mientras vamos reforzando los conocimientos previos.

#### Anaconda

* Acceder a la pagina oficial de [Anaconda](https://www.anaconda.com/).
* Entrar a Products->Individual Edition (Open source Distribution).
* Seleccionar el sistema operativo y bajar el archivo seleccionado **Download**.
* Después ejecutar el programa y seguir las indicaciones del instalador.

#### Visual Studio Code

* Acceder a la pagina oficial de [Code](https://code.visualstudio.com/).
* Bajar el instalador para el sistema operativo que utiliza.
* Después ejecutar el programa y seguir las indicaciones del instalador.
