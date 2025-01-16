import sqlite3
import os
from prettytable import PrettyTable


def criar_clientes():
    
    conn = sqlite3.connect("C:\Repositorios\Passagens_aerea_relacionamento\Banco_dados.db")
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
    
    conn = sqlite3.connect("C:\Repositorios\Passagens_aerea_relacionamento\Banco_dados.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS voo (
            id_voo INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_voo VARCHAR(10) UNIQUE NOT NULL,
            origem INT NOT NULL,
            destino INT NOT NULL,
            data_partida TIMESTAMP NOT NULL,
            data_chegada TIMESTAMP NOT NULL,
            preco INTEGER,
            duracao INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def criar_aeroporto():
    
    conn = sqlite3.connect("C:\Repositorios\Passagens_aerea_relacionamento\Banco_dados.db")
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
    
criar_clientes()
criar_voo()
criar_aeroporto()
