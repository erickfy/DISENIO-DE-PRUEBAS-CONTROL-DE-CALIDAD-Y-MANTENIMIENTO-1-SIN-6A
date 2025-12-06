def evaluar_cliente(edad, ingresos, deudas, historico_morosidad, productos_activos,
                    antiguedad_cliente, tipo_empleo, region, score_interno):
    """
    Función artificialmente compleja para probar la complejidad ciclomática.
    NO es buen diseño, es a propósito enredada para el ejemplo.
    """
    decision = "RECHAZAR"
    motivo = []

    # Primera capa de reglas generales
    if edad < 18:
        motivo.append("Menor de edad")
    elif edad > 75:
        motivo.append("Edad de alto riesgo")
    else:
        if ingresos < 500:
            motivo.append("Ingresos muy bajos")
        elif 500 <= ingresos < 1500:
            if deudas > ingresos * 0.8:
                motivo.append("Relación deuda/ingresos muy alta")
            elif historico_morosidad > 3:
                motivo.append("Morosidad alta")
            else:
                decision = "REVISAR_MANUAL"
        else:
            if deudas > ingresos:
                motivo.append("Deudas superan ingresos")
            else:
                if historico_morosidad == 0:
                    if productos_activos > 3:
                        decision = "APROBAR"
                    elif productos_activos == 0 and antiguedad_cliente < 1:
                        decision = "REVISAR_MANUAL"
                    else:
                        decision = "APROBAR_CONDICIONADO"
                elif 1 <= historico_morosidad <= 2:
                    if antiguedad_cliente > 5 and score_interno > 750:
                        decision = "APROBAR_CONDICIONADO"
                    else:
                        decision = "REVISAR_MANUAL"
                else:
                    motivo.append("Historial de morosidad preocupante")

    # Reglas por tipo de empleo
    if tipo_empleo == "informal":
        if ingresos < 1000 or historico_morosidad > 0:
            motivo.append("Empleo informal con riesgo")
            if decision == "APROBAR":
                decision = "APROBAR_CONDICIONADO"
        else:
            if decision == "RECHAZAR":
                decision = "REVISAR_MANUAL"
    elif tipo_empleo == "desempleado":
        if productos_activos == 0 or deudas > 0:
            decision = "RECHAZAR"
            motivo.append("Desempleado con deudas o sin historial")
        else:
            decision = "REVISAR_MANUAL"
    else:  # empleo formal
        if antiguedad_cliente > 10 and score_interno > 800 and deudas < ingresos * 0.3:
            if decision != "RECHAZAR":
                decision = "APROBAR"

    # Reglas por región
    if region in ("ALTO_RIESGO_1", "ALTO_RIESGO_2"):
        if decision == "APROBAR":
            decision = "APROBAR_CONDICIONADO"
            motivo.append("Región de alto riesgo")
        elif decision == "REVISAR_MANUAL":
            motivo.append("Revisión adicional por región")
    else:
        if score_interno < 500 and decision == "APROBAR":
            decision = "APROBAR_CONDICIONADO"

    # Ajustes finales por score
    if score_interno < 400:
        decision = "RECHAZAR"
        motivo.append("Score muy bajo")
    elif 400 <= score_interno < 650:
        if decision == "APROBAR":
            decision = "APROBAR_CONDICIONADO"
    elif 650 <= score_interno < 750:
        if decision == "RECHAZAR":
            decision = "REVISAR_MANUAL"

    return {
        "decision": decision,
        "motivo": ", ".join(motivo) if motivo else "Reglas estándar",
        "edad": edad,
        "ingresos": ingresos,
        "deudas": deudas,
        "score": score_interno,
    }