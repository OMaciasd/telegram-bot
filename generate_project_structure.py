import os

# Define the base project structure
project_structure = {
    "Dockerfile": (
        "FROM debian:bullseye-slim\n\n"
        "ENV PYTHONUNBUFFERED=1\n"
        "ENV PYTHONDONTWRITEBYTECODE=1\n\n"
        "LABEL org.opencontainers.image.source=\""
        "LABEL maintainer=\"omaciasd\"\n"
        "LABEL org.opencontainers.image.authors=\"omaciasd\"\n"
        "LABEL org.opencontainers.image.description=\"Image Docker\"\n"
        "LABEL org.opencontainers.image.documentation=\"\"\n\n"
        "RUN apt-get update && apt-get install -y --no-install-recommends \\\n"
        "    curl=7.74.0-1.3+deb11u7 \\\n"
        "    python3-pip=20.3.4-4+deb11u1 && \\\n"
        "    apt-get clean && rm -rf /var/lib/apt/lists/* && \\\n"
        "    groupadd -r appgroup && useradd -r -g appgroup -m appuser\n\n"
        "WORKDIR /app\n\n"
        "COPY requirements.txt .\n"
        "RUN pip3 install --no-cache-dir -r requirements.txt\n\n"
        "COPY script.py .\n\n"
        "USER appuser\n\n"
        "HEALTHCHECK --interval=30s --timeout=5s CMD [\"curl\", \"--fail\","
        "\"http://localhost:5000/ || exit 1\"]\n\n"
        "CMD [\"python3\", \"script.py\"]\n"
    ),
    "docker-compose.yml": (
        "version: '3.9'\n"
        "services:\n"
        "  app:\n"
        "    build:\n"
        "      context: .\n"
        "      dockerfile: Dockerfile\n"
        "    environment:\n"
        "      TELEGRAM_API_KEY: ${TELEGRAM_API_KEY}\n"
        "    ports:\n"
        "      - \"127.0.0.1:5000:5000\"\n"
        "    cap_drop:\n"
        "      - ALL\n"
        "    security_opt:\n"
        "      - no-new-privileges:true\n"
        "    healthcheck:\n"
        "      test: [\"CMD\", \"curl\", \"-f\","
        "\"http://localhost:5000/health\"]\n"
        "      interval: 30s\n"
        "      retries: 3\n"
        "      start_period: 5s\n"
        "      timeout: 10s\n"
        "    volumes:\n"
        "      - .:/app\n"
        "    env_file:\n"
        "      - .env\n"
    ),
    "requirements.txt": "requests\npython-telegram-bot",
    "script.py": (
        "import os\n\n"
        "TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')\n"
        "INSTAGRAM_ACCESS_TOKEN = os.getenv('INSTAGRAM_ACCESS_TOKEN')\n\n"
        "print(f'Telegram Key: {TELEGRAM_API_KEY}')\n"
    ),
    "terraform": {
        "main.tf": (
            "provider \"aws\" {\n"
            "  region = \"us-east-1\"\n"
            "}\n\n"
            "resource \"aws_s3_bucket\" \"example\" {\n"
            "  bucket = \"example-bucket\"\n"
            "  acl    = \"private\"\n"
            "}\n"
        ),
    },
    "grafana": {
        "prometheus.yml": (
            "global:\n"
            "  scrape_interval: 15s\n\n"
            "scrape_configs:\n"
            "  - job_name: 'app'\n"
            "    static_configs:\n"
            "      - targets: ['localhost:5000']\n"
        ),
    },
}


def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as file:
                file.write(content)


# Create the project structure in the current directory
base_path = "./project"
os.makedirs(base_path, exist_ok=True)
create_structure(base_path, project_structure)

print(
    f"Project structure created successfully in {os.path.abspath(base_path)}"
)
