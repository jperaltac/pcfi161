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
    parser.add_argument("--semana", type=int, default=None, help="Semana a subir (1-16).")
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
    parser.add_argument(
        "--eliminar-semana",
        type=int,
        default=None,
        help="Elimina esta semana del módulo. Puede usarse sola o junto a --semana. "
             "Ej: --eliminar-semana 13 --semana 12.",
    )

    args = parser.parse_args()

    if args.semana is None and args.eliminar_semana is None:
        parser.error("Debes indicar --semana, --eliminar-semana, o ambos.")

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
    if args.semana is not None and args.eliminar_semana is not None:
        print("🗑️📤 ELIMINACIÓN Y SUBIDA MASIVA DE SEMANA")
    elif args.semana is not None:
        print("📤 SUBIDA MASIVA DE SEMANA")
    else:
        print("🗑️ ELIMINACIÓN MASIVA DE SEMANA")
    if args.semana is not None:
        print(f"Semana a subir: {args.semana}")
    if args.eliminar_semana is not None:
        print(f"Semana a eliminar: {args.eliminar_semana}")
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

        if args.eliminar_semana is not None:
            eliminado = ck.eliminar_semana(
                args.eliminar_semana,
                test_mode=args.test_mode,
            )
            if eliminado is None:
                errores.append((usuario, f"Fallo en eliminar_semana({args.eliminar_semana})"))
                continue

        if args.semana is not None:
            resultado = ck.subir_contenido(args.semana, test_mode=args.test_mode)
            if resultado is None:
                errores.append((usuario, "Fallo en subir_contenido"))
            else:
                exitos.append(usuario)
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
