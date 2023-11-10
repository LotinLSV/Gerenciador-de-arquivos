import PySimpleGUI as sg

def main():
    # Definindo o layout da interface gráfica
    layout = [
        [sg.Text("Insira um valor:")],
        [sg.InputText(key='input_value'), sg.Button('Adicionar', key='add_button')],
        [sg.Listbox(values=[], size=(30, 5), key='listbox')],
        [sg.Button('Fechar')]
    ]

    # Criando a janela
    window = sg.Window('Exemplo de ListBox com PySimpleGUI', layout)

    # Inicializando a lista para armazenar os valores
    values_list = []

    # Loop principal para interação com a interface
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Fechar':
            break
        elif event == 'add_button':
            # Adicionando o valor à lista e atualizando a ListBox
            input_value = values['input_value']
            if input_value:
                values_list.append(input_value)
                window['listbox'].update(values=values_list)
                window['input_value'].update('')  # Limpar o campo de entrada após adicionar o valor

    # Fechando a janela ao sair do loop principal
    window.close()

if __name__ == "__main__":
    main()
