import sqlite3
import os
from prettytable import PrettyTable
from pathlib import Path


def remover_cliente(): 
        
    db_path = Path("C:\Repositorios\Relaciomento_passagens_aereas\passagens_aereas_relacionamento\Banco_dados.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
   
    id_cliente = input('Qual a identificação do Cliente a ser REMOVIDO?: ')
        
    cursor.execute('SELECT nome FROM clientes WHERE id_cliente = ?', (id_cliente))
    cliente = cursor.fetchone()
        
    if cliente:
        print()
        nome_cliente = cliente[0]
        opcao_excluir = input(f'Deseja realmente excluir o Cliente: {nome_cliente} ? (1 - Sim/ 2 - Não) ')
            
        if opcao_excluir == '1':
            cursor.execute('DELETE FROM clientes WHERE id_cliente = ?', (id_cliente))
            conn.commit() 
            print()
            input('Cliente removido com sucesso. Pressione enter!')
            conn.close()    
        else:
            input('Cliente NÃO removido. Pressione enter!')

def remover_voo(): 
        
    db_path = Path("C:\Repositorios\Relaciomento_passagens_aereas\passagens_aereas_relacionamento\Banco_dados.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

        
    id_voo = input('Qual a identificação do Voo a ser REMOVIDO?: ')
        
    cursor.execute('SELECT id_voo FROM voo WHERE id_voo = ?', (id_voo))
    voo = cursor.fetchone()
        
    if voo:
        print()
        numero_voo2 = voo[0]
        opcao_excluir = input(f'Deseja realmente excluir o Voo: {numero_voo2} ? (1 - Sim/ 2 - Não) ')
            
        if opcao_excluir == '1':
            cursor.execute('DELETE FROM voo WHERE id_voo = ?', (id_voo))
            conn.commit() 
            print()
            input('Voo removido com sucesso. Pressione enter!')
            conn.close()    
        else:
            input('Voo NÃO removido. Pressione enter!')
            
def remover_aeroporto(): 
        
    db_path = Path("C:\Repositorios\Relaciomento_passagens_aereas\passagens_aereas_relacionamento\Banco_dados.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

        
    id_aeroporto = input('Qual a identificação do Aeroporto a ser REMOVIDO?: ')
        
    cursor.execute('SELECT nome_aeroporto FROM aeroporto WHERE id_aeroporto = ?', (id_aeroporto))
    aeroporto = cursor.fetchone()
        
    if aeroporto:
        print()
        nome_aeroporto2 = aeroporto[0]
        opcao_excluir = input(f'Deseja realmente excluir o Aeroporto: {nome_aeroporto2} ? (1 - Sim/ 2 - Não) ')
            
        if opcao_excluir == '1':
            cursor.execute('DELETE FROM aeroporto WHERE id_aeroporto = ?', (id_aeroporto))
            conn.commit() 
            print()
            input('Aeroporto removido com sucesso. Pressione enter!')
            conn.close()    
        else:
            input('Aeroporto NÃO removido. Pressione enter!')

def remover_venda(): 
        
    db_path = Path("C:\Repositorios\Relaciomento_passagens_aereas\passagens_aereas_relacionamento\Banco_dados.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

        
    id_venda = input('Qual a identificação da Venda a ser REMOVIDA?: ')
        
    cursor.execute('SELECT id_cliente FROM venda_passagens WHERE id_venda = ?', (id_venda))
    venda = cursor.fetchone()
        
    if venda:
        print()
        nome2 = venda[0]
        opcao_excluir = input(f'Deseja realmente excluir o cliente: {nome2} ? (1 - Sim/ 2 - Não) ')
            
        if opcao_excluir == '1':
            cursor.execute('DELETE FROM venda_passagens WHERE id_venda = ?', (id_venda))
            conn.commit() 
            print()
            input('Venda removida com sucesso. Pressione enter!')
            conn.close()    
        else:
            input('Venda NÃO removida. Pressione enter!')
