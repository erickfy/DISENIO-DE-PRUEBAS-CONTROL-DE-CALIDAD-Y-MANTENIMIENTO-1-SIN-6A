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

wily report <file> [METRICS]...
Este comando permite sacar las metricas (cyclomatica, operadores unicos, índice de mantenibilidad y Lineas de código) de un archivo en particular en todos los commits del repositorio, por tal razón algunos commits aparece como 'Not found' ya que no se encontraba creado el archivo.

Para finalizar, al analizar el archivo 'cc_high.py', se observa que es un archivo pequeño/mediano (93 líneas) pero con complejidad muy alta (CC=38) y un índice de mantenibilidad medio-bajo (MI≈52), así que es un claro candidato a refactorización.

EJERCICIOS

1. Proceso de Pedido

1 Existen 2 predicados o condiciones lógicas
2: Existen 2 condiciones lógicas + 1 = 3
3: Número de caminos base = complejidad ciclomática. Por lo tanto, 3.
4: Mínimo de pruebas segun cc es 3 pero las combinaciones con 2 condiciones son 2^2=4

2. Autorizar Prestamo

Se tiene 3 condiciones lógicas:

- A: edad >= 18
- B: ingreso >= 2000
- C: historial_crediticio == "bueno"

Necesitamos todas las combinaciones posibles de A, B, C → 2³ = 8 casos.

3. Refactorización

1: En la función calcular_tarifa_original la complejidad ciclomática es 7, debido al sumar 1 por el flujo base y 1 por cada decisión: el if edad < 12, el elif edad >= 65, los if de es_estudiante, es_senior, dia_semana in ["sabado", "domingo"] y hora >= 18. En total hay 6 decisiones, por lo que la complejidad ciclomática es 6 + 1 = 7.

2: Para reducir la complejidad, se refactorizó la lógica en tres funciones auxiliares:

- refacto_tarifa_base_por_edad(edad) se encarga solo de decidir la tarifa base según la edad (niño, senior o tarifa general).
- refacto_aplicar_descuentos(tarifa, es_estudiante, es_senior) aplica únicamente los descuentos correspondientes.
- refacto_aplicar_recargos(tarifa, dia_semana, hora) aplica únicamente los recargos por fin de semana y por horario nocturno.

Para poder orquestar en refacto_calcular_tarifa las tres etapas, encadenando las llamadas. De esta forma, cada función tiene una complejidad ciclomática pequeña (CC=3 en las auxiliares y CC=1 en la función principal) y todas quedan por debajo del umbral solicitado de CC ≤ 5.

3: La prueba parametrizada test_calcular_tarifa_equivalente ejecuta calcular_tarifa_original y refacto_calcular_tarifa con varios conjuntos de datos (niño, adulto, senior, con y sin descuentos, días normales y fin de semana, distintas horas) y verifica que ambos devuelven el mismo resultado, tolerando pequeños errores de coma flotante con round/approx.

Además, se añadieron casos concretos en test_tarifa_casos_concretos para documentar explícitamente comportamientos clave (por ejemplo: niño sin recargos, adulto sin descuentos, senior con descuento, adulto estudiante en domingo por la noche). Con estos tests se demuestra que la versión refactorizada es equivalente a la original.

4. Obtener Impuestos

1: Variables:

- salario
- dependientes
- es_jubilado
- impuesto_base
- descuento
- impuesto_final

salario:
DEF: parametro
C-USE:
• En impuesto*base = salario * 0.15
• En descuento += salario \_ 0.05
P-USE: ninguna (no se usa en un if).

dependientes:
DEF: parametro
C-USE:
• En descuento = dependientes \* 500
P-USE:
• En if dependientes > 0: (se usa en la condición).

es_jubilado:
DEF: parametro
C-USE: ninguna

    P-USE:
    •	En if es_jubilado:

impuesto_base
• DEF: impuesto_base = salario \* 0.15
• C-USE:
• En impuesto_final = impuesto_base - descuento
• P-USE: ninguna.

descuento:
DEF:
• descuento = 0
• descuento = dependientes _ 500
• descuento += salario _ 0.05 (esta línea usa y vuelve a definir).
C-USE:
• En descuento += salario \* 0.05 (usa el valor previo de descuento)
• En impuesto_final = impuesto_base - descuento
P-USE: ninguna.

impuesto_final
DEF: impuesto_final = impuesto_base - descuento
C-USE:
• En return max(0, impuesto_final)
P-USE: ninguna.

2: Un camino DU (Def–Use) es la secuencia de ejecución que va desde una definición de una variable hasta un uso de esa misma variable (ya sea en un cálculo –C-USE– o en una condición –P-USE–) sin que esa variable vuelva a redefinirse entre medio. Por ejemplo:
Caso: dependientes = 0, es_jubilado = False

- DEF: descuento = 0
- No entra al if dependientes > 0
- No entra al if es_jubilado
- USE (C-USE): impuesto_final = impuesto_base - descuento

https://www.geeksforgeeks.org/software-testing/data-flow-testing/

3: Según el cc existe 2² = 8 casos. Por lo tanto, se tiene:

4: Se tiene los siguientes puntos:

- No hay usos sin definición previa.
- Todas las definiciones de 'descuento' pueden llegar a un uso en algún camino.
- 'impuesto_final' siempre se define antes de ser usado en return.
  Por lo tanto de conclusión, no se han detectado anomalías de flujo de datos en esta función.

5. Prueba estructurada
   1: cc = # decisiones 4 + 1 = 5
   2: Predicados o condiciones logicas = 4
   3: caminos base o caminos especificos a cubrir = 5 = cc
   4: cc = 5 = pruebas minimas

6: Procesar Transacción
1:

- Observación: variable no usada, afectando a la mantenibilidad del código.
  Código: recargo = monto \* 0.05
- Observación: posible acceso al atributo inexistente. Por lo tanto, puede lanzar un AttributeError:
  https://realpython.com/ref/builtin-exceptions/attributeerror/
  Código: if usuario.es_premium:
- Observación: posible uso sin definición
  Código: if total > 0:

2:

- Quitar variable no usada
- Definir fallback para acceso inseguro de es_premium
- asegurar que la variable 'resultado' siempre se defina correctamente

3 y 4:

- No hay variable muerta (recargo eliminado).
- No revienta si el usuario no tiene .es_premium.
- resultado siempre está definido (caso aprobado y rechazado).
