import sqlite3
import os
from prettytable import PrettyTable


def alterar_cliente(): 
        
    conn = sqlite3.connect("C:\Repositorios\Passagens_aerea\Banco_dados.db")
    cursor = conn.cursor()
        
    id_cliente = input('Qual a identificação do Cliente a ser ALTERADO?: ')
        
    cursor.execute('SELECT nome FROM clientes WHERE id_cliente = ?', (id_cliente))
    cliente = cursor.fetchone()
        
    if cliente:
        print()
        nome_cliente = cliente[0]
        opcao_alterar = input(f'Deseja realmente alter o cliente: {nome_cliente} ? (1 - Sim/ 2 - Não): ')
        
        if opcao_alterar == '1':
            novo_nome = input('Nome: ')
            novo_cpf = input('CPF: ')
            novo_telefone = input('Telefone:')
            nova_data_nascimento = input('Data de nascimento: ')
        
            dados_cliente = (novo_nome, novo_cpf,novo_telefone, nova_data_nascimento, id_cliente)
        
            cursor.execute('UPDATE clientes SET nome = ?, cpf = ?, telefone = ?, data_nascimento = ? WHERE id_cliente = ?',
                (dados_cliente))
        
            conn.commit()
            print()
            input('Deseja continuar alterando Clientes? Pressione enter!')
            conn.close()    
        elif opcao_alterar == '2':
            input('Cliente NÃO atualizado. Pressione enter!')
        else:
            input('Opção inválida!')
        
    else:
        input(f'Cliente com ID {id_cliente} não encontardo. Pressione enter!')
        
        
'''def alterar_voo(): 
        
    conn = sqlite3.connect("C:\Repositorios\Passagens_aerea\Banco_dados.db")
    cursor = conn.cursor()
        
    id_voo = input('Qual a identificação do Voo a ser ALTERADO?: ')
        
    cursor.execute('SELECT numero_voo FROM voo WHERE id_voo = ?', (id_voo))
    voo = cursor.fetchone()
        
    if voo:
        print()
        numero_voo2 = voo[0]
        opcao_alterar = input(f'Deseja realmente alter o cliente: {numero_voo2} ? (1 - Sim/ 2 - Não): ')
        
        if opcao_alterar == '1':
            novo_numero_voo = input('Numero do Voo: ')
            nova_origem = input('Origem: ')
            novo_destino = input('Destino:')
            nova_data_partida = input('Data de partida: ')
            nova_data_chegada = input('Data de chegada: ')
            nova_duracao = input('Duração: ')
            
        
            dados_voo = (novo_numero_voo, nova_origem, novo_destino, nova_data_partida, nova_data_chegada, nova_duracao, id_voo)
        
            cursor.execute('UPDATE voo SET numero_voo = ?, origem = ?, destino = ?, data_partida = ?, data_chegada = ?, duracao = ? WHERE id_voo = ?',
                (dados_voo))
        
            conn.commit()
            print()
            input('Deseja continuar alterando voos? Pressione enter!')
            conn.close()    
        elif opcao_alterar == '2':
            input('Voo NÃO atualizado. Pressione enter!')
        else:
            input('Opção inválida!')
        
    else:
        input(f'Voo com ID {id_voo} não encontardo. Pressione enter!')
        
def alterar_aeroporto(): 
        
    conn = sqlite3.connect("C:\Repositorios\Passagens_aerea\Banco_dados.db")
    cursor = conn.cursor()
        
    id_aeroporto = input('Qual a identificação do aeroporto a ser ALTERADO?: ')
        
    cursor.execute('SELECT nome_aeroporto FROM aeroporto WHERE id_aeroporto = ?', (id_aeroporto))
    aeroporto = cursor.fetchone()
        
    if aeroporto:
        print()
        nome_aeroporto2 = aeroporto[0]
        opcao_alterar = input(f'Deseja realmente alter o Aeroporto: {nome_aeroporto2} ? (1 - Sim/ 2 - Não): ')
        
        if opcao_alterar == '1':
            novo_nome_aeroporto = input('Nome do Aeroporto: ')
            novo_codigo_iata = input('Código IATA: ')
            nova_cidade = input('Cidade:')
            novo_pais = input('País : ')
        
            dados_aeroporto = (novo_nome_aeroporto, novo_codigo_iata, nova_cidade, novo_pais, id_aeroporto)
        
        
            cursor.execute('UPDATE aeroporto SET nome_aeroporto = ?, codigo_iata = ?, cidade = ?, pais = ? WHERE id_aeroporto = ?',
                (dados_aeroporto))
        
            conn.commit()
            print()
            input('Deseja continuar alterando Aeroporto? Pressione enter!')
            conn.close()    
        elif opcao_alterar == '2':
            input('Aeroporto NÃO atualizado. Pressione enter!')
        else:
            input('Opção inválida!')
        
    else:
        input(f'Aeroporto com ID {id_aeroporto} não encontardo. Pressione enter!')
'''