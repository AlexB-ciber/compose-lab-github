from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Task1: Build works! Сервер запущено."

if __name__ == "__main__":
    # host='0.0.0.0' обов'язково для Docker, щоб сервер був доступний ззовні
    app.run(host='0.0.0.0', port=5000)
