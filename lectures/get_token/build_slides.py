#!/usr/bin/env python3
"""Compila slides LaTeX y gestiona artefactos de compilacion.

Uso rapido:
  python3 build_slides.py
  python3 build_slides.py --tex token_id_usuario.tex
  python3 build_slides.py --delete
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path
from typing import Iterable

ARTIFACT_SUFFIXES = (
    ".aux",
    ".log",
    ".nav",
    ".out",
    ".snm",
    ".toc",
    ".vrb",
    ".fdb_latexmk",
    ".fls",
    ".synctex.gz",
    ".bbl",
    ".blg",
    ".xdv",
)


def list_tex_files(base_dir: Path) -> list[Path]:
    return sorted(base_dir.glob("*.tex"))


def choose_tex_file(base_dir: Path, requested_tex: str | None) -> Path:
    if requested_tex:
        tex_path = (base_dir / requested_tex).resolve()
        if not tex_path.exists() or tex_path.suffix.lower() != ".tex":
            raise SystemExit(f"No existe archivo .tex valido: {requested_tex}")
        return tex_path

    tex_files = list_tex_files(base_dir)
    if not tex_files:
        raise SystemExit(f"No se encontraron .tex en {base_dir}")
    if len(tex_files) == 1:
        return tex_files[0]

    names = ", ".join(file.name for file in tex_files)
    raise SystemExit(f"Hay multiples .tex. Usa --tex. Disponibles: {names}")


def compile_tex(tex_path: Path) -> None:
    base_dir = tex_path.parent
    tex_name = tex_path.name

    if shutil.which("latexmk"):
        cmd = ["latexmk", "-pdf", "-interaction=nonstopmode", tex_name]
    elif shutil.which("pdflatex"):
        cmd = ["pdflatex", "-interaction=nonstopmode", tex_name]
    else:
        raise SystemExit("No se encontro 'latexmk' ni 'pdflatex' en PATH.")

    print(f"Compilando: {tex_name}")
    result = subprocess.run(cmd, cwd=base_dir, capture_output=True, text=True)
    if result.returncode != 0:
        error_log = base_dir / "compile_error.log"
        error_log.write_text(result.stdout + "\n" + result.stderr, encoding="utf-8")
        raise SystemExit(f"Error de compilacion. Revisa {error_log}")

    if cmd[0] == "pdflatex":
        second = subprocess.run(cmd, cwd=base_dir, capture_output=True, text=True)
        if second.returncode != 0:
            error_log = base_dir / "compile_error.log"
            error_log.write_text(
                second.stdout + "\n" + second.stderr, encoding="utf-8"
            )
            raise SystemExit(
                f"Error en segunda pasada de compilacion. Revisa {error_log}"
            )


def is_artifact(path: Path, stem: str) -> bool:
    if path.suffix.lower() == ".pdf":
        return False
    if path.stem != stem:
        return False
    name = path.name.lower()
    return any(name.endswith(suffix) for suffix in ARTIFACT_SUFFIXES)


def iter_artifacts(base_dir: Path, stem: str) -> Iterable[Path]:
    for file_path in sorted(base_dir.iterdir()):
        if file_path.is_file() and is_artifact(file_path, stem):
            yield file_path


def move_artifacts(base_dir: Path, stem: str, log_dir_name: str) -> int:
    log_dir = base_dir / log_dir_name
    log_dir.mkdir(parents=True, exist_ok=True)
    moved = 0

    for file_path in iter_artifacts(base_dir, stem):
        destination = log_dir / file_path.name
        if destination.exists():
            destination.unlink()
        shutil.move(str(file_path), str(destination))
        moved += 1

    return moved


def delete_artifacts(base_dir: Path, stem: str) -> int:
    deleted = 0
    for file_path in iter_artifacts(base_dir, stem):
        file_path.unlink()
        deleted += 1
    return deleted


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compila slides LaTeX y limpia artefactos manteniendo PDFs."
    )
    parser.add_argument(
        "--tex",
        help="Archivo .tex a compilar (default: unico .tex del directorio).",
    )
    parser.add_argument(
        "--delete",
        action="store_true",
        help="Borra artefactos en vez de moverlos a la carpeta log.",
    )
    parser.add_argument(
        "--log-dir",
        default="log",
        help="Nombre de carpeta destino para mover artefactos (default: log).",
    )
    parser.add_argument(
        "--dir",
        default=".",
        help="Directorio de trabajo (default: directorio actual).",
    )
    args = parser.parse_args()

    base_dir = Path(args.dir).resolve()
    if not base_dir.is_dir():
        raise SystemExit(f"Directorio invalido: {base_dir}")

    tex_path = choose_tex_file(base_dir, args.tex)
    compile_tex(tex_path)
    stem = tex_path.stem

    if args.delete:
        count = delete_artifacts(base_dir, stem)
        print(f"Compilacion OK. Eliminados: {count} artefactos en {base_dir}")
        return

    count = move_artifacts(base_dir, stem, args.log_dir)
    print(f"Compilacion OK. Movidos: {count} artefactos a {base_dir / args.log_dir}")


if __name__ == "__main__":
    main()
