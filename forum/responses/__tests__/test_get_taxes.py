import pytest
from forum.responses.get_taxes import calcular_impuesto


@pytest.mark.parametrize(
    "salario, dependientes, es_jubilado, esperado",
    [
        # Caso 1: dependientes = 0, no jubilado
        # Usa descuento=0 directamente en el cálculo final
        (10000, 0, False, 1500),

        # Caso 2: dependientes = 0, jubilado
        # descuento = 0 + 10000*0.05 = 500 -> impuesto = 1500 - 500 = 1000
        (10000, 0, True, 1000),

        # Caso 3: dependientes > 0, no jubilado
        # descuento = 2*500 = 1000 -> impuesto = 1500 - 1000 = 500
        (10000, 2, False, 500),

        # Caso 4: dependientes > 0, jubilado
        # descuento = 2*500 + 10000*0.05 = 1000 + 500 = 1500 -> impuesto = 0
        (10000, 2, True, 0),
    ],
)
def test_calcular_impuesto_all_uses(salario, dependientes, es_jubilado, esperado):
    """Cobertura All-Uses de la variable 'descuento' y resto de variables."""
    resultado = calcular_impuesto(salario, dependientes, es_jubilado)
    assert resultado == pytest.approx(esperado)