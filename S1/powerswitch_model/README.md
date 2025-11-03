# Demo PyModel en Codespaces

Este repositorio demuestra PyModel (https://github.com/zlorb/PyModel) corriendo en GitHub Codespaces.

## ¿Qué es PyModel?

PyModel es un framework de *model-based testing* (pruebas basadas en modelos).  
En lugar de escribir casos de prueba manualmente, defines el comportamiento esperado del sistema como un **modelo**: estado interno, acciones permitidas y reglas de cuándo se pueden ejecutar.  
Luego PyModel genera y ejecuta automáticamente secuencias de acciones válidas y verifica si el sistema termina en un estado correcto.

Nosotros usamos el ejecutor de pruebas de PyModel (`pmt`) para correr el modelo y validar su comportamiento.

## ¿Qué hay en este repo?

- `S1/powerswitch_model/PowerSwitch.py`  
  Modelo del sistema. Representa un interruptor con estado `power` (encendido/apagado), acciones `PowerOn()` y `PowerOff()`, restricciones de uso (no puedes apagar si ya está apagado, etc.) y una función `Accepting()` que dice si el estado final es válido.  
  En este caso, el estado válido es quedar apagado.

- `S1/powerswitch_model/test.py`  
  Script que ejecuta varios escenarios de prueba usando PyModel (`pmt`).  
  Este script:
  - llama a `pmt` con distintas configuraciones (normal, solo PowerOn, prohibir PowerOff, múltiples corridas, etc.),
  - prepara el entorno para que `pmt` pueda importar `PowerSwitch.py`,
  - y aplica una compatibilidad para Python 3.12 (porque PyModel fue escrito para versiones antiguas de Python y usa `inspect.getargspec`).

  Al final imprime la salida de cada corrida de prueba.

- `.devcontainer/devcontainer.json`  
  Configuración de Codespaces.  
  Usa una imagen con Python 3.12, instala PyModel desde `zlorb/PyModel` y deja listo el entorno automáticamente dentro del contenedor.

- `requirements.txt`  
  Dependencias del proyecto (incluye PyModel y graphviz).

## ¿Cómo ejecutarlo en Codespaces?

Dentro del Codespace:

```bash
cd S1/powerswitch_model
python test.py