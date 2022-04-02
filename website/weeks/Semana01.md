---
title: Semana 01
---
# Elementos Fundamentales

En esta sección encontrarán los recursos básicos para iniciar el curso de *Programación para la Física y Astronomía*. Durante esta primera semana se revisarán los elementos básicos de GNU/Linux, poniendo énfasis en el uso del terminal, junto con la administración de archivos y directorios dentro del sistema.

A continuación encontrarán los archivos con el contenido de clases, videos de ayuda, y documentación adicional para complementar los contenidos.

## Archivos

* [PCFI161\_S01.pdf](/lectures/PCFI161\_S01.pdf)
	> Este archivo contiene los *slides* presentados en la clase. Estos suelen incluir ejercicios al final de cada presentación.
* [c2.pdf](/others/c2.pdf)
	> Este documento corresponde a un capítulo introductorio a los elementos básicos de GNU/Linux. Es una lectura obligatoria del curso. El documento, es un trabajo en desarrollo.

## Videos

En esta sección podrán encontrar videos de ayuda que las/los guiarán en el proceso de instalación de los recursos necesarios para el curso. Usted podrá utilizar un sistema GNU/Linux de la forma que más se acomode a sus necesidades entre las que destacan:

- **WSL** : *Windows Subsystem for Linux*. Es una incorporación de un sistema **GNU/Linux dentro de Windows**. Con el se puede trabajar sin inconvenientes. La versión de Windows 11 incorpora un ambiente gráfico, en Windows 10 suele requerir la instalación de GWSL (Windows Store), para aplicaciones gráficas.
- **MSYS2** : Similar a WSL, pero es independiente como software.
- **VirtualBox / VMware** : Sistemas de virtualización, que permiten instalar un sistema operativo, dentro de otro. Por ejemplo tener una máquina virtual de GNU/Linux dentro de Microsoft Windows.

A continuación verán los videos principales, para distintos casos.

1. https://www.youtube.com/watch?v=y-Hjkgka0lI  : Video que muestra como instalar **WSL** en Windows. También incluye la actualización de Ubuntu, y la instalación de software adicional que será utilizado en WSL.
2. https://www.youtube.com/watch?v=laN-oho3Z2A : Video que muestra como instalar **VMWARE** en Windows. El procedimiento para el uso de Virtualbox es muy similar.
3. https://www.youtube.com/watch?v=Eq52Kp\_SjeU : Video que muestra elementos básicos para comprender el uso de terminales y ssh.



------

# Otro Software para Microsoft Windows 10/11.


## Editores de Texto

Dentro del terminal de GNU/Linux utilizaremos `vim` de forma regular, pero luego de aprender lo fundamental, podrá sentirse libre de utilizar otros editores.

Acá existe una larga variedad de Editores para Windows, entre los que destacamos

1. **gvim** : https://www.vim.org/download.php
2. **visual studio code** :  https://code.visualstudio.com/Download
3. **notepad++** : https://notepad-plus-plus.org/



## GNU/Linux dentro de Windows

Para instalar un sistema GNU/Linux dentro de un computador con Windows, recomendamos **WSL** (preferido), o **MSYS2**.

* **WSL** : En la sección previa de Videos encontrará información más detallada.

* **MSYS2** : Es un software que simula el entorno de Linux en Windows. La mayoría de los comandos de shell se pueden usar en msys2.

  ​				https://www.msys2.org/
  ​	Al ingresar a la página de MSYS2 encontrar las instrucciones de como instalar, se recomienda por ser de fácil instalación y se instalan varios programas que se usaran en el curso, como `ls`, `pwd`, etc. En MSYS2 se utiliza el comando `pacman` para instalar programas y actualizar, para ver la ayuda escriba el comando `pacman --help`.

  ​	**Ejecutar MSYS2 en windows**
  ​	Para actualizar la base de datos de paquetes de MSYS2 ejecute

  * `pacman -Syu` 
        Actualice el resto de los paquetes ejecutando

  * `pacman -Su` 
    Instale los siguientes programas

  * `pacman -S mc` 

  * `pacman -S vim`

  * `pacman -S man`

    También puede instalar todos los programas de una vez usando 

  * `pacman -S mc vim man`

    

  ​    Otros programas que pueden instalar

  * `pacman -S mingw-w64-x86_64-python mingw-w64-x86_64-python-matplotlib mingw-w64-x86_64-python-numpy mingw-w64-x86_64-gnuplot`

