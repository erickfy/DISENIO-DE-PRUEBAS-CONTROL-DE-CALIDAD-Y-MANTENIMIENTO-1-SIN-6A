from transitions import Machine
import pytest

class SistemaLogin:
    states = ["inicial", "logueandose", "logueado"]
    
    def __init__(self):
        self.machine = Machine(model=self, states=SistemaLogin.states, initial="inicial")
        self.machine.add_transition("login", "inicial", "logueandose")
        self.machine.add_transition("login_ok", "logueandose", "logueado")
        self.machine.add_transition("login_error", "logueandose", "inicial")
        self.machine.add_transition("logout", "logueado", "inicial")

def test_login_flow():
    app = SistemaLogin()
    app.login()
    assert app.state == "logueandose"
    app.login_ok()
    assert app.state == "logueado"
    app.logout()
    assert app.state == "inicial"

def test_login_error():
    app = SistemaLogin()
    app.login()
    app.login_error()
    assert app.state == "inicial"