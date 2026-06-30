# ========= Config =========
MAIN            := main
LATEXMK         := latexmk
LATEXMK_FLAGS   := -lualatex -shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -synctex=1
TEX_CACHE_DIR   := .texlive-cache
export TEXMFCACHE := $(CURDIR)/$(TEX_CACHE_DIR)
export TEXMFVAR   := $(CURDIR)/$(TEX_CACHE_DIR)

PROBLEMS := ../../../problems/prob_1_examen_2026.tex \
            ../../../problems/prob_2_examen_2026.tex \
            ../../../problems/prob_3_examen_2026.tex

.PHONY: all pdf pdf-with-answers watch watch-answers clean distclean minted-cache tex-cache

all: pdf

pdf: minted-cache tex-cache
	$(LATEXMK) -g $(LATEXMK_FLAGS) $(MAIN).tex

$(MAIN).pdf: $(MAIN).tex preamble.tex $(PROBLEMS) | minted-cache tex-cache
	$(LATEXMK) $(LATEXMK_FLAGS) $(MAIN).tex

pdf-with-answers: minted-cache tex-cache
	$(LATEXMK) -g $(LATEXMK_FLAGS) \
	  -lualatex="lualatex %O '\\def\\WITHANSWERS{1}\\input{%S}'" \
	  $(MAIN).tex

watch-answers: minted-cache tex-cache
	$(LATEXMK) $(LATEXMK_FLAGS) -pvc \
	  -lualatex="lualatex %O '\\def\\WITHANSWERS{1}\\input{%S}'" \
	  $(MAIN).tex

watch: minted-cache tex-cache
	$(LATEXMK) $(LATEXMK_FLAGS) -pvc $(MAIN).tex

tex-cache:
	mkdir -p $(TEX_CACHE_DIR)

minted-cache:
	mkdir -p _minted-$(MAIN)

clean:
	$(LATEXMK) -c $(MAIN).tex
	find . -maxdepth 1 \( -name '*.gz' -o -name '*.fls' \) -delete
	rm -rf _minted-$(MAIN) $(TEX_CACHE_DIR)

distclean: clean
	rm -f $(MAIN).pdf
