from time import sleep
from pyautogui import press, write, alert, confirm
# alert
confirmação = confirm(text='Por favor retire as mãos do teclado', title='Cuidado', buttons=['OK', 'Cancel'])
while confirmação  == 'OK':
    # start brave
    press('winleft')
    sleep(1)
    write('brave')
    sleep(1)
    press('enter')
    sleep(2)
    # start whatsapp
    press('winleft')
    sleep(1)
    write('whatsapp')
    sleep(1)
    press('enter')
    sleep(2)
    # start files explorer
    press('winleft')
    sleep(1)
    write('explorador')
    sleep(1)
    press('enter')
    # alert
    alert('O script foi finalizado!')
    break
if confirm == 'Cancel':
    quit()
