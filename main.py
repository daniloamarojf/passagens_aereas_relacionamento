import sqlite3
import os
from prettytable import PrettyTable
from controle_passagens.tabelas import criar_clientes, criar_aeroporto, criar_voo
from controle_passagens.funcoes import cabecalho, crud, crud_tabelas
from controle_passagens.adicionar import adicionar_cliente, adicionar_aeroporto, adicionar_voo
from controle_passagens.alterar import alterar_cliente, alterar_voo, alterar_aeroporto
from controle_passagens.remover import remover_cliente, remover_voo, remover_aeroporto
from controle_passagens.visualizar import visualizar_cliente, visualizar_voo, visualizar_aeroporto

criar_clientes()
criar_aeroporto()
criar_voo()

os.system('cls')
while True:
    os.system('cls')
    crud_tabelas()
  
    opcao_tabelas = input('====> Qual tabela deseja administar? ')

    if opcao_tabelas == '1':
        os.system('cls')
        cabecalho('CLIENTE')
        crud()
        opcao = input('=====> Escolha a opção: ')
        
        
        if opcao == '1':
            cabecalho('ADICIONAR CLIENTE')
            adicionar_cliente()
        elif opcao == '2':
            cabecalho('ALTERAR CLIENTE')
            alterar_cliente()
        elif opcao == '3':
            cabecalho('REMOVER CLIENTE')
            remover_cliente()
        elif opcao == '4':
            cabecalho('VISUALIZAR CLIENTE')
            visualizar_cliente()
        else:
            input('Opção inválida! Pressione enter.') 
            
    elif opcao_tabelas == '2':
        os.system('cls')
        cabecalho('AEROPORTO')
        crud()
        opcao = input('=====> Escolha a opção: ')
        
        
        if opcao == '1':
            cabecalho('ADICIONAR AEROPORTO')
            adicionar_aeroporto()
        elif opcao == '2':
            cabecalho('ALTERAR AEROPORTO')
            alterar_aeroporto()
        elif opcao == '3':
            cabecalho('REMOVER AEROPORTO')
            remover_aeroporto()
        elif opcao == '4':
            cabecalho('VISUALIZAR AEROPORTO')
            visualizar_aeroporto()
        else:
            input('Opção inválida! Pressione enter.') 
            
    elif opcao_tabelas == '3':    
        os.system('cls')
        cabecalho('VOO')
        crud()
        opcao = input('=====> Escolha a opção: ')
        
        
        if opcao == '1':
            cabecalho('ADICIONAR VOO')
            adicionar_voo()
        elif opcao == '2':
            cabecalho('ALTERAR VOO')
            alterar_voo()
        elif opcao == '3':
            cabecalho('REMOVER VOO')
            remover_voo()
        elif opcao == '4':
            cabecalho('VISUALIZAR VOO')
            visualizar_voo()
        else:
            input('Opção inválida! Pressione enter.') 

    else:
        print('FIM')
