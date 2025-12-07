FROM mcr.microsoft.com/devcontainers/python:3.12

# Instala dependencias del proyecto
WORKDIR /workspace
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copia todo el código dentro del contenedor
COPY . .

# Puertos que vamos a usar (flask, locust)
EXPOSE 8000 8089

# Copia el script de entrada a un lugar del PATH
COPY .devcontainer/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Comando por defecto al iniciar el contenedor
CMD ["entrypoint.sh"]