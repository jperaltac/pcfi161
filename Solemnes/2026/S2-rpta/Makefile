# ========= Config =========
MAIN            := main
LATEXMK         := latexmk
LATEXMK_FLAGS   := -lualatex -shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -synctex=1
TEX_CACHE_DIR   := .texlive-cache
export TEXMFCACHE := $(CURDIR)/$(TEX_CACHE_DIR)
export TEXMFVAR   := $(CURDIR)/$(TEX_CACHE_DIR)

PROBLEMS := $(wildcard problems/*.tex)

.PHONY: all pdf pdf-with-answers watch watch-answers clean distclean minted-cache tex-cache

# Compilación por defecto (sin respuestas)
all: pdf

pdf: minted-cache tex-cache
	$(LATEXMK) -g $(LATEXMK_FLAGS) $(MAIN).tex

$(MAIN).pdf: $(MAIN).tex preamble.tex $(PROBLEMS) | minted-cache tex-cache
	$(LATEXMK) $(LATEXMK_FLAGS) $(MAIN).tex


# Con respuestas visibles: define \WITHANSWERS antes de compilar
pdf-with-answers: minted-cache tex-cache
	$(LATEXMK) -g $(LATEXMK_FLAGS) \
	  -lualatex="lualatex %O '\\def\\WITHANSWERS{1}\\input{%S}'" \
	  $(MAIN).tex

# Modo observar (con respuestas)
watch-answers: minted-cache tex-cache
	$(LATEXMK) $(LATEXMK_FLAGS) -pvc \
	  -lualatex="lualatex %O '\\def\\WITHANSWERS{1}\\input{%S}'" \
	  $(MAIN).tex

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
	$(LATEXMK) -C
	rm -rf _minted-$(MAIN) $(TEX_CACHE_DIR)

# Limpieza total (incluye PDF)
distclean: clean
	rm -f $(MAIN).pdf
