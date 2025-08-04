Preferences: Open Settings (JSON) (windows)

    // latex-workshop para que funcione con lualatex y shell-escape
    "latex-workshop.latex.tools": [
        {
            "name": "latexmk-lualatex-shell-escape",
            "command": "latexmk",
            "args": [
                "-lualatex",
                "-shell-escape",
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOC%"
            ]
        }
    ],
    "latex-workshop.latex.recipes": [
        {
            "name": "latexmk lualatex shell-escape",
            "tools": [
                "latexmk-lualatex-shell-escape"
            ]
        }
    ],
    "latex-workshop.latex.recipe.default": "lastUsed"
    // --- Hasta aquí ---
