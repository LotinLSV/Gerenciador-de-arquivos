import PySimpleGUI as sg
import os

caminho = 'C:/Users/lucas/OneDrive/Documentos/Projetos em python/Gerenciador-de-arquivos/Exemplo de arquivo.txt'

Layout = [
    [sg.Text('Entre com o texto')],
    [sg.InputText()],
    [sg.Button('Criar arquivo'), sg.Button('Adicionar texto'), sg.Button('Excluir arquivo'), sg.Button('Sair')]

]

Janela = sg.Window('Gerenciador de arquivos', Layout)

while True:
    evento, valores = Janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break
    elif evento == 'Criar arquivo':
        with open ('Exemplo de arquivo.txt', 'w') as arquivo:
            arquivo.write(f'{valores[0]}')
    elif evento == 'Adicionar texto':
        with open('Exemplo de arquivo.txt','a') as arquivo:
            arquivo.write(f'\n{valores[0]}')
    elif evento == 'Excluir arquivo':
        if os.path.exists(caminho):
            os.remove(caminho)
        else:
            print(f'O arquivo Exemplo de arquivo.txt não existe mais')

