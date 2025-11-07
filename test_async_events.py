import asyncio
import pytest

class TradingSystem:
    def __init__(self):
        self.state = "sin_orden"
        self.log = []

    async def buy(self):
        await asyncio.sleep(0.5)
        self.state = "orden_pendiente"
        self.log.append("Orden enviada")

    async def cancel(self):
        await asyncio.sleep(0.3)
        if self.state == "orden_pendiente":
            self.state = "cancelada"
        else:
            self.state = "sin_orden"
        self.log.append("Cancelación procesada")

@pytest.mark.asyncio
async def test_eventos_asincronos():
    sistema = TradingSystem()
    tarea1 = asyncio.create_task(sistema.buy())
    tarea2 = asyncio.create_task(sistema.cancel())
    await asyncio.gather(tarea1, tarea2)

    # A pesar del orden asíncrono, el sistema no debe quedar inconsistente
    assert sistema.state in ["sin_orden", "cancelada"]
    assert "Cancelación procesada" in sistema.log