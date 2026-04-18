# Variables
LATEX = lualatex -interaction=nonstopmode -halt-on-error -shell-escape
OUTPUT = > /dev/null 2>&1
export TEXMFCACHE := $(CURDIR)/.tex-cache
export TEXMFVAR := $(CURDIR)/.tex-var
SHOWSOLUTIONS ?= 0

# Archivos fuente
TEXS = Semana06-P1.tex Semana06-P2.tex
PDFS = $(TEXS:.tex=.pdf)

all: $(PDFS)
pdf-with-answers: SHOWSOLUTIONS=1
pdf-with-answers: $(PDFS)

# Regla genérica para compilar cualquier archivo .tex a .pdf
%.pdf: %.tex
	@mkdir -p $(TEXMFCACHE) $(TEXMFVAR)
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
	rm -fr .tex-cache .tex-var
	rm -fr _minted-*/
	rm -fr _minted/
