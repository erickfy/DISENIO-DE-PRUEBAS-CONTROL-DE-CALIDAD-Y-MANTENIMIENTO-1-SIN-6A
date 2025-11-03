"""
PowerSwitch model for PyModel
Basado en el ejemplo PowerSwitch incluido en PyModel.
"""

# --- Estado global del "sistema" ---
power = False

# --- Acciones que el tester puede intentar ejecutar ---
def PowerOn():
    global power
    power = True

def PowerOff():
    global power
    power = False

# --- Habilitadores: cuándo se pueden ejecutar las acciones ---
def PowerOnEnabled():
    return not power  # solo puedes encender si está apagado

def PowerOffEnabled():
    return power      # solo puedes apagar si está prendido

# --- Estado aceptable (post-condición final válida) ---
def Accepting():
    # estado aceptable = terminado apagado
    return not power

# --- Metadata que PyModel necesita ---
state = ('power',)

actions = (PowerOn, PowerOff)

enablers = {
    PowerOn: (PowerOnEnabled,),
    PowerOff: (PowerOffEnabled,)
}

# cleanup le dice a PyModel cómo dejar el sistema en estado aceptable al final
cleanup = (PowerOff,)

def Reset():
    """Dejar el sistema en un estado inicial limpio."""
    global power
    power = False