---
title: Semana 03
---

## Python

A continuación encontrarán los archivos con el contenido de las clases, algunos videos de ayuda, y también documentación adicional para complementar los contenidos.

### Archivos de clases y lecturas obligatorias

* [Semana03-C1.pdf](/lectures/Semana03-C1.pdf)

> Este archivo contiene los *slides* presentados en la primera clase de la tercera semana. Estos suelen incluir ejercicios al final de cada presentación.

* [Semana03-C2.pdf](/lectures/Semana03-C2.pdf)

> Este archivo contiene una guía con algunos ejercicios para desarrollar inicalmente, y luego la tarea grupal Semanal.

## Material Complementario

### Configurando un menú contextual "Bash"

#### **MSYS2/windows**

Podrá hacer clic con el botón derecho del mouse en windows y ejecute el shell MSYS2 MINGW32/64 en la carpeta seleccionada

página del programa [https://github.com/njzhangyifei/msys2-mingw-shortcut-menus](https://github.com/njzhangyifei/msys2-mingw-shortcut-menus)

Abra un terminal en MSYS2 y ejecute los siguientes comandos

```
pacman -S git  
git clone https://github.com/njzhangyifei/msys2-mingw-shortcut-menus.git
cd msys2-mingw-shortcut-menus
./install
```

se crea el archivo `install\_right\_click\_menu.reg` en la carpeta `msys2-mingw-shortcut-menus`  
en windows busque el archivo `.reg` y hacer doble clic sobre él para finalizar la instalación

![](/img/menu_msys2.png) 

#### **WSL/ubuntu**

Podrá hacer clic con el botón derecho del mouse en windows y ejecute el shell WSL ubuntu en la carpeta seleccionada

**Primera Opción** 

Al instalar WSL, puede abrir un terminal en la carpeta selecciona, pero debe presionar la tecla `Mayús` y después el botón derecho del mouse, en el menú emergente aparecerá la opción "**Abrir shell de Linux aquí**"

![](/img/menu_wsl2.png)

Si no está activa la primera opción, puede realizar la instalación con la segunda opción. 

**Segunda Opción**

Página del programa   [https://winaero.com/add-bash-context-menu-windows-10/](https://winaero.com/add-bash-context-menu-windows-10/)

 unzip your-file.zip -d directorybash

Ver video de instalación [https://www.youtube.com/watch?v=7dEnc5p0pqs](https://www.youtube.com/watch?v=7dEnc5p0pqs)  

![](/img/menu_wsl.png)


#### MAC OS

Podrá el ejecute el Shell de MAC OS usando el mouse en la carpeta seleccionada, se debe activar en mac, ver el siguiente video

[https://www.youtube.com/watch?v=iVTGhoCjGTI](https://www.youtube.com/watch?v=iVTGhoCjGTI)

#### LINUX

Los usuarios que tiene instalado alguna distribución de GNU/linux, el abrir un terminal en una carpeta esta activo de por defecto.

-------------

## PyInstaller

**¿Qué hace pyinstaller?**  
Lo que hace es generar un . EXE en Windows, un . DMG en MAC o el ejecutable que utilice el sistema operativo. Dentro del ejecutable se incluye el propio intérprete de Python, y por esa razón podremos utilizarlo en cualquier ordenador sin necesidad de instalar Python previamente.

#### MSYS2/windows

Abrir el terminal "msys2\_MinGW\_x64" y ejecute los siguientes comandos  

```
pacman -S mingw-w64-x86\_64-python-pip  
pip -V  
pip install pyinstaller
```

#### **WSL/ubuntu**

Abra un terminal en WSL/ubuntu y ejecute los siguientes comando

```
sudo apt install python3-pip  
pip -V  
pip install pyinstaller
```

#### **Probar Pyinstaller**

_Abra un termina y ejecute los siguientes comandos_

```bash
nano prueba_pyinstaller.py
```

copy el siguientes codigo de python en el archivo prueba\_pyinstaller.py (puede bajar el archivo [prueba\_pyinstaller.py](https://unab.blackboard.com/bbcswebdav/pid-7920269-dt-content-rid-41113780_1/xid-41113780_1) )

```python
x=1  
print(x)  
x=2  
print(x)
```

Guarde el archivo y salga del editor. Luego ejecute los siguientes comandos

```bash
pyinstaller prueba\_pyinstaller.py --onefile  
./dist/prueba\_pyinstaller
```

Se crea el ejecutable en la carpeta `dist`, revise los descrito ejecute los siguientes comandos

```bash
cd dist  
ls -al  
./prueba\_pyinstaller
```

----------------------------------

## Anaconda / Windows

Ejecute el `cmd` de anaconda como administrador, ver figura (Anaconda Prompt) o (Anacona Powershell)


![](/img/anaconda_cmd.png)  


En terminal escriba los siguientes comandos

```powershell
conda update anaconda  
pip -V
pip install pyinstaller
```

Podrá hacer clic con el botón derecho del Mouse en windows y ejecute el `cmd` de windows en la carpeta seleccionada

bajar el archivo [anaconda\_menu.reg](https://unab.blackboard.com/bbcswebdav/pid-7920273-dt-content-rid-41113782_1/xid-41113782_1) y en windows busque el archivo .reg y hacer doble clic sobre él para finalizar la instalación.

Pruebe el funcionamiento de  pyinstaller con las instrucciones dadas anteriormente, pero habrá un terminal de windows conocido como `cmd` usando el botón derecho del mouse en la carpeta donde está el archivo python.


![](/img/anaconda_cmd2.png)
