import pytest
from forum.responses.process_transaction import procesar_transaccion_refactored


class Usuario:
    def __init__(self, es_premium=False):
        self.es_premium = es_premium

class UsuarioSinPremium:
    """Usuario sin atributo es_premium."""
    pass

def test_transaccion_nacional_no_premium_aprobada():
    usuario = Usuario(es_premium=False)
    assert procesar_transaccion_refactored(1000, "nacional", usuario) == "Aprobada"


def test_transaccion_internacional_premium_aprobada():
    usuario = Usuario(es_premium=True)
    # aquí solo verificamos que no falle y sea aprobada con monto positivo
    assert procesar_transaccion_refactored(1000, "internacional", usuario) == "Aprobada"


def test_transaccion_monto_negativo_rechazada():
    usuario = Usuario(es_premium=True)
    assert procesar_transaccion_refactored(-100, "nacional", usuario) == "Rechazada"


def test_usuario_sin_es_premium_no_revienta_y_aprueba():
    usuario = UsuarioSinPremium()
    assert procesar_transaccion_refactored(1000, "nacional", usuario) == "Aprobada"


# EXTRA: misma lógica individual pero en formato "array" con parametrize
@pytest.mark.parametrize(
    "monto, tipo, clase_usuario, es_premium, esperado, descripcion",
    [
        # 1) nacional, no premium -> Aprobada
        (1000, "nacional",      Usuario,         False, "Aprobada",  "nacional no premium"),

        # 2) internacional, premium -> Aprobada
        (1000, "internacional", Usuario,         True,  "Aprobada",  "internacional premium"),

        # 3) monto negativo -> Rechazada
        (-100, "nacional",      Usuario,         True,  "Rechazada", "monto negativo"),

        # 4) usuario sin es_premium -> no debe romper, Aprobada
        (1000, "nacional",      UsuarioSinPremium, None, "Aprobada", "usuario sin es_premium"),
    ],
)
def test_transacciones_parametrizadas(monto, tipo, clase_usuario, es_premium, esperado, descripcion):
    # Creamos el usuario según la clase
    if clase_usuario is Usuario:
        usuario = clase_usuario(es_premium=es_premium)
    else:
        # UsuarioSinPremium no tiene es_premium
        usuario = clase_usuario()

    resultado = procesar_transaccion_refactored(monto, tipo, usuario)
    assert resultado == esperado, f"Fallo en caso: {descripcion}"