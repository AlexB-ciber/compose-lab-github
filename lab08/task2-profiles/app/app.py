from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Task2: Profiles working"

if __name__ == "__main__":
    # Ми додаємо перевірку name == main, щоб уникнути помилок при імпорті
    app.run(host="0.0.0.0", port=6000)
