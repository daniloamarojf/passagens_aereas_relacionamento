import sqlite3
import os
from prettytable import PrettyTable
from pathlib import Path


def adicionar_cliente(): 
        
    db_path = Path("C:\Repositorios\Relaciomento_passagens_aereas\passagens_aereas_relacionamento\Banco_dados.db")
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
        
    db_path = Path("C:\Repositorios\Relaciomento_passagens_aereas\passagens_aereas_relacionamento\Banco_dados.db")
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
        
    db_path = Path("C:\Repositorios\Relaciomento_passagens_aereas\passagens_aereas_relacionamento\Banco_dados.db")
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

def adicionar_venda(): 
        
    db_path = Path("C:\Repositorios\Relaciomento_passagens_aereas\passagens_aereas_relacionamento\Banco_dados.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    data_venda = input('Data da venda: ')
     
    cursor.execute('SELECT * FROM clientes')
    resultado = cursor.fetchall()
    
    if not resultado:
        print('Nenhum Cliente  encontrado. Cadastre Cliente primeiro.')
        # conn.close()
        return
    
    tabela = PrettyTable(['id_cliente', 'nome', 'cpf', 'telefone', 'data_nascimento'])
    for linha in resultado:
        tabela.add_row(linha)
    print(tabela)
    
    
    id_cliente = int(input('Digite o ID do cliente: '))
    
    cursor.execute('SELECT * FROM voo')
    resultado = cursor.fetchall()
    
    if not resultado:
        print('Nenhum Voo encontrado. Cadastre Voo primeiro.')
        # conn.close()
        return
    
    tabela = PrettyTable(['id_voo', 'origem', 'destino', 'data_partida', 'data_chegada','preco'])
    for linha in resultado:
        tabela.add_row(linha)
    print(tabela)
    
    id_voo = int(input('Digite o ID do Voo: '))
    assento = input('Numero do assento: ')
    status = input('Status da venda: ')
    
    
    dados_venda = (data_venda, id_cliente, id_voo, assento, status)
    
    cursor.execute('INSERT INTO venda_passagens (data_venda, id_cliente, id_voo, assento, status) VALUES (?, ?, ?, ?, ?)', dados_venda)
    conn.commit()
    print('Venda adicionado com sucesso!')
    conn.close()

