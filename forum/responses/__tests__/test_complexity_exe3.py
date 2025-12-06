import pytest
from  forum.responses.refactor import calcular_tarifa_original, refacto_calcular_tarifa


@pytest.mark.parametrize(
    "edad, es_estudiante, es_senior, dia_semana, hora",
    [
        (10, False, False, "lunes", 10),       # niño, día normal, hora normal
        (10, True,  False, "sabado", 19),      # niño estudiante, finde, noche
        (30, False, False, "lunes", 10),       # adulto sin descuentos
        (30, True,  False, "domingo", 20),     # adulto estudiante, finde, noche
        (70, False, True,  "miercoles", 17),   # senior con descuento
        (70, True,  True,  "sabado", 21),      # senior estudiante, finde, noche
    ],
)
def test_calcular_tarifa_equivalente(edad, es_estudiante, es_senior, dia_semana, hora):
    """La versión refactorizada debe dar el mismo resultado que la original."""
    original = calcular_tarifa_original(edad, es_estudiante, es_senior, dia_semana, hora)
    refactor = refacto_calcular_tarifa(edad, es_estudiante, es_senior, dia_semana, hora)

    assert round(original, 4) == round(refactor, 4)


def test_tarifa_casos_concretos():
    """Algunos valores específicos para documentar comportamiento."""
    # niño sin nada, día normal
    assert refacto_calcular_tarifa(10, False, False, "lunes", 10) == pytest.approx(5.0)

    # adulto sin descuentos, día normal, hora normal
    assert refacto_calcular_tarifa(30, False, False, "martes", 10) == pytest.approx(10.0)

    # senior con descuento, sin recargos
    assert refacto_calcular_tarifa(70, False, True, "miercoles", 10) == pytest.approx(6 * 0.7)

    # adulto estudiante en domingo por la noche
    # base 10 -> estudiante (0.8) -> finde (1.5) -> noche (1.2)
    esperado = 10 * 0.8 * 1.5 * 1.2
    assert refacto_calcular_tarifa(30, True, False, "domingo", 20) == pytest.approx(esperado)