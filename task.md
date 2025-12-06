Radon

La complejidad ciclomática de McCabe es una métrica que mide cuántos caminos lógicamente independientes existen en un bloque de código (por ejemplo, una función o un método). Mientras mayor es la complejidad, más difícil es de entender, probar y mantener ese código.

En la salida del programa se observa que la mayoría de las funciones analizadas tienen complejidades bajas (entre 1 y 7) con rango A o B, lo que indica código relativamente simple y fácil de mantener. Solo la función analyze_complexity alcanza una complejidad de 11 (rango C), lo que sugiere que concentra más decisiones lógicas y sería la principal candidata a refactorización si se quisiera mejorar la mantenibilidad. Los promedios por archivo (entre ~2 y 3.5 en general) también muestran que, en conjunto, el proyecto tiene una complejidad moderada y controlada.

En contraste, la función evaluar_cliente presenta una complejidad ciclomática de 38 (rango E), lo que indica un código con un número muy alto de caminos lógicos posibles. Esto la vuelve difícil de entender, de probar exhaustivamente y de mantener, ya que pequeños cambios pueden afectar muchos flujos distintos de ejecución. En un caso real, una función con este nivel de complejidad sería una candidata clara a refactorización, dividiéndola en funciones más pequeñas y especializadas para reducir el riesgo de errores y hacer más sencilla la evolución del sistema.

Wily
Wily es una herramienta de análisis estático para proyectos Python que:

- complejidad ciclomática (cc)
- métricas de Halstead
- líneas de código (raw)
- índice de mantenibilidad (Maintainability Index, MI)

Permite consultar y ordenar archivos según esas métricas (por ejemplo: “muéstrame los archivos menos mantenibles”).

wily build .
Recorre el directorio (.) y analiza el código, calculando varias métricas por archivo para ser almacena esos datos en un cache para posteriores consultas.

- Los de MI más alto → más “fáciles de mantener”
- Los de MI más bajo → candidatos a refactorizar
