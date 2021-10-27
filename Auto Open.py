from PySimpleGUI import PySimpleGUI as sg  
from time import sleep
import os
from pyautogui import press, write

sg.theme('SystemDefault')

layout = [
    [sg.Text('Aplicativos a serem executados: ')],
    [sg.Checkbox('Navegador', default=False, key='Navegador')],
    [sg.Checkbox('Whatsapp', default=False, key='Whatsapp')],
    [sg.Checkbox('Explorador de arquivos', default=False, key='Arquivos')],
    [sg.Checkbox('Configurações do mouse', default=False, key='Configs')],
    [sg.Button('Play', key='Abrir'), sg.Button('Quit', key='Quit')]
]

janela = sg.Window('Nero1Dev', layout)

while True:

    events, values = janela.read()

    if events == sg.WIN_CLOSED or events == 'Quit':
        quit()
        break
    
    if events == 'Abrir':
        janela.hide()
        if values['Navegador'] is True:
            os.system(r'C:\Users\Nero1Dev\AppData\Local\Vivaldi\Application\vivaldi.exe')
            '''press('Winleft')
            write('Aplicativos: Vivaldi')
            sleep(1)
            press('enter')
            sleep(3.5)'''

        if values['Whatsapp'] is True:
            os.system(r'C:\Users\Nero1Dev\AppData\Local\WhatsApp\WhatsApp.exe')
            '''press('Winleft')
            write('Aplicativos: Whatsapp')
            sleep(1)
            press('enter')
            sleep(3.5)'''

        if values['Arquivos'] is True:
            os.system(r'%SystemRoot%\Explorer.exe')
            '''press('Winleft')
            write('Aplicativos: Explorador de arquivos')
            sleep(1)
            press('enter')
            sleep(3.5)'''
            
        if values['Configs'] is True:
            press('Winleft')
            write('mouse')
            sleep(1)
            press('enter')
            sleep(3.5)
        sleep(3)
        janela.UnHide()
