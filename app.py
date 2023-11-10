import PySimpleGUI as sg
import os



Layout = [
    [sg.Text('Entre com o nome do arquivo')],
    [sg.InputText()],
    [sg.Text('Entre com o texto')],
    [sg.InputText()],
     [sg.Listbox([], size=(40, 6), key='registros')],
    [sg.Button('Criar arquivo'), sg.Button('Adicionar texto'), sg.Button('Excluir arquivo'), sg.Button('Sair')]

]

i = 0

Janela = sg.Window('Gerenciador de arquivos', Layout)

# def carregar_registros():
#     try:
#         with open('registros.txt', 'r') as arquivo:
#             registros = [linha.strip() for linha in arquivo.readlines()]
#     except FileNotFoundError:
#         registros = []
#     return registros

registros = []

while True:

    evento, valores = Janela.read()
    valorD = valores[0]
    caminho = f'C:/Users/lucas/OneDrive/Documentos/Projetos em python/Gerenciador-de-arquivos/{valorD}'
    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break
    # elif evento == 'Testar':
    #     print(f'{valores[0]}'),
    #     print(f'{valores[1]}')

    elif evento == 'Criar arquivo':
        with open (f'{valores[0]}', 'w')as arquivo:
            Title = f'{valores[0]}'
            registros.append(Title)
            Janela['registros'].update(values=registros)
            arquivo.write(f'{valores[1]}')
            # Janela['{valores[0]}'].update('')
            
    elif evento == 'Adicionar texto':
        selected = valores['registros'][0]
        with open(f'{selected}','a') as arquivo:
            arquivo.write(f'\n{valores[1]}')
            
    elif evento == 'Excluir arquivo':
        selected = valores['registros'][0]
        registros.remove(selected)
        caminho = f'C:/Users/lucas/OneDrive/Documentos/Projetos em python/Gerenciador-de-arquivos/{selected}' 
        if os.path.exists(caminho):
            os.remove(caminho)
            Janela['registros'].update(values=registros)
        else:
            print(f'O arquivo Exemplo de arquivo.txt não existe mais')