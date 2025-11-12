import pandas as pd
import itertools

# Definir las opciones de cada parámetro
parametros = [
    ["Ecuador", "Perú"],  # Temperatura
    ["Chile", "México"],  # Tiempo
    ["Económico", "Ejecutivo"]  # Rejilla
]

# Generar todas las combinaciones posibles (como en un diseño factorial 2^3)
combinaciones = list(itertools.product(*parametros))

# Crear un DataFrame con las combinaciones
df = pd.DataFrame(combinaciones, columns=["Temperatura", "Tiempo", "Rejilla"])

print(df)