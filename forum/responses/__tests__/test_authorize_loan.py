from forum.responses.authorize_loan import autorizar_prestamo

def test_prestamo_caso_1():
    # A=F, B=F, C=F
    assert autorizar_prestamo(17, 1500, "malo") == "RECHAZADO"


def test_prestamo_caso_2():
    # A=F, B=F, C=T
    assert autorizar_prestamo(17, 1500, "bueno") == "RECHAZADO"


def test_prestamo_caso_3():
    # A=F, B=T, C=F
    assert autorizar_prestamo(17, 2500, "malo") == "RECHAZADO"


def test_prestamo_caso_4():
    # A=F, B=T, C=T
    assert autorizar_prestamo(17, 2500, "bueno") == "RECHAZADO"


def test_prestamo_caso_5():
    # A=T, B=F, C=F
    assert autorizar_prestamo(20, 1500, "malo") == "RECHAZADO"


def test_prestamo_caso_6():
    # A=T, B=F, C=T
    assert autorizar_prestamo(20, 1500, "bueno") == "RECHAZADO"


def test_prestamo_caso_7():
    # A=T, B=T, C=F
    assert autorizar_prestamo(20, 2500, "malo") == "RECHAZADO"


def test_prestamo_caso_8():
    # A=T, B=T, C=T
    assert autorizar_prestamo(20, 2500, "bueno") == "APROBADO"