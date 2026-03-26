import os
import sys
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    mode = os.getenv('MODE', 'not set')
    is_debug = '--debug' in sys.argv
    # Використовуємо <br> для переносу рядка в браузері
    return f"Mode={mode}<br>Debug={is_debug}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)
