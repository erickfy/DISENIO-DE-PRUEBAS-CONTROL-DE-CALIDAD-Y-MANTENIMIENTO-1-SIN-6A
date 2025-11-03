import os
import copy
import subprocess
import shlex
import textwrap

# DEFINICIÓN DE LOS CASOS DE PRUEBA
# Cada item es: (descripcion, comando_a_ejecutar)
CASES = [
    (
        "PowerOn / PowerOff alternan por las condiciones de habilitación",
        "pmt -n 10 PowerSwitch"
    ),
    (
        "Solo permitimos PowerOn (-a PowerOn), así que solo puede encender una vez",
        "pmt -n 10 -a PowerOn PowerSwitch"
    ),
    (
        "Excluimos PowerOff (-e PowerOff), entonces no puede apagarse",
        "pmt -n 10 -e PowerOff PowerSwitch"
    ),
    (
        "Ejecutar varias corridas (-r 2) con limpieza entre corridas (-c)",
        "pmt -n 3 -c 3 -r 2 PowerSwitch"
    )
]


def run_case(desc: str, cmd: str, workdir: str):
    """
    Ejecuta UNA corrida de PyModel con parche de compatibilidad
    contra Python 3.12.
    """
    print()
    print("=== CASO:", desc, "===")

    # Ejemplo de cmd: "pmt -n 10 -a PowerOn PowerSwitch"
    # Lo convertimos en lista tipo argv: ["pmt","-n","10","-a","PowerOn","PowerSwitch"]
    argv = shlex.split(cmd)

    # Script que va a correr en un proceso Python hijo:
    # 1. Parchea inspect.getargspec si no existe (En python 3.12 no existe debido a que usamos un .venv)
    # 2. Setea sys.argv con los args de pmt
    # 3. Llama pymodel.pmt.main()
    child_script = textwrap.dedent(f"""
        import sys, inspect

        # parche retrocompatibilidad para PyModel en Python 3.12+
        if not hasattr(inspect, "getargspec"):
            from inspect import getfullargspec
            from collections import namedtuple
            ArgSpec = namedtuple("ArgSpec", "args varargs keywords defaults")
            def getargspec(func):
                fas = getfullargspec(func)
                return ArgSpec(fas.args, fas.varargs, fas.varkw, fas.defaults)
            inspect.getargspec = getargspec  # monkeypatch

        import pymodel.pmt

        # simular que se llamó por CLI:
        sys.argv = {argv!r}

        # ejecutar PyModel Tester
        pymodel.pmt.main()
    """)

    # Tenemos que asegurarnos de que el hijo pueda importar PowerSwitch.
    # Para eso, le pasamos PYTHONPATH apuntando a la carpeta con PowerSwitch.py
    env = copy.deepcopy(os.environ)
    here = workdir
    old_pp = env.get("PYTHONPATH", "")
    if old_pp:
        env["PYTHONPATH"] = here + os.pathsep + old_pp
    else:
        env["PYTHONPATH"] = here

    # Lanzamos un Python hijo que ejecuta el script anterior
    result = subprocess.run(
        ["python", "-c", child_script],
        cwd=workdir,
        text=True,
        env=env
    )

    if result.returncode != 0:
        print(f"[ERROR] Caso falló (returncode {result.returncode})")


def main():
    # workdir = carpeta donde vive PowerSwitch.py
    workdir = os.path.dirname(os.path.abspath(__file__))

    for desc, cmd in CASES:
        run_case(desc, cmd, workdir)


if __name__ == "__main__":
    main()