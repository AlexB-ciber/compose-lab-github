import os
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return f"Log level: {os.getenv('LOG')}"
app.run(host="0.0.0.0", port=8010)
