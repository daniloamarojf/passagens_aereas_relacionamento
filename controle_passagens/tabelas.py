import sqlite3
import os
from pathlib import Path
from prettytable import PrettyTable


def criar_clientes():
    
    
    db_path = Path("C:\Repositorios\Relaciomento_passagens_aereas\passagens_aereas_relacionamento\Banco_dados.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf INTEGER (11),
            telefone VARCHAR(14),
            data_nascimento date
        )
    ''')
    conn.commit()
    conn.close()

def criar_voo():
    
    db_path = Path("C:\Repositorios\Relaciomento_passagens_aereas\passagens_aereas_relacionamento\Banco_dados.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS voo (
            id_voo INTEGER PRIMARY KEY AUTOINCREMENT,
            origem INT NOT NULL,
            destino INT NOT NULL,
            data_partida TIMESTAMP NOT NULL,
            data_chegada TIMESTAMP NOT NULL,
            preco INTEGER,
            FOREIGN KEY (origem) REFERENCES aeroporto(id_aeroporto),
            FOREIGN KEY (destino) REFERENCES aeroporto(id_aeroporto)
        )
    ''')
    conn.commit()
    conn.close()

def criar_aeroporto():
    
    db_path = Path("C:\Repositorios\Relaciomento_passagens_aereas\passagens_aereas_relacionamento\Banco_dados.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS aeroporto (
            id_aeroporto INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_aeroporto VARCHAR(100) NOT NULL,
            codigo_iata CHAR(3) UNIQUE NOT NULL,
            cidade VARCHAR(50) NOT NULL,
            pais VARCHAR(50) NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    
