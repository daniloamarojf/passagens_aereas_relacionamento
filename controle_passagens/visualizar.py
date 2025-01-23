import sqlite3
import os
from prettytable import PrettyTable
from pathlib import Path


def visualizar_cliente():
        
    db_path = Path("C:\Repositorios\Relaciomento_passagens_aereas\passagens_aereas_relacionamento\Banco_dados.db")
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
        
    db_path = Path("C:\Repositorios\Relaciomento_passagens_aereas\passagens_aereas_relacionamento\Banco_dados.db") # Definindo o caminho
    conn = sqlite3.connect(db_path)  # Conectando o BD
    cursor = conn.cursor()

    print('1 - Visualizar Voo')
    print('2 - Visualizar todos os Voos')
    opcao_visualizar = input('====> Escolha a opção: ')
    
    if opcao_visualizar == '1':    
        id_voo = input('Qual a identificação do Voo que deseja visualizar? ')    
            
        cursor.execute('''
            SELECT voo.id_voo,
                    aeroporto_origem.nome_aeroporto AS origem,
                    aeroporto_destino.nome_aeroporto AS destino,
                    voo.data_partida,
                    voo.data_chegada,
                    voo.preco 
            FROM voo 
            JOIN aeroporto aeroporto_origem ON voo.origem = aeroporto_origem.id_aeroporto
            JOIN aeroporto aeroporto_destino ON voo.destino = aeroporto_destino.id_aeroporto
            WHERE id_voo = ?
        ''', (id_voo,))
        
        # Variável para armazenar consulta
        resultados = cursor.fetchall()
            
        tabela = PrettyTable()
            
        colunas = [descricao [0] for descricao in cursor.description] # description: retorna o nome das colunas
            
        tabela.field_names = colunas
            
        for row in resultados:
            tabela.add_row(row) # Adiciona linha de resultado à tabela
                
        print(tabela)
        input('Pressione Enter')
        conn.close()
        
    elif opcao_visualizar == '2':
    
        cursor.execute('''
            SELECT voo.id_voo, 
                   aeroporto_origem.nome_aeroporto AS origem, 
                   aeroporto_destino.nome_aeroporto AS destino,
                   voo.data_partida, 
                   voo.data_chegada, 
                   voo.preco
            FROM voo
            JOIN aeroporto aeroporto_origem ON voo.origem = aeroporto_origem.id_aeroporto
            JOIN aeroporto aeroporto_destino ON voo.destino = aeroporto_destino.id_aeroporto
        ''')
        
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
        
    db_path = Path("C:\Repositorios\Relaciomento_passagens_aereas\passagens_aereas_relacionamento\Banco_dados.db")
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
   
 
def visualizar_venda():
        
    db_path = Path("C:\Repositorios\Relaciomento_passagens_aereas\passagens_aereas_relacionamento\Banco_dados.db") # Definindo o caminho
    conn = sqlite3.connect(db_path)  # Conectando o BD
    cursor = conn.cursor()

    print('1 - Visualizar Venda')
    print('2 - Visualizar todas as Venda')
    opcao_visualizar = input('====> Escolha a opção: ')
    
    if opcao_visualizar == '1':    
        id_venda = input('Qual Venda deseja visualizar? ')    
            
        cursor.execute('''
            SELECT venda_passagens.id_venda,
                    clientes.nome AS nome_cliente,
                    aeroporto_origem.nome_aeroporto AS origem,
                    aeroporto_destino.nome_aeroporto AS destino,
                    voo.data_partida,
                    voo.data_chegada,
                    voo.preco,
                    venda_passagens.assento,
                    venda_passagens.status 
            FROM venda_passagens 
            JOIN clientes ON venda_passagens.id_cliente = clientes.id_cliente
            JOIN voo ON venda_passagens.id.voo = voo.id_voo
            JOIN aeroporto aeroporto_origem ON voo.origem = aeroporto_origem.id_aeroporto
            JOIN aeroporto aeroporto_destino ON voo.destino = aeroporto_destino.id_aeroporto
            WHERE venda_passagens.id_venda = ?
        ''', (id_venda,))
        
        # Variável para armazenar consulta
        resultados = cursor.fetchall()
            
        tabela = PrettyTable()
            
        colunas = [descricao [0] for descricao in cursor.description] # description: retorna o nome das colunas
            
        tabela.field_names = colunas
            
        for row in resultados:
            tabela.add_row(row) # Adiciona linha de resultado à tabela
                
        print(tabela)
        input('Pressione Enter')
        conn.close()
        
    elif opcao_visualizar == '2':
    
        cursor.execute('''
            SELECT venda_passagens.id_venda,
                    clientes.nome AS nome_cliente,
                    aeroporto_origem.nome_aeroporto AS origem,
                    aeroporto_destino.nome_aeroporto AS destino,
                    voo.data_partida,
                    voo.data_chegada,
                    voo.preco,
                    venda_passagens.assento,
                    venda_passagens.status 
            FROM venda_passagens 
            JOIN clientes ON venda_passagens.id_cliente = clientes.id_cliente
            JOIN voo ON venda_passagens.id_voo = voo.id_voo
            JOIN aeroporto aeroporto_origem ON voo.origem = aeroporto_origem.id_aeroporto
            JOIN aeroporto aeroporto_destino ON voo.destino = aeroporto_destino.id_aeroporto
        ''')
        
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
  