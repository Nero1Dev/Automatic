from PySimpleGUI import PySimpleGUI as sg  
from time import sleep
from pyautogui import press, write

sg.theme('SystemDefault')

layout = [
    [sg.Text('Aplicativos a serem executados: ')],
    [sg.Checkbox('Navegador', default=False, key='Navegador')],
    [sg.Checkbox('Whatsapp', default=False, key='Whatsapp')],
    [sg.Checkbox('Explorador de arquivos', default=False, key='Arquivos')],
    [sg.Checkbox('Configurações do mouse', default=False, key='Configs')],
    [sg.Button('Quit', key='Quit'), sg.Button('Abrir', key='Abrir')]
]

janela = sg.Window('AUTOMATIC', layout)

while True:

    events, values = janela.read()

    if events == sg.WIN_CLOSED or events == 'Quit':
        break
    
    if events == 'Abrir':
        if values['Navegador'] is True:
            press('Winleft')
            write('Aplicativos: Brave')
            press('enter')
            sleep(3.5)

        if values['Whatsapp'] is True:
            press('Winleft')
            write('Aplicativos: Whatsapp')
            press('enter')
            sleep(3.5)

        if values['Arquivos'] is True:
            press('Winleft')
            write('Aplicativos: Explorador de arquivos')
            press('enter')
            sleep(3.5)
            
        if values['Configs'] is True:
            press('Winleft')
            write('configurações do mouse')
            sleep(3.5)
