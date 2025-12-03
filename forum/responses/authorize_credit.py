def autorizar_prestamo(edad, ingreso, historial_crediticio):
    if edad >= 18 and ingreso >= 2000 and historial_crediticio == "bueno":
        return "APROBADO"
    return "RECHAZADO"


print(autorizar_prestamo(17, 1500, "malo"))    # Caso 1 -> RECHAZADO (F,F,F)
print(autorizar_prestamo(17, 1500, "bueno"))   # Caso 2 -> RECHAZADO (F,F,V)
print(autorizar_prestamo(17, 2500, "malo"))    # Caso 3 -> RECHAZADO (F,V,F)
print(autorizar_prestamo(17, 2500, "bueno"))   # Caso 4 -> RECHAZADO (F,V,V)
print(autorizar_prestamo(20, 1500, "malo"))    # Caso 5 -> RECHAZADO (V,F,F)
print(autorizar_prestamo(20, 1500, "bueno"))   # Caso 6 -> RECHAZADO (V,F,V)
print(autorizar_prestamo(20, 2500, "malo"))    # Caso 7 -> RECHAZADO (V,V,F)
print(autorizar_prestamo(40, 2500, "bueno"))   # Caso 8 -> APROBADO (V,V,V)