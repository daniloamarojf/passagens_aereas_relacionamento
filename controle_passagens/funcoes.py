import sqlite3
import os
from prettytable import PrettyTable

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
    print('2 - Aeroporto')
    print('3 - Voo\n')
