import os
restaurante = ['pizza', 'sorvete', 'bolo']

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    # os.system('clear') 
    print('Finalizando o app')

def voltar_menu_principal():
    input('\n Digite uma tecla para volar para o menu ')
    main()

def opcao_invalida():
    print('Opção inválida\n')
    voltar_menu_principal()

def exibir_subtitulo():

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos resaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurante.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu_principal()
       

def listar_restaurantes():
    os.system('cls')
    print('Listando restaurantes\n')
    
    for restaurantes in restaurante:       
        print(f'.{restaurantes}')

    voltar_menu_principal()
       

    # 'para cada resturante na lista *restaurantes*
        # 'nome'

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
    # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        
        elif opcao_escolhida == 3: 
            print('Ativar restaurante')
        
        elif opcao_escolhida == 4:
            finalizar_app()
        
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()