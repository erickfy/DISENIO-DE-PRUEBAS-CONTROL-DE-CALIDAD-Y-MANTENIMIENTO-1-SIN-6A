1. Implementar el cálculo de la complejidad ciclomática de McCabe usando la librería https://github.com/rubik/radonEnlaces a un sitio externo. en un código de python de libre elección

2. Implementar el cálculo del índice de mantenibilidad usando la librería https://github.com/tonybaloney/wilyEnlaces a un sitio externo. en un código de python de libre elección y explicar brevemente como realiza la librería este cálculo

3. EJERCICIOS

Ejercicio 1: Análisis Básico ⭐
Objetivo: Calcular la complejidad ciclomática manualmente

def procesar_pedido(cantidad, es_miembro, tiene_descuento):
total = cantidad \* 10

    if es_miembro:
        total *= 0.9

    if tiene_descuento:
        total *= 0.95

    return total

Preguntas:

¿Cuántos predicados de prueba tiene?
¿Cuál es la complejidad ciclomática?
¿Cuántos caminos base necesitas probar?
Escribe los casos de prueba para 100% de cobertura de ramas
Ejercicio 2: Cobertura de Condiciones ⭐⭐
Objetivo: Diseñar casos de prueba para cobertura de condición múltiple

def autorizar_prestamo(edad, ingreso, historial_crediticio):
if edad >= 18 and ingreso >= 2000 and historial_crediticio == "bueno":
return "APROBADO"
return "RECHAZADO"
Tarea: Crea una matriz de pruebas con todas las combinaciones posibles (2³ = 8 casos)

Ejercicio 3: Refactorización ⭐⭐⭐
Objetivo: Reducir complejidad ciclomática

def calcular_tarifa(edad, es_estudiante, es_senior, dia_semana, hora):
tarifa = 10

    if edad < 12:
        tarifa = 5
    elif edad >= 65:
        tarifa = 6

    if es_estudiante:
        tarifa *= 0.8

    if es_senior:
        tarifa *= 0.7

    if dia_semana in ["sabado", "domingo"]:
        tarifa *= 1.5

    if hora >= 18:
        tarifa *= 1.2

    return tarifa

Tarea:

Calcula la CC actual
Refactoriza para reducir CC a ≤ 5
Mantén la funcionalidad idéntica
Escribe tests que demuestren equivalencia 4) EJERCICIOS

Ejercicio 1: Identificar Caminos DU ⭐
def calcular_impuesto(salario, dependientes, es_jubilado):
impuesto_base = salario \* 0.15
descuento = 0

    if dependientes > 0:
        descuento = dependientes * 500

    if es_jubilado:
        descuento += salario * 0.05

    impuesto_final = impuesto_base - descuento
    return max(0, impuesto_final)

Tareas:

Identificar todas las variables y sus DEF, C-USE, P-USE
Listar todos los caminos DU
Diseñar casos de prueba para cobertura All-Uses
¿Hay alguna anomalía?
Ejercicio 2: Testing Estructurado ⭐⭐
def clasificar_riesgo(edad, historial, monto):
if edad < 25:
if historial == "malo":
return "ALTO"
else:
return "MEDIO"
else:
if monto > 50000:
return "ALTO"
elif historial == "excelente":
return "BAJO"
else:
return "MEDIO"
Tareas:

Calcular CC
Identificar predicados
Generar caminos base sistemáticamente
Crear casos de prueba para cada camino base
Ejercicio 3: Detectar y Corregir Anomalías ⭐⭐⭐
def procesar_transaccion(monto, tipo, usuario):
comision = 0.02
total = monto

    if tipo == "internacional":
        recargo = monto * 0.05  # ❌ Definida pero no usada
        comision = 0.03

    if usuario.es_premium:  # ❌ usuario puede no tener .es_premium
        total = monto * (1 - comision)

    # ❌ 'resultado' no está definida en todos los caminos
    if total > 0:
        resultado = "Aprobada"

    return resultado

Tareas:

Identificar todas las anomalías
Clasificar cada anomalía (var no usada, var no definida, etc.)
Proponer correcciones
Escribir versión corregida con tests
