import subprocess
import sys
from pathlib import Path

# Raíz del proyecto (un nivel por encima de /forum)
PROJECT_ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str]) -> None:
    """Ejecuta un comando wily desde la raíz del proyecto."""
    print(f"$ {' '.join(cmd)}  (cwd={PROJECT_ROOT})")
    result = subprocess.run(cmd, text=True, cwd=PROJECT_ROOT)
    if result.returncode != 0:
        print(f"[ERROR] El comando falló con código {result.returncode}")
        sys.exit(result.returncode)


def main() -> None:
    # Vamos a analizar siempre la carpeta 'forum'
    target = "forum"

    # 1) Construir el caché de métricas de wily sobre 'forum'
    run(["wily", "build", target])

    # 2) Ranking por índice de mantenibilidad (Maintainability Index)
    run(["wily", "rank", target, "maintainability.mi"])

    # 3) Reporte detallado del archivo de alta complejidad
    # run(["wily", "report", "forum/experiments/cc_high.py"])
    run(["wily", "report"])


if __name__ == "__main__":
    main()