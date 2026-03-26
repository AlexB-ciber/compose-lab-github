from flask import Flask
import pymysql, os

app = Flask(__name__)
@app.route("/")
def index():
conn = pymysql.connect(
host="db",
user=os.getenv("MYSQL_USER"),
password=os.getenv("MYSQL_PASSWORD"),
database=os.getenv("MYSQL_DATABASE")
)
cursor = conn.cursor()
cursor.execute("SELECT NOW();")
result = cursor.fetchone()
conn.close()
return f"<h2>Hello from Flask + MySQL!</h2><p>Current DB time: {result}</p>"
if __name__ == "__main__":
app.run(host="0.0.0.0", port=5000)
