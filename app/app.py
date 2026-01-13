from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Connexion à PostgreSQL
DB_HOST = os.environ.get("POSTGRES_HOST", "db")
DB_NAME = os.environ.get("POSTGRES_DB", "mydb")
DB_USER = os.environ.get("POSTGRES_USER", "user")
DB_PASS = os.environ.get("POSTGRES_PASSWORD", "password")

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

@app.route('/')
def home():
    return "Bienvenue sur la page d'accueil !"

@app.route('/users')
def users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, name FROM users;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return {"users": rows}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
