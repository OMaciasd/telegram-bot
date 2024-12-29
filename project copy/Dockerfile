FROM debian:bullseye

# Instalar curl con versión fija, y configurar usuario no root
RUN apt-get update && \
 apt-get install -y --no-install-recommends \
 curl=7.74.0-1.3+deb11u14 \
 python3-pip=20.3.4-4+deb11u1 && \
 rm -rf /var/lib/apt/lists/* && \
 groupadd -r appgroup && \
 useradd -r -g appgroup -m appuser

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios para la instalación de dependencias
COPY requirements.txt .

# Instalar dependencias de Python sin caché
RUN pip3 install --no-cache-dir -r requirements.txt

# Copiar el script principal
COPY script.py .

# Cambiar a usuario no root después de las copias
USER appuser

# Instrucción HEALTHCHECK para asegurar que el contenedor sigue saludable
HEALTHCHECK CMD ["sh", "-c", "curl --fail http://localhost:5000/ || exit 1"]

# Usar exec form para el comando final
CMD ["python3", "script.py"]
