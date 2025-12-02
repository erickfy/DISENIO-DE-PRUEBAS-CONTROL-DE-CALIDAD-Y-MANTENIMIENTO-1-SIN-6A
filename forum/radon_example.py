# forum/radon_example.py

import os
from radon.complexity import cc_visit, cc_rank


def analyze_file(filepath: str):
    """Analiza la complejidad ciclomática de un solo archivo .py"""
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    # cc_visit devuelve una lista de bloques (funciones, métodos, clases)
    blocks = cc_visit(code)

    results = []
    for b in blocks:
        results.append(
            {
                "name": b.name,
                "lineno": b.lineno,
                "complexity": b.complexity,
                "rank": cc_rank(b.complexity),
                # Tipo aproximado para entender qué es el bloque
                "kind": b.__class__.__name__,  # Function o Class
            }
        )
    return results


def analyze_complexity(root_path: str = "."):
    """Recorre recursivamente root_path y calcula complejidad de todos los .py"""
    for dirpath, dirnames, filenames in os.walk(root_path):
        # Opcional: saltar carpetas que no te interesan
        if "__pycache__" in dirpath or ".venv" in dirpath or "env" in dirpath:
            continue

        for filename in filenames:
            if not filename.endswith(".py"):
                continue

            full_path = os.path.join(dirpath, filename)
            print(f"\n=== Archivo: {full_path} ===")

            try:
                results = analyze_file(full_path)
            except Exception as e:
                print(f"  [ERROR] No se pudo analizar este archivo: {e}")
                continue

            if not results:
                print("  (Sin funciones/clases detectadas)")
                continue

            # Mostrar resultados por bloque
            for r in results:
                print(
                    f"  - {r['kind']} '{r['name']}' "
                    f"(línea {r['lineno']}): "
                    f"complejidad = {r['complexity']} "
                    f"(rango {r['rank']})"
                )

            # Pequeño resumen por archivo
            avg = sum(r["complexity"] for r in results) / len(results)
            print(f"  > Complejidad promedio del archivo: {avg:.2f}")


if __name__ == "__main__":
    # Analizar el directorio actual del proyecto
    analyze_complexity(".")