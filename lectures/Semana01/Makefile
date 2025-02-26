# Variables
LATEX = lualatex -interaction=nonstopmode -halt-on-error
OUTPUT = > /dev/null 2>&1

# Archivos fuente
PDFS = Semana01-P1.pdf Semana01-P2.pdf

all: $(PDFS)

# Regla genérica para compilar cualquier archivo .tex a .pdf
%.pdf: %.tex
	$(LATEX) $< $(OUTPUT)
	$(LATEX) $< $(OUTPUT)

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb *.pdf
	rm -f preamble.tex
	rm -fr _minted/
