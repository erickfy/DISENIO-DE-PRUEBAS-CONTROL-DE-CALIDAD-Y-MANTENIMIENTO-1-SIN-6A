import subprocess
import sys
from pathlib import Path


def run(cmd: list[str]) -> None:
    """Ejecuta un comando y lo muestra en pantalla."""
    print(f"$ {' '.join(cmd)}")
    result = subprocess.run(cmd, text=True)
    if result.returncode != 0:
        print(f"[ERROR] El comando falló con código {result.returncode}")
        sys.exit(result.returncode)


def main() -> None:
    # Carpeta a analizar: por defecto el directorio actual (.)
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    target = str(Path(target))

    # 1) Construir el caché de métricas de wily (usa git + historial)
    run(["wily", "build", target])

    # 2) Mostrar ranking por índice de mantenibilidad (maintainability.mi)
    #    maintainability.mi = Maintainability Index que calcula wily 
    run(["wily", "rank", target, "maintainability.mi"])


if __name__ == "__main__":
    main()