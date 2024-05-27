from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(BASE_DIR, 'data', 'database.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/tutors', methods=['GET'])
def get_tutors():
    conn = get_db_connection()
    tutors = conn.execute('SELECT * FROM tutors').fetchall()
    conn.close()
    tutor_list = [dict(tutor) for tutor in tutors]
    return jsonify({'tutors': tutor_list})

@app.route('/animals', methods=['GET'])
def get_animals():
    conn = get_db_connection()
    animals = conn.execute('SELECT * FROM animais').fetchall()
    conn.close()
    animal_list = [dict(animal) for animal in animals]
    return jsonify({'animals': animal_list})

@app.route('/veterinarians', methods=['GET'])
def get_veterinarians():
    conn = get_db_connection()
    veterinarians = conn.execute('SELECT * FROM veterinarios').fetchall()
    conn.close()
    veterinarian_list = [dict(veterinarian) for veterinarian in veterinarians]
    return jsonify({'veterinarians': veterinarian_list})

@app.route('/add_tutor', methods=['POST'])
def add_tutor():
    data = request.json
    if data:
        conn = get_db_connection()
        conn.execute('INSERT INTO tutors (nome, endereco, metodo_pagamento, telefone, email) VALUES (?, ?, ?, ?, ?)',
                     (data['nome'], data['endereco'], data['metodo_pagamento'], data['telefone'], data['email']))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Tutor added successfully'}), 201
    else:
        return jsonify({'error': 'No data provided'}), 400

@app.route('/add_animal', methods=['POST'])
def add_animal():
    data = request.json
    if data:
        conn = get_db_connection()
        conn.execute('INSERT INTO animais (tutor_id, nome, peso, porte, sintomas, raca, idade) VALUES (?, ?, ?, ?, ?, ?, ?)',
                     (data['tutor_id'], data['nome'], data['peso'], data['porte'], data['sintomas'], data['raca'], data['idade']))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Animal added successfully'}), 201
    else:
        return jsonify({'error': 'No data provided'}), 400

@app.route('/add_veterinarian', methods=['POST'])
def add_veterinarian():
    data = request.json
    if data:
        conn = get_db_connection()
        conn.execute('INSERT INTO veterinarios (nome, endereco, telefone, crmv, email) VALUES (?, ?, ?, ?, ?)',
                     (data['nome'], data['endereco'], data['telefone'], data['crmv'], data['email']))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Veterinarian added successfully'}), 201
    else:
        return jsonify({'error': 'No data provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
