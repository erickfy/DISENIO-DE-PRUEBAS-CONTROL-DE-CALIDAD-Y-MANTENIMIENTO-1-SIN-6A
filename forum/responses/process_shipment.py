def procesar_pedido(cantidad, es_miembro, tiene_descuento):
    total = cantidad * 10 # 10 represent unit
    
    if es_miembro:
        total *= 0.9
    
    if tiene_descuento:
        total *= 0.95
    
    return total