# Variables
PATH := /Library/TeX/texbin:/opt/homebrew/opt/python@3.11/libexec/bin:$(PATH)
export PATH
SELFAUTOLOC := $(shell /Library/TeX/texbin/kpsewhich -var-value=SELFAUTOLOC)
SELFAUTODIR := $(shell /Library/TeX/texbin/kpsewhich -var-value=SELFAUTODIR)
SELFAUTOPARENT := $(shell /Library/TeX/texbin/kpsewhich -var-value=SELFAUTOPARENT)
export SELFAUTOLOC SELFAUTODIR SELFAUTOPARENT
OUTPUT = > /dev/null 2>&1
export TEXMFCACHE := $(CURDIR)/.tex-cache
export TEXMFVAR := $(CURDIR)/.tex-var
export TEXMF_OUTPUT_DIRECTORY := $(CURDIR)
LATEX_ENV = env PATH="$(PATH)" TEXMFCACHE="$(TEXMFCACHE)" TEXMFVAR="$(TEXMFVAR)" TEXMF_OUTPUT_DIRECTORY="$(TEXMF_OUTPUT_DIRECTORY)" SELFAUTOLOC="$(SELFAUTOLOC)" SELFAUTODIR="$(SELFAUTODIR)" SELFAUTOPARENT="$(SELFAUTOPARENT)"
LATEX = $(LATEX_ENV) /Library/TeX/texbin/lualatex -interaction=nonstopmode -halt-on-error -shell-escape
SHOWSOLUTIONS ?= 0

# Archivos fuente
TEXS = Semana16-P1.tex
PDFS = $(TEXS:.tex=.pdf)

.PHONY: all clean pdf-with-answers pdf-answers

all:
	@$(MAKE) --no-print-directory -B $(PDFS) SHOWSOLUTIONS=0

pdf-with-answers: SHOWSOLUTIONS=1
pdf-with-answers:
	@$(MAKE) --no-print-directory -B $(PDFS) SHOWSOLUTIONS=1

pdf-answers: pdf-with-answers

# Regla generica para compilar cualquier archivo .tex a .pdf
%.pdf: %.tex
	@mkdir -p $(TEXMFCACHE) $(TEXMFVAR)
	@if [ "$(SHOWSOLUTIONS)" = "1" ]; then \
		$(LATEX) -jobname=$(basename $<) "\\def\\SHOWSOLUTIONS{1}\\input{$<}" $(OUTPUT) || { tail -n 80 "$(basename $<).log"; exit 1; }; \
		$(LATEX) -jobname=$(basename $<) "\\def\\SHOWSOLUTIONS{1}\\input{$<}" $(OUTPUT) || { tail -n 80 "$(basename $<).log"; exit 1; }; \
	else \
		$(LATEX) $< $(OUTPUT) || { tail -n 80 "$(basename $<).log"; exit 1; }; \
		$(LATEX) $< $(OUTPUT) || { tail -n 80 "$(basename $<).log"; exit 1; }; \
	fi

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb *.fdb_latexmk *.fls *.synctex.gz *.cut
	rm -f preamble.tex
	rm -fr .tex-cache .tex-var
	rm -fr _minted-*/
	rm -fr _minted/
