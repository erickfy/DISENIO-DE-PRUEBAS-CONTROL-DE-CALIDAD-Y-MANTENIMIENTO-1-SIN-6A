def beneficios_cliente(es_miembro, plazo_incumplido, es_15_renta):
    if es_miembro:
        if not plazo_incumplido:
            if es_15_renta:
                return ["Descuento 20%", "Camiseta"]
            return ["Descuento 20%"]
    return []


def test_beneficios_cliente():
    assert beneficios_cliente(True, False, False) == ["Descuento 20%"]
    assert beneficios_cliente(True, False, True) == ["Descuento 20%", "Camiseta"]
    assert beneficios_cliente(True, True, False) == []
    assert beneficios_cliente(False, False, False) == []