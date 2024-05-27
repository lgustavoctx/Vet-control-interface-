CREATE TABLE IF NOT EXISTS tutors (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    metodo_pagamento TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS animais (
    id INTEGER PRIMARY KEY,
    tutor_id INTEGER NOT NULL,
    nome TEXT NOT NULL,
    peso REAL NOT NULL,
    porte TEXT NOT NULL,
    sintomas TEXT,
    raca TEXT NOT NULL,
    idade INTEGER NOT NULL,
    FOREIGN KEY (tutor_id) REFERENCES tutors(id)
);

CREATE TABLE IF NOT EXISTS veterinarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    telefone TEXT NOT NULL,
    crmv TEXT NOT NULL,
    email TEXT NOT NULL
);
