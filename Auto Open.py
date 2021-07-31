from time import sleep
import pyautogui as pa
# confirmação
confirmação = pa.confirm(text='Por favor retire as mãos do teclado', title='Cuidado', buttons=['OK', 'Cancel'])
while confirmação  == 'OK':
    #alert
    pa.alert('Tire as mão do teclado e mouse o script ira iniciar')
    # start brave
    pa.press('win')
    sleep(1)
    pa.write('brave')
    sleep(1)
    pa.press('enter')
    sleep(2)
    # start whatsapp
    pa.press('winleft')
    sleep(1)
    pa.write('whatsapp')
    sleep(1)
    pa.press('enter')
    sleep(2)
    # start files explorer
    pa.press('winleft')
    sleep(1)
    pa.write('explorador')
    sleep(1)
    pa.press('enter')
    # alert
    pa.alert('O script foi finalizado!')
    break
if confirmação == 'Cancel':
    quit()
