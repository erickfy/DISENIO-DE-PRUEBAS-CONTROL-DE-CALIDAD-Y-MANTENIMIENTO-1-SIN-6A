def calcular_tarifa_original(edad, es_estudiante, es_senior, dia_semana, hora):
    tarifa = 10
    
    if edad < 12: # 1 step
        tarifa = 5
    elif edad >= 65: # 1 step
        tarifa = 6
    
    if es_estudiante: # 1 step
        tarifa *= 0.8
    
    if es_senior: # 1 step
        tarifa *= 0.7
    
    if dia_semana in ["sabado", "domingo"]: # 2 step if+in
        tarifa *= 1.5
    
    if hora >= 18: # 1 step
        tarifa *= 1.2
    
    return tarifa
    # Decision steps 7

"""
REFACTORIZED FUNCTION BY METHODS IN ORDER TO REDUCE CC TO 3 STEPS
"""
# MODULE 1
def refacto_tarifa_base_por_edad(edad):
    if edad < 12:
        return 5
    elif edad >= 65:
        return 6
    return 10

# MODULE 2
def refacto_aplicar_descuentos(tarifa, es_estudiante, es_senior):
    if es_estudiante:
        tarifa *= 0.8
    if es_senior:
        tarifa *= 0.7
    return tarifa

# MODULE 3
def refacto_aplicar_recargos(tarifa, dia_semana, hora):
    if dia_semana in ("sabado", "domingo"):
        tarifa *= 1.5
    if hora >= 18:
        tarifa *= 1.2
    return tarifa

# FINAL REFACTO FUNCTION
def refacto_calcular_tarifa(edad, es_estudiante, es_senior, dia_semana, hora):
    # CC = 3 STEPS
    tarifa = refacto_tarifa_base_por_edad(edad)
    tarifa = refacto_aplicar_descuentos(tarifa, es_estudiante, es_senior)
    tarifa = refacto_aplicar_recargos(tarifa, dia_semana, hora)
    return tarifa