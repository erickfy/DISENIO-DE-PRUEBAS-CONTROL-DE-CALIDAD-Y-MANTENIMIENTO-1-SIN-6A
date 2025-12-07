#!/usr/bin/env bash
set -e

cd /workspace

echo ">>> Iniciando API de Fibonacci en el puerto 8000..."
python -m w5.api &

# Espera 2 segundos para que la api levante
sleep 2

echo ">>> Iniciando Locust en el puerto 8089..."
locust -f locustfile.py --host=http://localhost:8000