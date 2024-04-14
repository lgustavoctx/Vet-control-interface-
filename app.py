from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, template_folder='templates', static_folder='static')

DATABASE = os.path.join(BASE_DIR, 'data', 'database.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    tutores = conn.execute('SELECT * FROM tutors').fetchall()
    animais = conn.execute('SELECT * FROM animais').fetchall()
    veterinarios = conn.execute('SELECT * FROM veterinarios').fetchall()
    conn.close()
    return render_template('index.html', tutores=tutores, animais=animais, veterinarios=veterinarios)

@app.route('/cadastro-tutor')
def cadastro_tutor():
    conn = get_db_connection()
    tutores = conn.execute('SELECT * FROM tutors').fetchall()
    animais = conn.execute('SELECT * FROM animais').fetchall()
    veterinarios = conn.execute('SELECT * FROM veterinarios').fetchall()
    conn.close()
    return render_template('cadastro-tutor.html', tutores=tutores, animais=animais, veterinarios=veterinarios)

@app.route('/add_tutor', methods=['POST'])
def add_tutor():
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        modo_pagamento = request.form['modo_pagamento']
        telefone = request.form['telefone']
        email = request.form['email']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO tutors (nome, endereco, modo_pagamento, telefone, email) VALUES (?, ?, ?, ?, ?)',
                     (nome, endereco, modo_pagamento, telefone, email))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return 'Method not allowed. Please use POST to submit a new tutor.'

@app.route('/add_animal', methods=['POST'])
def add_animal():
    if request.method == 'POST':
        nome_tutor = request.form['Nome Tutor']
        nome = request.form['nome']
        peso = request.form['peso']
        raca = request.form['raca']
        tamanho = request.form['tamanho']
        idade = request.form['idade']
        problema_saude = request.form['problema_saude']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO animais (nome_tutor, nome, peso, raca, tamanho, idade, problema_saude) VALUES (?, ?, ?, ?, ?, ?, ?)',
                     (nome_tutor, nome, peso, raca, tamanho, idade, problema_saude))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return 'Method not allowed. Please use POST to submit a new animal.'

@app.route('/add_veterinario', methods=['POST'])
def add_veterinario():
    if request.method == 'POST':
        nome = request.form['nome']
        especialidade = request.form['especialidade']
        telefone = request.form['telefone']
        email = request.form['email']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO veterinarios (nome, especialidade, telefone, email) VALUES (?, ?, ?, ?)',
                     (nome, especialidade, telefone, email))
        conn.commit()
        conn.close()
        return redirect(url_for('cadastro_tutor'))
    
    return 'Method not allowed. Please use POST to submit a new veterinarian.'

if __name__ == '__main__':
    app.run(debug=True)
