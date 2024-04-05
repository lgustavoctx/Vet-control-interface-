
-- database.sql

-- Create table for tutors
CREATE TABLE IF NOT EXISTS tutors (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    modo_pagamento TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT NOT NULL
);

-- Create table for animais
CREATE TABLE IF NOT EXISTS animais (
    id INTEGER PRIMARY KEY,
    tutor_id INTEGER NOT NULL,
    nome TEXT NOT NULL,
    peso REAL NOT NULL,
    raca TEXT NOT NULL,
    tamanho TEXT NOT NULL,
    idade INTEGER NOT NULL,
    problema_saude TEXT,
    FOREIGN KEY (tutor_id) REFERENCES tutors(id)
);

-- Create table for veterinarios
CREATE TABLE IF NOT EXISTS veterinarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    especialidade TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT NOT NULL
);

