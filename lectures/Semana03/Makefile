# Makefile de ejemplo
# ===================
# Este Makefile asume que el archivo preamble.tex
# está en la carpeta padre de donde estamos (../preamble.tex).
# Luego copia preamble.tex a la carpeta actual y compila.

all: Semana03-P1.pdf Semana03-P2.pdf

# Regla para compilar la parte 1
Semana03-P1.pdf: Semana03-P1.tex preamble.tex
	lualatex Semana03-P1.tex
	# Se suele compilar 2 veces para actualizar referencias
	lualatex Semana03-P1.tex

# Regla para compilar la parte 2
Semana03-P2.pdf: Semana03-P2.tex preamble.tex
	lualatex Semana03-P2.tex
	lualatex Semana03-P2.tex

# Copiamos preamble.tex desde un nivel superior
preamble.tex:
	cp ../preamble.tex .

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb *.pdf
	rm -f preamble.tex
	rm -fr _minted/
