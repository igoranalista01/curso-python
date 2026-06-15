import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo':False},
                {'nome': 'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo':False}]

def exibir_nome_do_programa():
      '''Essa função é responsável por exibir o nome principal do programa'''
      print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
      """)

def exibir_opcoes():
      '''Essa função é responsável por exibir as opções no menu principal'''
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Alternar estado do resturante')
      print('4. Sair\n')

def finalizar_app():
    '''Exibe mensagem de finalizar o aplicativo '''
    exibir_subtitulo('Finalizando o app')
    voltar_ao_menu_principal()
   
def voltar_ao_menu_principal():
     '''Solicita uma tecla para voltar ao menu principal
     
     Outputs:
     - Digite uma tecla para voltar ao menu principal

     '''
     input('\nDigite uma tecla para voltar ao menu principal: ')
     main()

def opcao_invalida():
     '''Exibe uma mensagem de opção invalida
      Outputs:
      - Voltar ao menu principal
     '''
     print('Opção inválida\n')
     voltar_ao_menu_principal()

def exibir_subtitulo(texto):
     '''Exibe o subtitulo estilizado na tela
     Inputs:
     - texto: O texto do subtitulo
     
     '''
     os.system('cls')
     linha = '*' *(len(texto))
     print(linha)
     print(texto)
     print(linha)
     print()

def cadastrar_novo_restaurante():
     '''Essa função é responsável por cadastrar um novo restaurante
     
     Inputs:
     - Nome do restaurante
     - Categoria do restaurante

     Outputs:
     - Adiciona  um novo restaurante a lista de restaurantes

     '''
     exibir_subtitulo('Cadastros de novos restaurantes')
     nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
     categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
     dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo':False}
     restaurantes.append(dados_do_restaurante)
     print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
     voltar_ao_menu_principal()
     
def listar_restaurantes():
     ''' Exibe os restaurantes presentes na lista

     Outputs:
     - Exibe a lista de restaurantes na lista

     '''
     exibir_subtitulo('Listando restaurantes')

     print(f'{'Nome do restaurante:'.ljust(22)} | {'Categoria:'.ljust(20)} | {'Status:'}') 
     for restaurante in restaurantes:
          nome_restaurante = restaurante['nome']
          categoria = restaurante['categoria']
          ativo = 'ativado' if restaurante ['ativo'] else 'desativado'
          print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

     voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Altera o estado dos restaurantes ativado/desativado
    Outputs:
    -Exibe a mensagem indicando o sucesso da operação

    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
      print('O restaurante não foi encontrado.')
        
    voltar_ao_menu_principal()  
       
            

def escolher_opcoes():
      '''Solicita  e executa a opção escolhida pelo usuario
      Outputs:
      - Executa a opção escolhida pelo usuario
      '''
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

      except:
           opcao_invalida()
def main():
    '''Função principal que inicia o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()