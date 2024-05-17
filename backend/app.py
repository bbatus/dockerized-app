from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database COnnection 
def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB', 'testdb'),
        user=os.getenv('POSTGRES_USER', 'postgres'),
        password=os.getenv('POSTGRES_PASSWORD', 'password'),
        host='db'
    )
    return conn

@app.route('/')
def hello():
    return "Hello from Backend!"

@app.route('/db')
def db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f"Database version: {db_version}"

# Table Method
@app.route('/create_table', methods=['POST'])
def create_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            age INTEGER
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()
    return "Table created", 201

# Add data method
@app.route('/add', methods=['POST'])
def add_entry():
    data = request.get_json()
    name = data['name']
    age = data['age']
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO test_table (name, age) VALUES (%s, %s)', (name, age))
    conn.commit()
    cur.close()
    conn.close()
    return "Entry added", 201

# Get data method
@app.route('/entries', methods=['GET'])
def get_entries():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM test_table')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)