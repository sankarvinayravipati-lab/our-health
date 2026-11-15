from flask import Flask, render_template
import mysql.connector
from db import get_connection

app = Flask(__name__)

@app.route('/')
def home():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM diseases")
    diseases = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', diseases=diseases)

if __name__ == '__main__':
    app.run(debug=True)
