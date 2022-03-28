---
title: Semana 01
---
# Elementos Fundamentales

En esta sección encontrarán algunos elementos básicos para iniciar este curso, entre los que destacan el uso de GNU/Linux, especialmente la terminal.

## Archivos

* PCFI161\_S01.pdf
	> Este archivo contiene los slides presentados en la clase. Estos suelen incluir ejercicios al final de cada presentación.
* c2.pdf
	> Este fichero corresponde a un capítulo con una introducción a los elementos básicos para el uso de GNU/Linux. Es una lectura obligatoria del curso.

## Videos

1. https://www.youtube.com/watch?v=y-Hjkgka0lI  : Video que muestra como instalar WSL en Windows comandos usados y corregidos
	* wsl --install
	* apt --help
	* sudo apt update
	* sudo apt full-upgrade
	* sudo apt  upgrade
	* sudo apt install python3 python3-matplotlib  python3-numpy vim gnuplot-x11
	* sudo apt-cache search adwaita
	* sudo apt install  adwaita-icon-theme-full
2. https://www.youtube.com/watch?v=laN-oho3Z2A : Video que muestra como instalar VMWARE en Windows
3. https://www.youtube.com/watch?v=Eq52Kp\_SjeU : Video que muestra elementos básicos de terminales y ssh.

# Software para Microsoft Windows 10/11.

## Editor de Texto
	Notepad++ es un editor de texto y de código fuente libre con soporte para varios lenguajes de programación. Con soporte nativo para Microsoft Windows.
https://notepad-plus-plus.org/

## GNU/Linux dentro de Windows
* WSL
* MSYS2
	MSYS2 es un software que simula el entorno de Linux en Windows. La mayoría de los comandos de shell se pueden usar en msys2.
https://www.msys2.org/
	Al ingresar a la página de MSYS2 encontrar las instrucciones de como instalar, se recomienda por ser de fácil instalación y se instalan varios programas que se usaran en el curso, como ls, pwd, etc.
	En MSYS2 se utiliza el comando "pacman" para instalar programas y actulizar, para ver la ayuda escriba el comando pacman --help
	Ejecutar MSYS2 en windows
	Para actualice la base de datos de paquetes de MSYS2 ejecute
	* pacman -Syu 
        Actualice el resto de los paquetes ejecutando
	* pacman -Su 
	Instale los siguientes programas
	* pacman -S mc 
	* pacman -S vim
	* pacman -S man
	tambien puede instalar todos los programas usando el siguiente comando
	* pacman -S mc vim man
	otros programas que pueden instalar
	* pacman -S mingw-w64-x86_64-python mingw-w64-x86_64-python-matplotlib mingw-w64-x86_64-python-numpy mingw-w64-x86_64-gnuplot

