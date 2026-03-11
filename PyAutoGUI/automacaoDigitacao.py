import pyautogui
import time

time.sleep(5)
pyautogui.hotkey('win')
pyautogui.write('bloco de notas')
pyautogui.press('enter')
time.sleep(0.2)
pyautogui.write('Estou aprendendo automação com Python')
pyautogui.press('enter')
pyautogui.write('PyAutoGUI é muito poderoso')