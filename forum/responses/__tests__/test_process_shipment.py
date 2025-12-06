from forum.responses.process_shipment import procesar_pedido

# FF
def test_no_miembro_sin_descuento():
    assert procesar_pedido(10, False, False) == 100

# VF
def test_miembro_sin_descuento():
    assert procesar_pedido(10, True, False) == 90


# FV
def test_no_miembro_con_descuento():
    assert procesar_pedido(10, False, True) == 95

# VV
def test_miembro_con_descuento():
    assert procesar_pedido(10, True, True) == 85.5