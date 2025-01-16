import sqlite3
import os
from prettytable import PrettyTable

conn = sqlite3.connect("C:\Repositorios\Passagens_aerea_relacionamento\Banco_dados.db")
cursor = conn.cursor()

def cabecalho(nome_cabecalho):
    print (f':::::::::: { nome_cabecalho } ::::::::::\n\n')
    return()


def crud():
        
    print('1 - Adicionar')
    print('2 - Alterar dados')  
    print('3 - Remover')  
    print('4 - Visualizar')
    
def crud_tabelas():
    print('::::  ADMINISTRAÇÃO DE TABELAS  ::::\n')
    print('1 - Cliente')
    print('2 - Voo')
    print('3 - Aeroporto\n')
    
    
def cliente_existe(id_cliente):
    cursor.execute(
        'SELECT 1 FROM Clientes WHERE id_cliente = ?', (id_cliente,))
    
    return cursor.fetchone() is not None