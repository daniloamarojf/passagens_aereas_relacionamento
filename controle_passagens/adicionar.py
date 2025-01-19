import sqlite3
import os
from prettytable import PrettyTable
from pathlib import Path


def adicionar_cliente(): 
        
    db_path = Path("C:/Repositorios/passagens_aereas_relacionamento/Banco_dados.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

        
    nome = input('Nome cliente: ')
    cpf = input('CPF: ')
    telefone = input('Telefone: ')
    data_nascimento = input('Data de nascimento: ')
        
    dados_cliente = (nome, cpf, telefone, data_nascimento)
        
    cursor.execute('INSERT INTO clientes (nome, cpf, telefone, data_nascimento) VALUES (?,?,?,?)', dados_cliente)
        
    conn.commit()
    print()
    input('Cliente adicionado com sucesso. Pressione enter!')
    conn.close()
    
    
def adicionar_aeroporto(): 
        
    db_path = Path("C:/Repositorios/passagens_aereas_relacionamento/Banco_dados.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

        
    nome_aeroporto = input('Nome Aeroporto: ')
    codigo_iata = input('Codigo IATA: ')
    cidade = input('Cidade: ')
    pais = input('País: ')
        
    dados_aeroporto = (nome_aeroporto, codigo_iata, cidade, pais)
        
    cursor.execute('INSERT INTO aeroporto (nome_aeroporto, codigo_iata, cidade, pais) VALUES (?,?,?,?)', dados_aeroporto)
        
    conn.commit()
    print()
    input('Aeroporto adicionado com sucesso. Pressione enter!')
    conn.close()   
    
    
     
def adicionar_voo(): 
        
    db_path = Path("C:/Repositorios/passagens_aereas_relacionamento/Banco_dados.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    
    cursor.execute('SELECT * FROM aeroporto')
    resultado = cursor.fetchall()
    
    if not resultado:
        print('Nenhum Aeroporto encontrado. Cadastre Aeroportos primeiro.')
        # conn.close()
        return
    
    tabela = PrettyTable(['id_aeroporto', 'nome_aeroporto', 'codigo_iata', 'cidade', 'pais'])
    for linha in resultado:
        tabela.add_row(linha)
    print(tabela)
    
    origem = int(input('Digite o ID do aeroporto de origem: '))
    destino = int(input('Digite o ID do aeroporto de destino: '))
    data_partida = input('Data de partida (YYYY-MM-DD): ')
    data_chegada = input('Data de chegada (YYYY-MM-DD): ')
    preco = float(input('Preço: '))
    
    dados_voo = (origem, destino, data_partida, data_chegada, preco)
    
    cursor.execute('INSERT INTO voo (origem, destino, data_partida, data_chegada, preco) VALUES (?, ?, ?, ?, ?)', dados_voo)
    conn.commit()
    print('Voo adicionado com sucesso!')
    conn.close()
