import pymysql
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    connection = pymysql.connect(
        host="database-1.xxxxxxx.us-east-1.rds.amazonaws.com",
        user="admin",
        password="mypassword",
        database="mydatabase"
    )
    return connection

@app.route('/')
def home():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    connection.close()
    return f"Database connected! Current time: {result[0]}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
