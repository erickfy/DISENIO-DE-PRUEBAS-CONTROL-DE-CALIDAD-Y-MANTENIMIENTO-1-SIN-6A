# .devcontainer/Dockerfile
FROM mcr.microsoft.com/devcontainers/java:1-21-bullseye

# Opcional: instala utilidades extra
RUN apt-get update && apt-get install -y \
    tree \
    && rm -rf /var/lib/apt/lists/*