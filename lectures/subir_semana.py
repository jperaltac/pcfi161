#!/usr/bin/env python3
import argparse
import sys

import Canvas_Key as ck


def _usuarios_disponibles():
    return sorted([k for k in ck.USERS.keys() if not k.endswith("_id")])


def _parsear_usuarios(raw, disponibles):
    if not raw:
        return disponibles
    pedidos = [u.strip() for u in raw.split(",") if u.strip()]
    return pedidos


def main():
    parser = argparse.ArgumentParser(
        description="Sube una semana a Canvas para múltiples usuarios."
    )
    parser.add_argument("--semana", type=int, required=True, help="Semana a subir (1-15).")
    parser.add_argument(
        "--usuarios",
        type=str,
        default="",
        help="Lista separada por coma. Ej: David,Fabrizzio,Joaquin. "
             "Si se omite, usa todos los usuarios del Key.txt.",
    )
    parser.add_argument(
        "--test-mode",
        action="store_true",
        help="Sube en modo test (no publica).",
    )

    args = parser.parse_args()

    disponibles = _usuarios_disponibles()
    if not disponibles:
        print("❌ No hay usuarios configurados en Key.txt")
        return 1

    usuarios = _parsear_usuarios(args.usuarios, disponibles)
    desconocidos = [u for u in usuarios if u not in disponibles]
    if desconocidos:
        print(f"❌ Usuarios no encontrados en Key.txt: {', '.join(desconocidos)}")
        print(f"💡 Disponibles: {', '.join(disponibles)}")
        return 1

    print("=" * 80)
    print("📤 SUBIDA MASIVA DE SEMANA")
    print(f"Semana: {args.semana}")
    print(f"Usuarios: {', '.join(usuarios)}")
    print(f"Modo: {'TEST (no publica)' if args.test_mode else 'PRODUCCIÓN (publica)'}")
    print("=" * 80)

    errores = []
    exitos = []

    for usuario in usuarios:
        print(f"\n--- Usuario: {usuario} ---")

        if not ck.select_user(usuario):
            errores.append((usuario, "No se pudo conectar"))
            continue

        resultado = ck.subir_contenido(args.semana, test_mode=args.test_mode)
        if resultado is None:
            errores.append((usuario, "Fallo en subir_contenido"))
        else:
            exitos.append(usuario)

    print("\n" + "=" * 80)
    print("RESUMEN")
    print(f"✅ Exitosos: {len(exitos)}")
    if exitos:
        print(f"   {', '.join(exitos)}")
    print(f"❌ Con error: {len(errores)}")
    for usuario, motivo in errores:
        print(f"   - {usuario}: {motivo}")
    print("=" * 80)

    return 0 if not errores else 1


if __name__ == "__main__":
    raise SystemExit(main())
