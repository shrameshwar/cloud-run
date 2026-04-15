import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host='/cloudsql/' + os.environ.get("INSTANCE_CONNECTION_NAME"),
        dbname=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS")
    )

@app.route("/")
def hello():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return f"DB Connected! Time: {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
