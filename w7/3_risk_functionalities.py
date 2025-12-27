import pandas as pd

casos = pd.DataFrame([
    ["TC01", "Transferencia válida", 3, 3],
    ["TC02", "Transferencia sin saldo", 3, 2],
    ["TC03", "Login con credenciales válidas", 3, 2],
    ["TC04", "Login incorrecto", 2, 2],
    ["TC05", "Pago básico", 2, 2],
    ["TC06", "Actualizar perfil", 1, 1],
], columns=["ID", "Descripción", "Impacto", "Probabilidad"])

casos["Riesgo"] = casos["Impacto"] * casos["Probabilidad"]

print(casos.sort_values("Riesgo", ascending=False))


"""
Se presenta una matriz de pruebas basado en riesgo, por lo cual el caso práctivo y medible es enfocarse en las pruebas que más riesgo tienen.
Por lo cual, se puede concluir que la Transferencia válida tiene el puntaje mas alto para el riesgo y por lo tanto es la más crítica. Por otro lado, la 'Transferencia sin saldo' y 'Login con credenciales válidas' es otra fuente de riesgo alto, por lo que se tiene que observar y priorizar este caso.
Para concluir, las demás tienen su riesgo moderado a bajo pero no son críticas.
"""