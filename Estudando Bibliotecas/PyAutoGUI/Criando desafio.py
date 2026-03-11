#Desafio criar um programa que mostre a posição do mouse em tempo real.
import pyautogui
import time

try:
    print('Aperte Ctrl + C para parar leitura')
    while True:
        eixoX, eixoY = pyautogui.position()
        print(f"X: {eixoX}  Y:{eixoY}")
        time.sleep(1.1)
except KeyboardInterrupt:
    print('Programa finalizado!')