import sqlite3
import os
from prettytable import PrettyTable
from pathlib import Path


def visualizar_cliente():
        
    db_path = Path("C:/Repositorios/passagens_aereas_relacionamento/Banco_dados.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    
    print('1 - Visualizar Cliente')
    print('2 - Visualizar todos os Clientes')
    opcao_visualizar = input('====> Escolha a opção: ')
    
    if opcao_visualizar == '1':    
        id_cliente = input('Qual a identificação do Cliente que deseja visualizar? ')    
            
        cursor.execute('SELECT * FROM clientes WHERE id_cliente = ?', (id_cliente,))   # pORQUE ESSA VÍRGULA?
        resultados = cursor.fetchall()
            
        tabela = PrettyTable()
            
        colunas = [descricao [0] for descricao in cursor.description]
            
        tabela.field_names = colunas
            
        for row in resultados:
            tabela.add_row(row)
                
        print(tabela)
        input('Pressione Enter')
        conn.close()
    elif opcao_visualizar == '2':
        cursor.execute('SELECT * FROM clientes')
        resultados = cursor.fetchall()
            
        tabela = PrettyTable()
            
        colunas = [descricao [0] for descricao in cursor.description]
            
        tabela.field_names = colunas
            
        for row in resultados:
            tabela.add_row(row)
                
        print(tabela)
        input('Pressione Enter')
        conn.close()
        
        
    else:
        input('Opção inválida. Pressione enter!')    
    
   
def visualizar_voo():
        
    db_path = Path("C:/Repositorios/passagens_aereas_relacionamento/Banco_dados.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    
    print('1 - Visualizar Voo')
    print('2 - Visualizar todos os Voos')
    opcao_visualizar = input('====> Escolha a opção: ')
    
    if opcao_visualizar == '1':    
        id_voo = input('Qual a identificação do Voo que deseja visualizar? ')    
            
        cursor.execute('SELECT * FROM voo WHERE id_voo = ?', (id_voo,))   # pORQUE ESSA VÍRGULA?
        resultados = cursor.fetchall()
            
        tabela = PrettyTable()
            
        colunas = [descricao [0] for descricao in cursor.description]
            
        tabela.field_names = colunas
            
        for row in resultados:
            tabela.add_row(row)
                
        print(tabela)
        input('Pressione Enter')
        conn.close()
    elif opcao_visualizar == '2':
        cursor.execute('SELECT * FROM voo')
        resultados = cursor.fetchall()
            
        tabela = PrettyTable()
            
        colunas = [descricao [0] for descricao in cursor.description]
            
        tabela.field_names = colunas
            
        for row in resultados:
            tabela.add_row(row)
                
        print(tabela)
        input('Pressione Enter')
        conn.close()
        
        
    else:
        input('Opção inválida. Pressione enter!')    
   
def visualizar_aeroporto():
        
    db_path = Path("C:/Repositorios/passagens_aereas_relacionamento/Banco_dados.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    
    print('1 - Visualizar Aeroporto')
    print('2 - Visualizar todos os Aeroportos')
    opcao_visualizar = input('====> Escolha a opção: ')
    
    if opcao_visualizar == '1':    
        id_aeroporto = input('Qual a identificação do Aeroporto que deseja visualizar? ')    
            
        cursor.execute('SELECT * FROM aeroporto WHERE id_aeroporto = ?', (id_aeroporto,))   # pORQUE ESSA VÍRGULA?
        resultados = cursor.fetchall()
            
        tabela = PrettyTable()
            
        colunas = [descricao [0] for descricao in cursor.description]
            
        tabela.field_names = colunas
            
        for row in resultados:
            tabela.add_row(row)
                
        print(tabela)
        input('Pressione Enter')
        conn.close()
    elif opcao_visualizar == '2':
        cursor.execute('SELECT * FROM aeroporto')
        resultados = cursor.fetchall()
            
        tabela = PrettyTable()
            
        colunas = [descricao [0] for descricao in cursor.description]
            
        tabela.field_names = colunas
            
        for row in resultados:
            tabela.add_row(row)
                
        print(tabela)
        input('Pressione Enter')
        conn.close()
        
        
    else:
        input('Opção inválida. Pressione enter!')    
   
   