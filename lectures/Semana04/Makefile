# Variables
LATEX = lualatex -shell-escape -interaction=nonstopmode -halt-on-error
OUTPUT = > /dev/null 2>&1
export TEXMFCACHE := $(CURDIR)/.tex-cache
SHOWSOLUTIONS ?= 0

# Archivos fuente
TEXS = Semana04-P1.tex Semana04-P2.tex
PDFS = $(TEXS:.tex=.pdf)

all: $(PDFS)
pdf-with-answers: SHOWSOLUTIONS=1
pdf-with-answers: $(PDFS)

# Regla genérica para compilar cualquier archivo .tex a .pdf
%.pdf: %.tex
	@mkdir -p $(TEXMFCACHE)
	@if [ "$(SHOWSOLUTIONS)" = "1" ]; then \
		$(LATEX) -jobname=$(basename $<) "\\def\\SHOWSOLUTIONS{1}\\input{$<}" $(OUTPUT); \
		$(LATEX) -jobname=$(basename $<) "\\def\\SHOWSOLUTIONS{1}\\input{$<}" $(OUTPUT); \
	else \
		$(LATEX) $< $(OUTPUT); \
		$(LATEX) $< $(OUTPUT); \
	fi

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb *.fdb_latexmk *.fls *.synctex.gz
	rm -f preamble.tex
	rm -fr _minted-*/
	rm -fr _minted/
