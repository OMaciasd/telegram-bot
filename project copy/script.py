from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


# Obtener las claves de entorno
TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')
INSTAGRAM_ACCESS_TOKEN = os.getenv('INSTAGRAM_ACCESS_TOKEN')

print(f"Telegram Key: {TELEGRAM_API_KEY}")
print(f"Instagram Token: {INSTAGRAM_ACCESS_TOKEN}")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
