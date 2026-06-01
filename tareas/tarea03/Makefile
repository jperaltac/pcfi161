# ========= Config =========
MAIN            := main
LATEXMK         := latexmk
LATEXMK_FLAGS   := -lualatex -shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -synctex=1
LATEXMK_ANSWERS := $(LATEXMK) $(LATEXMK_FLAGS) -lualatex="lualatex %O '\def\WITHANSWERS{1}\input{%S}'"
TEX_CACHE_DIR   := .texlive-cache
export TEXMFCACHE := $(CURDIR)/$(TEX_CACHE_DIR)
export TEXMFVAR   := $(CURDIR)/$(TEX_CACHE_DIR)

PROBLEMS := $(wildcard problems/*.tex)

.PHONY: all pdf pdf-with-answers watch watch-answers clean distclean minted-cache tex-cache

# Compilación por defecto (sin respuestas)
all: pdf

pdf: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex preamble.tex $(PROBLEMS) | minted-cache tex-cache
	$(LATEXMK) $(LATEXMK_FLAGS) $(MAIN).tex


# Con respuestas visibles: genera un PDF separado
pdf-with-answers: $(MAIN)-answers.pdf

$(MAIN)-answers.pdf: $(MAIN).tex preamble.tex $(PROBLEMS) | minted-cache tex-cache
	$(LATEXMK_ANSWERS) -jobname='$(MAIN)-answers' $(MAIN).tex

# Modo observar (con respuestas)
watch-answers: minted-cache tex-cache
	$(LATEXMK_ANSWERS) -pvc -jobname='$(MAIN)-answers' $(MAIN).tex

# Observa cambios (sin respuestas)
watch: minted-cache tex-cache
	$(LATEXMK) $(LATEXMK_FLAGS) -pvc $(MAIN).tex

# Carpetas de caché
tex-cache:
	mkdir -p $(TEX_CACHE_DIR)

minted-cache:
	mkdir -p _minted-$(MAIN)

# Limpieza de temporales
clean:
	$(LATEXMK) -c $(MAIN).tex
	$(LATEXMK) -c -jobname='$(MAIN)-answers' $(MAIN).tex
	rm -f *.synctex.gz *.fls *.fdb_latexmk *.aux *.log
	rm -rf _minted-$(MAIN) $(TEX_CACHE_DIR)

# Limpieza total (incluye PDF)
distclean: clean
	rm -f $(MAIN).pdf $(MAIN)-answers.pdf
