CREATE TABLE IF NOT EXISTS tutors (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    modo_pagamento TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS animais (
    id INTEGER PRIMARY KEY,
    nome_tutor TEXT NOT NULL,
    nome TEXT NOT NULL,
    peso REAL NOT NULL,
    raca TEXT NOT NULL,
    tamanho TEXT NOT NULL,
    idade INTEGER NOT NULL,
    problema_saude TEXT,
    FOREIGN KEY (nome_tutor) REFERENCES tutors(nome)
);

CREATE TABLE IF NOT EXISTS veterinarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    especialidade TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT NOT NULL
);

