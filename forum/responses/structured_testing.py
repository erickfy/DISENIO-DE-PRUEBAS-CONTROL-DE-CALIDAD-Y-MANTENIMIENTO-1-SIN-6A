def clasificar_riesgo(edad, historial, monto):
    if edad < 25: # step
        if historial == "malo": # step
            return "ALTO"
        else:
            return "MEDIO"
    else:
        if monto > 50000: # step
            return "ALTO"
        elif historial == "excelente": # step
            return "BAJO"
        else:
            return "MEDIO"

    # cc = 4 + 1 = 5
    # Predicates: 4
    # base way = 5 = cc