import os
import subprocess
from tqdm import tqdm

# Lista de subdirectorios
subfolders = [f"Semana{str(i).zfill(2)}" for i in range(1, 6)]

# Progreso visual con tqdm
with tqdm(total=len(subfolders), desc="Compilando", unit="folder") as pbar:
    for folder in subfolders:
        print(f"\n📦 Compilando {folder}...\n")
        log_file = os.path.join(folder, "compilation.log")

        try:
            # Ejecutar make dentro del subdirectorio, silenciando stdout pero guardando stderr en un log
            with open(log_file, "w") as log:
                subprocess.run(["make", "-C", folder], stdout=subprocess.DEVNULL, stderr=log, check=True)

            print(f"✅ {folder} compilado con éxito\n")
        except subprocess.CalledProcessError:
            print(f"❌ Error en la compilación de {folder}. Revisa {log_file} para más detalles.\n")

        pbar.update(1)  # Actualizar la barra de progreso
