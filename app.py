import os

restaurantes = [
    {'nome': 'Paiol', 'categoria': 'Brasileira', 'ativo': False},
    {'nome': 'La Braciera', 'categoria': 'Italiana', 'ativo': True},
    {'nome': 'Inari Sushi', 'categoria': 'Japonesa', 'ativo': False},
]

def exibir_nome_do_programa():
    """
    Exibe o nome estilizado do programa no terminal.
    
    Esta função imprime um cabeçalho artístico em ASCII com o nome da aplicação.
    Não recebe nem retorna nenhum valor.
    """
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")


def exibir_opcoes():
    """
    Exibe o menu principal com as opções disponíveis para o usuário.

    Mostra as opções numeradas e não retorna nenhum valor.
    """
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')


def finalizar_app():
    """
    Exibe uma mensagem de encerramento da aplicação.
    
    Não recebe nem retorna nenhum valor.
    """
    exibir_subtititulo('Finalizando aplicação... Até mais!')


def voltar_ao_menu_principal():
    """
    Aguarda uma entrada do usuário e retorna ao menu principal.

    Exibe uma mensagem solicitando que o usuário pressione uma tecla
    para voltar ao menu principal e chama a função `main()`.
    """
    input('\nDigite uma tecla para voltar ao menu principal...')
    main()


def opcao_invalida():
    """
    Trata opções inválidas digitadas pelo usuário.

    Exibe uma mensagem de erro e retorna ao menu principal.
    """
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtititulo(texto):
    """
    Exibe um subtítulo formatado na tela.

    Args:
        texto (str): O texto que será exibido como subtítulo.

    Cria uma linha de asteriscos proporcional ao tamanho do texto
    e o exibe de forma destacada.
    """
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    """
    Cadastra um novo restaurante na lista global `restaurantes`.

    Solicita ao usuário o nome e a categoria do restaurante,
    adiciona os dados à lista e define o status inicial como inativo.

    Não retorna valores; atualiza a lista global.

    Inputs:
    - Nome do restaurante 
    - Categoria do restaurante 

    Outputs:
    - Adiciona um novo restaurante à lista `restaurantes`.
    """
    exibir_subtititulo('Cadastrar novo restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'\nRestaurante {nome_do_restaurante} cadastrado com sucesso!\n')
    voltar_ao_menu_principal()


def listar_restaurantes():
    """
    Lista todos os restaurantes cadastrados na aplicação.

    Exibe uma tabela com colunas para nome, categoria e status (ativo/inativo).
    Não recebe nem retorna valores.
    """
    exibir_subtititulo('Listando os restaurantes:')

    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def escolher_opcao():
    """
    Lê e executa a opção escolhida pelo usuário no menu principal.

    Usa um bloco try/except para tratar erros de entrada.
    Direciona o fluxo de execução conforme a opção informada.
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except ValueError:
        opcao_invalida()


def alternar_estado_restaurante():
    """
    Altera o estado (ativo/inativo) de um restaurante.

    Solicita o nome do restaurante ao usuário e busca-o na lista.
    Se encontrado, alterna o valor booleano do campo 'ativo'.
    Caso contrário, exibe uma mensagem informando que não foi encontrado.
    """
    exibir_subtititulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (
                f'O restaurante {nome_restaurante} foi ativado com sucesso!'
                if restaurante['ativo']
                else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            )
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')

    voltar_ao_menu_principal()


def main():
    """
    Função principal da aplicação.

    Limpa o terminal, exibe o cabeçalho e o menu principal,
    e direciona o fluxo para a função `escolher_opcao()`.
    """
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
