import time
import random
import statistics

def simulated_request():
    # Simula tiempos de respuesta entre 0.1 y 1.2 segundos
    latency = random.uniform(0.1, 1.2)
    time.sleep(latency / 50)  # divide para no esperar demasiado
    return latency

latencias = [simulated_request() for _ in range(200)]
print("Promedio:", statistics.mean(latencias))
print("Mínimo:", min(latencias))
print("Máximo:", max(latencias))
print("Percentil 95:", statistics.quantiles(latencias, n=100)[94])