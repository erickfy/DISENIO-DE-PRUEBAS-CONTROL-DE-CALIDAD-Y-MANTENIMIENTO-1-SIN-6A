from forum.responses.structured_testing import clasificar_riesgo


def test_camino_1_joven_historial_malo():
    # edad < 25 y historial == "malo" -> ALTO
    assert clasificar_riesgo(20, "malo", 10000) == "ALTO"


def test_camino_2_joven_historial_no_malo():
    # edad < 25 y historial != "malo" -> MEDIO
    assert clasificar_riesgo(22, "bueno", 20000) == "MEDIO"


def test_camino_3_adulto_monto_alto():
    # edad >= 25 y monto > 50000 -> ALTO
    assert clasificar_riesgo(30, "regular", 60000) == "ALTO"


def test_camino_4_adulto_monto_no_alto_historial_excelente():
    # edad >= 25, monto <= 50000, historial == "excelente" -> BAJO
    assert clasificar_riesgo(40, "excelente", 40000) == "BAJO"


def test_camino_5_adulto_monto_no_alto_historial_no_excelente():
    # edad >= 25, monto <= 50000, historial != "excelente" -> MEDIO
    assert clasificar_riesgo(35, "malo", 30000) == "MEDIO"