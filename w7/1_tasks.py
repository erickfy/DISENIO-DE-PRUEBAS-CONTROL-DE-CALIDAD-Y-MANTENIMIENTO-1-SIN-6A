# Estimación de esfuerzo bottom-up para testing

tareas = {
    "Analizar requisitos": 4,
    "Diseño de casos de prueba": 8,
    "Configurar entorno": 4,
    "Preparar datos de prueba": 3,
    "Ejecución de pruebas": 12,
    "Pruebas exploratorias": 6,
    "Reporte y gestión de defectos": 6,
    "Re-ejecución": 4,
}

total_horas = sum(tareas.values())

print("ESTIMACIÓN DE ESFUERZO\n")

for tarea, horas in tareas.items():
    print(f"{tarea}: {horas} horas")

print(f"\nTotal estimado: {total_horas} horas")

# 
"""
Se define un diccionario para estimar las horas de cada tarea y que además suma el total de horas.
También se da entender que el flujo que buena cantidad de horas ha sido dedicado a desarrollar las pruebas que van casi a la par que el diseñño de casos de prueba.
También algo que podria aumentarse a las tareas es añadir pruebas de regresión y riesgos.
"""
