# Demo PyModel en Codespaces

Este repo demuestra PyModel (https://github.com/zlorb/PyModel) corriendo en GitHub Codespaces.

## ¿Qué es PyModel?

PyModel es un framework de *model-based testing* en Python: defines un modelo del sistema (estados, acciones permitidas, etc.)
y PyModel genera y ejecuta pruebas automáticamente con el comando `pmt` y las orquesta con `trun`.  
Incluye soporte para elegir acciones habilitadas, limpiar el estado, y reportar si el sistema termina en un estado aceptable.

## ¿Qué hay aquí?

- `S1/PowerSwitch.py`: el modelo de un interruptor ON/OFF.
- `S1/test.py`: casos de prueba que llaman a `pmt`.
- `.devcontainer/devcontainer.json`: configuración para que Codespaces instale PyModel automáticamente.
- `requirements.txt`: dependencias.


## Verificación y ejecución
```bash
# 1. Verifica que PyModel está instalado
pmt --help

# 2. Corre los tests del modelo PowerSwitch usando trun
cd S1/powerswitch_model
python test.py
```