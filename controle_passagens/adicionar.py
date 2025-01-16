import sqlite3
import os
from prettytable import PrettyTable


def adicionar_cliente(): 
        
    conn = sqlite3.connect("C:\Repositorios\Passagens_aerea_relacionamento\Banco_dados.db")
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
    
def adicionar_voo(): 
    conn = sqlite3.connect("C:\Repositorios\Passagens_aerea_relacionamento\Banco_dados.db")
    cursor = conn.cursor()
    
    cursor.execute(''' 
    SELECT * from clientes
    ''')
    resultados = cursor.fetchall()
        
    if not resultados:
        
        print('Nenhum cliente encontrado. Cadastre um cliente primeiro')
        
        return
    
    tabela = PrettyTable(['id_cliente', 'Nome'])
    for linha in resultados:
        tabela.add_row(linha)
    print(tabela)
    
    try: 
        # Garantir que o ID seja um número inteiro
        id_cliente = int(input('Digite o ID do cliente: '))
        
        # Verificar se o cliente existe antes de prosseguir
        if not cliente_existe(id_cliente):
            
            print(f'Erro: Cliente com ID {id_cliente} não encontrado!')
            print('Por favor, cadastre o cliente primeiro.')
            
            return
        
        numero_voo = input('Numero do Voo: ')
        origem = input('Origem: ')
        destino = input('Destino: ')
        data_partida = input('Data de partida: ')
        data_chegada = input('Data de chegada: ')
        duracao = input('Duração: ')
        
        dados_voo = (numero_voo, origem, destino, data_partida, data_chegada, duracao)
        
        cursor.execute('INSERT INTO voo (id_cliente, numero_voo, origem, destino, data_partida, data_chegada, duracao) VALUES (?,?,?,?,?,?,?)', dados_voo)
        
        conn.commit()
        print()
        input('Voo adicionado com sucesso. Pressione enter!')
        conn.close()
    
    except ValueError:
        print('-'*70)
        print('Erro: ID do cliente deve ser um número inteiro.')
        print('-'*70)
    
def adicionar_aeroporto(): 
        
    conn = sqlite3.connect("C:\Repositorios\Passagens_aerea_relacionamento\Banco_dados.db")
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
    
adicionar_cliente()
