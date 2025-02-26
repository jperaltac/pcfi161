# Makefile de ejemplo
# ===================
# Este Makefile asume que el archivo preamble.tex
# está en la carpeta padre de donde estamos (../preamble.tex).
# Luego copia preamble.tex a la carpeta actual y compila.

all: Semana05-P1.pdf

# Regla para compilar la parte 1
Semana05-P1.pdf: Semana05-P1.tex
	lualatex Semana05-P1.tex
	# Se suele compilar 2 veces para actualizar referencias
	lualatex Semana05-P1.tex

# Copiamos preamble.tex desde un nivel superior
#preamble.tex:
#	cp ../preamble.tex .

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb *.pdf
	rm -f preamble.tex
	rm -fr _minted/
