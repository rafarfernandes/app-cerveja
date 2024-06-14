import os 

cervejas = [
    {'nome': 'Stella Artois', 'categoria': 'Pilsen', 'ativo':False},
    {'nome': 'Eisenbahn IPA', 'categoria': 'IPA', 'ativo':True},
    {'nome': 'Eisenbahn Stout', 'categoria': 'Stout', 'ativo':False}]

def exibir_logo():
    print("""
██████╗░███████╗██╗░░░░░██╗██╗░░░██╗███████╗██████╗░██╗░░░██╗
██╔══██╗██╔════╝██║░░░░░██║██║░░░██║██╔════╝██╔══██╗╚██╗░██╔╝
██║░░██║█████╗░░██║░░░░░██║╚██╗░██╔╝█████╗░░██████╔╝░╚████╔╝░
██║░░██║██╔══╝░░██║░░░░░██║░╚████╔╝░██╔══╝░░██╔══██╗░░╚██╔╝░░
██████╔╝███████╗███████╗██║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░
╚═════╝░╚══════╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░

░█████╗░███████╗██████╗░██╗░░░██╗███████╗░░░░░██╗░█████╗░
██╔══██╗██╔════╝██╔══██╗██║░░░██║██╔════╝░░░░░██║██╔══██╗
██║░░╚═╝█████╗░░██████╔╝╚██╗░██╔╝█████╗░░░░░░░██║███████║
██║░░██╗██╔══╝░░██╔══██╗░╚████╔╝░██╔══╝░░██╗░░██║██╔══██║
╚█████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗╚█████╔╝██║░░██║
░╚════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝""")
    
def exibir_opcoes():
    print('1. Cadastrar cerveja')
    print('2. Listar cervejas')
    print('3. Alterar disponibilidade da cerveja')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_nova_cerveja():
    exibir_subtitulo('Cadastro de novas cervejas')
    nome_da_cerveja = input('Digite o nome da cerveja que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria da cerveja {nome_da_cerveja}: ')
    dados_da_cerveja = {'nome':nome_da_cerveja, 'categoria':categoria, 'ativo':False}
    cervejas.append(dados_da_cerveja)
    print(f'A cerveja {nome_da_cerveja} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_cervejas():
    exibir_subtitulo('Listando cervejas')

    print(f'{'Nome da cerveja'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for cerveja in cervejas:
        nome_cerveja = cerveja['nome']
        categoria = cerveja['categoria']
        ativo = 'ativado' if cerveja['ativo'] else 'desativado'
        print(f'- {nome_cerveja.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_cerveja():
    exibir_subtitulo('ALterando estado da cerveja')
    nome_cerveja = input('Digite o nome da cerveja que deseja alterar o estado: ')
    cerveja_encontrado = False

    for cerveja in cervejas:
        if nome_cerveja == cerveja['nome']:
            cerveja_encontrado = True
            cerveja['ativo'] = not cerveja['ativo']
            mensagem = f'A cerveja {nome_cerveja} foi ativado com sucesso' if cerveja['ativo'] else f'A cerveja {nome_cerveja} foi desativado com sucesso'
            print(mensagem)
            
    if not cerveja_encontrado:
        print('A cerveja não foi encontrado')
            
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_cerveja
        if opcao_escolhida == 1: 
            cadastrar_nova_cerveja()
        elif opcao_escolhida == 2: 
            listar_cervejas()
        elif opcao_escolhida == 3: 
            alternar_estado_cerveja()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_logo()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()