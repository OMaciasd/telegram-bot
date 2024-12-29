import os

# Define the base project structure
project_structure = {
    "Dockerfile": "FROM python:3.9-slim\n\n# Install required packages\n"
    "RUN apt-get update && apt-get install -y curl\n\n# Set work directory\n"
    "WORKDIR /app\n\n# Copy files\nCOPY requirements.txt .\n"
    "RUN pip install -r requirements.txt\n\n# Copy script\nCOPY script.py .\n"
    "CMD [\"python\", \"script.py\"]\n",
    "docker-compose.yml": "version: '3.9'\nservices:\n  app:\n    build: .\n"
    "environment:\n      - TELEGRAM_API_KEY=${TELEGRAM_API_KEY}\n"
    "- INSTAGRAM_ACCESS_TOKEN=${INSTAGRAM_ACCESS_TOKEN}\n    volumes:\n"
    "- ./app:/app\n    ports:\n      - \"5000:5000\"\n",
    "requirements.txt": "requests\npython-telegram-bot",
    "script.py": "# Placeholder Python script\nimport os\n\n"
    "TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')\n"
    "INSTAGRAM_ACCESS_TOKEN = os.getenv('INSTAGRAM_ACCESS_TOKEN')\n\n"
    "print(f\"Telegram Key: {TELEGRAM_API_KEY}\")\n"
    "print(f\"Instagram Token: {INSTAGRAM_ACCESS_TOKEN}\")",
    "terraform": {
        "main.tf": "provider \"aws\" {\n  region = \"us-east-1\"\n}\n\n"
        "resource \"aws_s3_bucket\" \'example\'"
        "{\n  bucket = \"example-bucket\"\n  acl    = \"private\"\n}",
    },
    "grafana": {
        "prometheus.yml": "global:\n  scrape_interval: 15s\n\n"
        "scrape_configs:\n  - job_name: 'app'\n    static_configs:\n"
        "- targets: ['localhost:5000']",
    }
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
