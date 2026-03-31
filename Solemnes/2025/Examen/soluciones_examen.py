"""
Pregunta 1: Ecuación Cúbica
Resolver ax^3 + bx^2 + cx + d = 0
"""

import numpy as np

# 1. Entrada de datos
print("Resolución de ecuación cúbica: ax³ + bx² + cx + d = 0")
print("-" * 50)

a = float(input("Ingrese coeficiente a: "))
b = float(input("Ingrese coeficiente b: "))
c = float(input("Ingrese coeficiente c: "))

# Generar d al azar
d = np.random.randint(-20, 21)
print(f"\nCoeficiente d generado al azar: {d}")

# 2. Cálculo de las raíces
coeficientes = [a, b, c, d]
raices = np.roots(coeficientes)

# Filtrar raíces reales
raices_reales = []
for raiz in raices:
    if abs(raiz.imag) < 1e-10:
        raices_reales.append(raiz.real)

# 3. Clasificación y presentación
num_raices = len(raices_reales)

print("\n" + "=" * 50)
if num_raices == 0:
    print("No hay raíces reales")
elif num_raices == 1:
    print("Hay 1 raíz real:")
    print(f"  x = {raices_reales[0]:.4f}")
elif num_raices == 2:
    print("Hay 2 raíces reales:")
    for i, raiz in enumerate(raices_reales, 1):
        print(f"  x{i} = {raiz:.4f}")
else:  # num_raices == 3
    print("Hay 3 raíces reales:")
    for i, raiz in enumerate(raices_reales, 1):
        print(f"  x{i} = {raiz:.4f}")

print("=" * 50)
# ==============================================================================
# PREGUNTA 2: Espiral de Arquímedes
# ==============================================================================

print("\n" + "=" * 60)
print("PREGUNTA 2: Espiral de Arquímedes")
print("=" * 60)

# Parámetros
a = 0.5
b = 0.3

# Crear arreglo theta
theta = np.linspace(0, 6*np.pi, 1000)

# Calcular radio
r = a + b * theta

# Coordenadas cartesianas
x = r * np.cos(theta)
y = r * np.sin(theta)

# Graficar
plt.figure(figsize=(8, 8))
plt.plot(x, y, 'b-', linewidth=1)
plt.axis('equal')
plt.grid(True, alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Espiral de Arquímedes')
plt.tight_layout()
plt.savefig('espiral_arquimedes.png', dpi=150)
print("\nGráfico guardado como 'espiral_arquimedes.png'")

# Calcular radios máximo y mínimo
r_max = np.max(r)
r_min = np.min(r)
print(f"\nRadio mínimo: {r_min:.4f}")
print(f"Radio máximo: {r_max:.4f}")

# ==============================================================================
# PREGUNTA 3: Crecimiento Bacteriano (curve_fit)
# ==============================================================================

print("\n" + "=" * 60)
print("PREGUNTA 3: Crecimiento Bacteriano")
print("=" * 60)

# Generar datos sintéticos
np.random.seed(42)
t_crecimiento = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
P0_real = 1000
k_real = 0.25

P_teorico = P0_real * np.exp(k_real * t_crecimiento)
sigma_P = 50 + 0.03 * P_teorico
P_obs = P_teorico + np.random.normal(0, sigma_P)

print("\nDatos generados.")
plt.figure(figsize=(10, 6))
plt.scatter(t_crecimiento, P_obs, label='Datos observados', color='red', zorder=3)
plt.xlabel('Tiempo (horas)')
plt.ylabel('Población')
plt.title('Datos de Crecimiento Bacteriano')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('datos_crecimiento.png', dpi=150)
print("Gráfico de datos guardado como 'datos_crecimiento.png'")

# 1. Definir modelo
def modelo_crecimiento(t, P0, k):
    return P0 * np.exp(k * t)

# 2. Ajuste con curve_fit
p0 = [800, 0.2]
popt, pcov = curve_fit(modelo_crecimiento, t_crecimiento, P_obs, 
                       p0=p0, sigma=sigma_P, absolute_sigma=True)

P0_fit = popt[0]
k_fit = popt[1]
P_fit = modelo_crecimiento(t_crecimiento, P0_fit, k_fit)

# 3. Incertidumbres
perr = np.sqrt(np.diag(pcov))
sigma_P0 = perr[0]
sigma_k = perr[1]

print(f"\nParámetros ajustados:")
print(f"P0 = {P0_fit:.4f} ± {sigma_P0:.4f}")
print(f"k = {k_fit:.4f} ± {sigma_k:.4f}")

# 4. Chi cuadrado reducido
residuos = (P_obs - P_fit) / sigma_P
chi2 = np.sum(residuos**2)
nu = len(t_crecimiento) - 2
chi2_red = chi2 / nu

print(f"\nEstadísticos de bondad de ajuste:")
print(f"χ² = {chi2:.4f}")
print(f"ν = {nu}")
print(f"χ²_red = {chi2_red:.4f}")

# 5. Visualización con barras de error
plt.figure(figsize=(10, 6))
plt.errorbar(t_crecimiento, P_obs, yerr=sigma_P, fmt='o', 
             label='Datos observados', color='red', capsize=5)

t_fino = np.linspace(0, 9, 200)
P_fino = modelo_crecimiento(t_fino, P0_fit, k_fit)
plt.plot(t_fino, P_fino, 'b-', linewidth=2, 
         label=f'Ajuste: $P_0 = {P0_fit:.1f} \\pm {sigma_P0:.1f}$, $k = {k_fit:.3f} \\pm {sigma_k:.3f}$')

plt.xlabel('Tiempo (horas)', fontsize=12)
plt.ylabel('Población de bacterias', fontsize=12)
plt.title('Ajuste de Crecimiento Bacteriano', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('ajuste_crecimiento.png', dpi=150)
print("\nGráfico de ajuste guardado como 'ajuste_crecimiento.png'")

print("\n" + "=" * 60)
print("TODAS LAS PREGUNTAS COMPLETADAS")
print("=" * 60)
