# Evaluador simple de riesgo basado en Impacto y Probabilidad
# Escalas sugeridas por ISTQB: 1 = bajo, 2 = medio, 3 = alto

funcionalidades = {
    "Login": {"impacto": 3, "probabilidad": 2},
    "Transferencia": {"impacto": 3, "probabilidad": 3},
    "Pagos": {"impacto": 2, "probabilidad": 2},
    "Perfil": {"impacto": 1, "probabilidad": 1},
}


def calcular_riesgo(f: dict) -> int:
    """Riesgo = Impacto x Probabilidad (rango posible: 1 a 9)."""
    return f["impacto"] * f["probabilidad"]


riesgos = {nombre: calcular_riesgo(datos) for nombre, datos in funcionalidades.items()}

for nombre, riesgo in sorted(riesgos.items(), key=lambda x: x[1], reverse=True):
    print(f"{nombre}: Riesgo = {riesgo}")



"""
El código se basa en la priorización de pruebas basada en riesgo, con lo cual el punto no es multiplicar números, sino priorizar las pruebas que más riesgo tienen. Que viene dado por:
 Riesgo = Impacto x Probabilidad (rango posible: 1 a 9).
La conlución, segun la escala de riesgo es que la Transferencia es un punto crítico y viene dado por 9, el máximo posible para un riesgo que se debe tomar en cuenta.
Luego le sigue Login con 6 que es una prioridad alta para tomar en cuenta el riesgo de seguridad.
Las demas son menores desde medio a bajo por lo cual se debe cuidar pero primero priorizar las que más riesgo tienen.
"""