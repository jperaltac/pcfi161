# ========= Config =========
MAIN            := main
RUBRICA_MAIN    := main_rubrica
LATEXMK         := latexmk
LATEXMK_FLAGS   := -lualatex -shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -synctex=1
LATEXMK_ANSWERS := $(LATEXMK) $(LATEXMK_FLAGS) -lualatex="lualatex %O '\def\WITHANSWERS{1}\input{%S}'"
TEX_CACHE_DIR   := .texlive-cache
export TEXMFCACHE := $(CURDIR)/$(TEX_CACHE_DIR)
export TEXMFVAR   := $(CURDIR)/$(TEX_CACHE_DIR)

PROBLEMS := $(wildcard problems/*.tex)

.PHONY: all pdf pdf-rubrica pdf-with-answers pdf-rubrica-with-answers watch watch-answers watch-rubrica clean distclean minted-cache tex-cache

# Compilación por defecto (sin respuestas)
all: pdf

pdf: $(MAIN).pdf

pdf-rubrica: $(RUBRICA_MAIN).pdf

pdf-with-answers: $(MAIN)-answers.pdf $(RUBRICA_MAIN)-answers.pdf

pdf-rubrica-with-answers: $(RUBRICA_MAIN)-answers.pdf

$(MAIN).pdf: $(MAIN).tex preamble.tex $(PROBLEMS) | minted-cache tex-cache
	$(LATEXMK) $(LATEXMK_FLAGS) $(MAIN).tex

$(RUBRICA_MAIN).pdf: $(RUBRICA_MAIN).tex preamble.tex ../../problems/rubrica-t1.tex | tex-cache
	$(LATEXMK) $(LATEXMK_FLAGS) $(RUBRICA_MAIN).tex

$(MAIN)-answers.pdf: $(MAIN).tex preamble.tex $(PROBLEMS) | minted-cache tex-cache
	$(LATEXMK_ANSWERS) -jobname='$(MAIN)-answers' $(MAIN).tex

$(RUBRICA_MAIN)-answers.pdf: $(RUBRICA_MAIN).tex preamble.tex ../../problems/rubrica-t1.tex | tex-cache
	$(LATEXMK_ANSWERS) -jobname='$(RUBRICA_MAIN)-answers' $(RUBRICA_MAIN).tex

# Modo observar (con respuestas)
watch-answers: minted-cache tex-cache
	$(LATEXMK_ANSWERS) -pvc -jobname='$(MAIN)-answers' $(MAIN).tex

# Observa cambios (sin respuestas)
watch: minted-cache tex-cache
	$(LATEXMK) $(LATEXMK_FLAGS) -pvc $(MAIN).tex

watch-rubrica: tex-cache
	$(LATEXMK) $(LATEXMK_FLAGS) -pvc $(RUBRICA_MAIN).tex

# Carpetas de caché
tex-cache:
	mkdir -p $(TEX_CACHE_DIR)

minted-cache:
	mkdir -p _minted-$(MAIN)

# Limpieza de temporales
clean:
	$(LATEXMK) -c $(MAIN).tex
	$(LATEXMK) -c $(RUBRICA_MAIN).tex
	$(LATEXMK) -c -jobname='$(MAIN)-answers' $(MAIN).tex
	$(LATEXMK) -c -jobname='$(RUBRICA_MAIN)-answers' $(RUBRICA_MAIN).tex
	rm -f *.synctex.gz *.fls *.fdb_latexmk *.aux *.log
	rm -rf _minted-$(MAIN) $(TEX_CACHE_DIR)

# Limpieza total (incluye PDF)
distclean: clean
	rm -f $(MAIN).pdf $(RUBRICA_MAIN).pdf $(MAIN)-answers.pdf $(RUBRICA_MAIN)-answers.pdf
