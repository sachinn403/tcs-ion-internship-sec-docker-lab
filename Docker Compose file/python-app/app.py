from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Hello from Python app inside Docker!"

# Existing test route
@app.route("/python")
def python_page():
    return "Hello from Flask /python route!"

# New DB test route
@app.route("/users")
def get_users():
    try:
        conn = mysql.connector.connect(
            host="db",           # Service name in docker-compose
            user="labuser",
            password="labpass123",
            database="labdb"
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
