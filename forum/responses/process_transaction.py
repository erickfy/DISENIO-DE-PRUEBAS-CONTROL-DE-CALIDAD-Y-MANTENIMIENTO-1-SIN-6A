
# cc = 3 + 1 = 4
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

# cc = 3 + 1 = 4
def procesar_transaccion_refactored(monto, tipo, usuario):
    comision = 0.02
    total = monto

    # Si es internacional, solo cambiamos la comisión
    if tipo == "internacional":
        comision = 0.03

    # Acceso seguro a usuario.es_premium (si no existe, asumimos False)
    es_premium = getattr(usuario, "es_premium", False)

    # Solo los usuarios premium pagan con comisión aplicada
    if es_premium:
        total = monto * (1 - comision)

    # Nos aseguramos de definir 'resultado' en todos los caminos, porque ahora permite 'Rechazada'
    if total > 0:
        resultado = "Aprobada"
    else:
        resultado = "Rechazada"

    return resultado