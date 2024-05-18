#CEFSA - Centro Eduacional da Fundação Salvador Arena
#FESA - Faculdade Engenheiro Salvado Arena
#Enzo Brito Alves de Oliveira - RA: 082220040
#Erikson Vieira Queiroz - RA: 082220021
#Heitor Santos Ferreira - RA: 081230042
#William Santim - RA: 082220033
#Engenharia de Computação - 4° Semestre - EC4
#PBL - Project Based Learning

# 1. Realizando instalação forçada das bibliotecas usadas ao longo do software
# 1.1. Importando biblioteca nativa do python chamada de 'subprocess', capaz de realizar execuções diretamente na run do powershell da máquina
import subprocess

# 1.2. Realizando comando de instalação das bibliotecas
subprocess.run(['pip', 'install', 'PySimpleGUI'])
subprocess.run(['pip', 'install', 'pyautogui'])

# 2. Realizando importação das bibliotecas principais que serão usadas ao longo do software
# 2.1. Importando biblioteca com o nome de pyautogui, resposável por executar as telas de alerta e de comando subsequente
import pyautogui as pag

# 2.2. Importando biblioteca com o nome de PySimpleGUI, responsável por trazer as visualizações gráficas e elementos visuais ao software
import PySimpleGUI as sg

# 3. Criando função resposável por exibir a tela de informações sobre os participantes do grupo
# 3.1. Atribuindo nome a variável/função
def telaParticipantesDoGrupo():

    #3.1.1. Criando tela de confirmação simples apenas com um botão de 'Ok' para exibir o cabeçalho da atividade
    pag.confirm(
        
                    text='CEFSA - Centro Eduacional da Fundação Salvador Arena\n FESA - Faculdade Engenheiro Salvador Arena\n Enzo Brito Alves de Oliveira - RA: 082220040\n Erikson Vieira Queiroz - RA: 082220021\n Heitor Santos Ferreira - RA: 081230042\n William Santim - RA: 082220033\n Engenharia de Computação - 4° Semestre - EC4\n PBL - Project Based Learning',
                    title='Integrantes do grupo', #<--- 3.1.1.1. Alterando titulo da página de popup
                    buttons=['Ok'] #<--- 3.1.1.2. Atribuindo os botões

                )

# 4. Criando função responsável por executar os calculos e exibir a tela principal de interação com o usuário
# 4.1. Atribuindo nome à variável/função
def inicializarSoftware():

    # 4.1.1. Criando variaveis de pré-definição de fontes a serem usadas ao longo da execução
    fonte_texto = ('Segoe UI Semibold', 12)
    fonte_input = ('Arial', 12)

    # 4.1.2. Criando layout da página principal
    layout = [

                # 4.1.2.1. Criando linha de texto digitavel com recebimento de valor digitado para atribuição do valor de Tensão Primária
                [sg.Text('Digite a tensão no primário', font=fonte_texto, justification='center'), sg.Input(key='valorTensaoPrimario', size=(40, 1), font=fonte_input, justification='center')],

                # 4.1.2.2. Criando linha de texto digitavel com recebimento de valor digitado para atribuição do valor do número de espiras no setor primário
                [sg.Text('Digite o número de espiras no primário', font=fonte_texto, justification='center'), sg.Input(key='valorNumeroEspirasPrimario', size=(40, 1), font=fonte_input, justification='center')],

                # 4.1.2.3. Criando linha de texto digitavel com recebimento de valor digitado para atribuição do valor do número de espiras no setor secundário
                [sg.Text('Digite o número de espiras no secundário', font=fonte_texto, justification='center'), sg.Input(key='valorNumeroEspirasSecundario', size=(40, 1), font=fonte_input, justification='center')],

                # 4.1.2.4. Criando os dois botões de execução final da página
                [sg.Button('Calcular!'), sg.Button('Sair')]

            ]

    # 4.1.3. Difinindo modelos de execução da tela principal e alterando o titulo
    janela = sg.Window('PBL - 4° Semestre - Engenharia de Computação', layout, finalize=True, )

    # 4.1.4. Criando laço de repetição contínua da página gráfica
    while True:

        # 4.1.4.1. Atribuindo o modelo de coleta dos valores digitados e de eventos realizados pelos botões
        evento, valores = janela.read()

        # 4.1.4.2. Criando condição de execução caso a tela seja fechada normalmente ou o usuário clique no botão de 'Sair' -----> O software é enecerrado em ambas as ocasiões
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            break
            exit()

        # 4.1.4.3. Criando condição de execução caso o usuário clique no botão de 'Calcular!'
        if evento == 'Calcular!':

            # 4.1.4.3.1. Criando função de tentativa de execução normal
            try:

                # 4.1.4.3.1.1. Obtendo o valor digitado na 'input box' presente na tela gráfica que recebe a keyValue de 'valorTensaoPrimario'
                valor_variavel_valorTensaoPrimario = valores['valorTensaoPrimario']

                # 4.1.4.3.1.2. Convertendo o valor de númerico digitado em string para um valor em float
                valor_variavel_valorTensaoPrimario = float(valor_variavel_valorTensaoPrimario)

                # 4.1.4.3.1.3. Obtendo o valor digitado na 'input box' presente na tela gráfica que recebe a keyValue de 'valorNumeroEspirasPrimario'
                valor_variavel_valorNumeroEspirasPrimario = valores['valorNumeroEspirasPrimario']

                # 4.1.4.3.1.4. Convertendo o valor de númerico digitado em string para um valor em float
                valor_variavel_valorNumeroEspirasPrimario = float(valor_variavel_valorNumeroEspirasPrimario)

                # 4.1.4.3.1.5. Obtendo o valor digitado na 'input box' presente na tela gráfica que recebe a keyValue de 'valorNumeroEspirasPrimario'
                valor_variavel_valorNumeroEspirasSecundario = valores['valorNumeroEspirasSecundario']

                # 4.1.4.3.1.6. Convertendo o valor de númerico digitado em string para um valor em float
                valor_variavel_valorNumeroEspirasSecundario = float(valor_variavel_valorNumeroEspirasSecundario)
                
                # 4.1.4.3.1.7. Calculando o valor da relação da transformação
                relacao_transformacao = valor_variavel_valorNumeroEspirasPrimario/valor_variavel_valorNumeroEspirasSecundario

                # 4.1.4.3.1.8. Calculando o valor da voltagem secundária
                voltagem_secundario = valor_variavel_valorTensaoPrimario/relacao_transformacao

                # 4.1.4.3.1.9. Exibindo os valores digitados e os resultados obtidos
                sg.popup(

                            f'Valor digitado para a tensão primária: {valor_variavel_valorTensaoPrimario}',
                            f'Valor digitado para o número de espiras primário: {valor_variavel_valorNumeroEspirasPrimario}',
                            f'Valor digitado para o número de espiras secundário: {valor_variavel_valorNumeroEspirasSecundario}',
                            '',
                            '#-----Resultados------#',
                            f'Valor calculado da relação da transformação: {relacao_transformacao}',
                            f'Valor calculado da voltagem secundária: {voltagem_secundario}',
                            font=fonte_texto,
                            title='Resultados'
                        
                        )
                
            # 4.1.4.3.2. Criando execução de exibição caso ocorra algum erro durante a tentativa normal de execução do código
            except ValueError as descricao_erro:

                sg.popup(f'Erro: {descricao_erro}', font=fonte_texto) 

    # 4.1.4.4. Fechando janela caso o loop while de execução continua se encerre
    janela.close()

# 5. Realizando execução de página de confirmação do usuário sobre desejo de executar o software verdadeiramente
escolha_usuario = pag.confirm(text='O software será iniciado, deseja continuar?', title='PBL - 4° Semestre - Engenharia de Computação', buttons=['Continuar', 'Cancelar'])

# 6. Realizando checagem de de resposta obtida perante ao clique dos botões
# 6.1. Criando modelo de condição de execução caso o usuário clique em 'continuar'
if escolha_usuario == 'Continuar':

    # 6.1.1. Executando a função que exibe a tela de participantes do grupo
    telaParticipantesDoGrupo()

    # 6.1.2. Executando a função responsável por executar o software principal
    inicializarSoftware()

# 6.2. Criando modelo de condição de execução caso o usuário clique em 'cancelar'
elif escolha_usuario == 'Cancelar':

    # 6.2.1. Encerrando software
    exit()