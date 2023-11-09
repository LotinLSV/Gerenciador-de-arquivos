import PySimpleGUI as sg
import os



Layout = [
    [sg.Text('Entre com o nome do arquivo')],
    [sg.InputText()],
    [sg.Text('Entre com o texto')],
    [sg.InputText()],
    [sg.Listbox(["","","",""],size=(20,5))],
    [sg.Button('Criar arquivo'), sg.Button('Adicionar texto'), sg.Button('Excluir arquivo'), sg.Button('Sair')]

]

i = 0

Janela = sg.Window('Gerenciador de arquivos', Layout)

while True:
    caminho = f'C:/Users/lucas/OneDrive/Documentos/Projetos em python/Gerenciador-de-arquivos/{valorD}'
    evento, valores = Janela.read()
    valorD = valores[0]
    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break
    # elif evento == 'Testar':
    #     print(f'{valores[0]}'),
    #     print(f'{valores[1]}')
        
    elif evento == 'Criar arquivo':
        with open (f'{valores[0]}', 'w')as arquivo:
            Janela['Listbox'].insert(i,f'{valores[0]}'),
            arquivo.write(f'{valores[1]}'),
            i =+ 1
            
    elif evento == 'Adicionar texto':
        with open('Exemplo de arquivo.txt','a') as arquivo:
            arquivo.write(f'\n{valores[1]}')
            
    elif evento == 'Excluir arquivo':
        if os.path.exists(caminho):
            os.remove(caminho)
        else:
            print(f'O arquivo Exemplo de arquivo.txt não existe mais')

    