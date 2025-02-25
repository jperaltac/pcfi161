# Makefile de ejemplo
# ===================
# Este Makefile asume que el archivo preamble.tex
# está en la carpeta padre de donde estamos (../preamble.tex).
# Luego copia preamble.tex a la carpeta actual y compila.

all: Semana02-P1.pdf Semana02-P2.pdf

# Regla para compilar la parte 1
Semana02-P1.pdf: Semana02-P1.tex preamble.tex
	pdflatex Semana02-P1.tex
	# Se suele compilar 2 veces para actualizar referencias
	pdflatex Semana02-P1.tex

# Regla para compilar la parte 2
Semana02-P2.pdf: Semana02-P2.tex preamble.tex
	pdflatex Semana02-P2.tex
	pdflatex Semana02-P2.tex

# Copiamos preamble.tex desde un nivel superior
preamble.tex:
	cp ../preamble.tex .

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb *.pdf
	rm -f preamble.tex

