import os
import subprocess
import argparse
from tqdm import tqdm

# Lista de subdirectorios
subfolders = [f"Semana{str(i).zfill(2)}" for i in range(1, 16)]

def compile_folder(folder):
    """Ejecuta `make` en un subdirectorio para compilar"""
    log_file = os.path.join(folder, "compilation.log")

    try:
        with open(log_file, "w") as log:
            subprocess.run(["make", "-C", folder], stdout=subprocess.DEVNULL, stderr=log, check=True)
        print(f"✅ {folder} compilado con éxito")
    except subprocess.CalledProcessError:
        print(f"❌ Error en la compilación de {folder}. Revisa {log_file} para más detalles.")

def clean_folder(folder):
    """Ejecuta `make clean` en un subdirectorio"""
    try:
        subprocess.run(["make", "-C", folder, "clean"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print(f"🧹 {folder} limpiado con éxito")
    except subprocess.CalledProcessError:
        print(f"⚠️ Error al limpiar {folder}")

def main():
    parser = argparse.ArgumentParser(description="Compilador de documentos con Makefile en subdirectorios")

    # Opciones disponibles
    parser.add_argument("--all", action="store_true", help="Compilar todos los subdirectorios")
    parser.add_argument("--clean", action="store_true", help="Limpiar archivos generados")
    parser.add_argument("--only", type=str, help="Compilar o limpiar solo un subdirectorio específico (Ej: Semana03)")

    args = parser.parse_args()

    if args.only:
        # Ejecutar en un solo subdirectorio
        if args.only in subfolders:
            if args.clean:
                clean_folder(args.only)
            else:
                compile_folder(args.only)
        else:
            print(f"⚠️ Error: {args.only} no es un subdirectorio válido.")
    elif args.all:
        # Compilar todos los subdirectorios
        with tqdm(total=len(subfolders), desc="Compilando", unit="folder") as pbar:
            for folder in subfolders:
                compile_folder(folder)
                pbar.update(1)
    elif args.clean:
        # Limpiar todos los subdirectorios
        with tqdm(total=len(subfolders), desc="Limpiando", unit="folder") as pbar:
            for folder in subfolders:
                clean_folder(folder)
                #pbar.update(1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

