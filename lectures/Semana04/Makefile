# Variables
LATEX = lualatex -interaction=nonstopmode -halt-on-error -shell-escape
OUTPUT = > /dev/null 2>&1

# Archivos fuente
PDFS = Semana04-P1.pdf Semana04-P2.pdf

all: $(PDFS)

# Regla genérica para compilar cualquier archivo .tex a .pdf
%.pdf: %.tex
	$(LATEX) $< $(OUTPUT)
	$(LATEX) $< $(OUTPUT)

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb *.pdf
	rm -f preamble.tex
	rm -fr _minted-*/
